
Шпаргалка: https://habr.com/ru/companies/flant/articles/336654/

Запуск:
- Создать образ:

      docker build --no-cache -t scraper .
- Запуск контейнера:

        docker run -itd --name scraper --restart always scraper 
