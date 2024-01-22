import aiomysql
import logging
import asyncio


def check_connection(func):
    async def wrapper(self, *args, **kwargs):
        try:

            return await func(self, *args, **kwargs)

        except (aiomysql.InterfaceError, aiomysql.OperationalError):

            await self.connect()
            return await wrapper(self, *args, **kwargs)

    return wrapper


class Database:
    def __init__(self, loop, host, user, password, pool_size=5, ):
        self.pool = None
        self.loop = loop
        self.host = host
        self.user = user
        self.password = password
        self.pool_size = pool_size
        # self.db = db

    async def connect(self):
        try:
            self.pool = await aiomysql.create_pool(
                host=self.host,
                user=self.user,
                password=self.password,
                loop=self.loop,
                minsize=1,
                maxsize=self.pool_size,
            )
            logging.info('Database connection succeed')

        except Exception as e:
            logging.error(f'DB error: {str(e)}')

            self.pool = None


    @check_connection
    async def execute_query(self, query, args=None):
        async with self.pool.acquire() as conn:
            async with conn.cursor() as cur:
                await cur.execute(query, args)
                result = await cur.fetchall()
                await conn.commit()
                return result


    @check_connection
    async def execute_many(self, query, args=None):
        async with self.pool.acquire() as conn:
            async with conn.cursor() as cur:
                await cur.executemany(query, args)
                result = await cur.fetchall()
                await conn.commit()
                return result


    async def add_many_metal(self, data):
        async with self.pool.acquire() as conn:
            async with conn.cursor() as cur:
                query = "INSERT INTO Metall.Price (City, Company, Name, Price_Fiz, Price_Ur)" \
                        "VALUES (%s,%s,%s,%s,%s)"

                await cur.executemany(query, data)
                await conn.commit()


    async def get_exist_metal(self):
        async with self.pool.acquire() as conn:
            async with conn.cursor() as cur:

                query = "SELECT t1.City, t1.Company, t1.Name, t1.Price_Fiz, t1.Price_Ur " \
                        "FROM Metall.Price t1 " \
                        "LEFT JOIN Metall.Price t2 " \
                        "    ON t1.Name = t2.Name AND t1.Company = t2.Company " \
                        "    AND t1.City = t2.City AND t1.time < t2.time " \
                        "WHERE t2.time IS NULL " \
                        "ORDER BY t1.time DESC"

                await cur.execute(query)
                result = await cur.fetchall()
                return result


    async def compare_metal(self, data):
        async with self.pool.acquire() as conn:
            async with conn.cursor() as cur:

                old_data = await self.get_exist_metal()

                new_data = []

                for row in data:
                    if tuple(row) in old_data:
                        pass
                    else:
                        new_data.append(row)

                if len(new_data) > 0:
                    await self.add_many_metal(new_data)
                    logging.info(f"Added {len(new_data)} elements")
