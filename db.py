import aiomysql
import logging
import asyncio


class Database:
    def __init__(self, loop, host, user, password, pool_size=5,):
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

    async def execute_query(self, query, args=None):
        try:
            async with self.pool.acquire() as conn:
                async with conn.cursor() as cur:
                    await cur.execute(query, args)
                    result = await cur.fetchall()
                    await conn.commit()
                    return result


        except (aiomysql.InterfaceError, aiomysql.OperationalError):

            await self.connect()
            return self.execute_query(query, args)

    async def execute_many(self, query, args=None):
        try:
            async with self.pool.acquire() as conn:
                async with conn.cursor() as cur:
                    await cur.executemany(query, args)
                    result = await cur.fetchall()
                    await conn.commit()
                    return result


        except (aiomysql.InterfaceError, aiomysql.OperationalError):

            await self.connect()
            return self.execute_query(query, args)