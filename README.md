Добавление проекта:
- Инициализация git репозитория

           git init

- Подключение к удаленному репозиторию

            git remote add origin git@github.com:YarikATM/MetallScraper.git
- Скачивание репозитория

            git fetch origin

- Переключение на основную ветку

            git checkout main

Шпаргалка: https://habr.com/ru/companies/flant/articles/336654/

Запуск:
- Создать образ:

      docker build --no-cache -t scraper .
- Запуск контейнера:

        docker run -itd --name scraper --restart always scraper 
