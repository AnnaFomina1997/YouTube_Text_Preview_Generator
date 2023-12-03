# YouTube Text Preview Generator

## Описание
Это веб-приложение на Django, предназначенное для преобразования превью видео с YouTube в текст. Приложение извлекает текст из изображения превью и предоставляет его в удобном формате.

## Функционал
- **Преобразование превью в текст**: Приложение автоматически извлекает текст из изображения превью видео на YouTube.

## Методы REST API
1. **POST `http://localhost:8000/api/makeText/`**
   - Описание: Генерирует изображение превью для видео на YouTube.
   - Параметры запроса:
     - `video_url` (строка): Ссылка на видео на YouTube.
   - Пример запроса:
     ```json
     {
       "video_url": "https://www.youtube.com/watch?v=your_video_id"
     }
     ```
   - Пример ответа:
     ```json
     {
       "text": "Заголовок вашего видео на YouTube"
     }
     ```

## Postman Коллекция
- [Ссылка на Postman коллекцию](https://api.postman.com/collections/14852565-ccf6a9fa-6775-42cc-88cf-adf7678692f5?access_key=PMAT-01HGQYTWQM1NK2PDE7NTG9PEY2)

## Инструкция по развертыванию
1. Установите Docker и Docker Compose.
2. Склонируйте репозиторий: `git clone https://github.com/Izlaster/YouTube_Text_Preview_Generator.git`
3. Перейдите в директорию проекта: `cd YouTube_Text_Preview_Generator`
4. Зайти в файл src/config.py и установить туда свой API ключ от Youtube v3
   - [Ссылка для получения API ключа](https://console.cloud.google.com/apis/credentials)
6. Выполните команду: `docker-compose up -d`
7. Приложение будет доступно по адресу: `http://localhost:8000`


## Запуск Docker-Compose
В папке ./docker пропишите команду для запуска:

    ```
    docker-compose up -d 
    ``` 
