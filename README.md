# FastAPI "To-Do List" Application

## Описание проекта
Это REST API для управления задачами, разработанное с использованием FastAPI. Приложение позволяет создавать, просматривать, обновлять и удалять задачи, а также фильтровать их по статусу. Данные хранятся в PostgreSQL. Проект контейнеризирован с использованием Docker и Docker Compose.

### Основной функционал:
- Создание задач.
- Получение списка задач с фильтрацией по статусу.
- Просмотр деталей задачи.
- Обновление задачи.
- Удаление задачи.

---

## Инструкции по локальному запуску

### 1. Предварительные требования
- Установить [Docker](https://www.docker.com/) и [Docker Compose](https://docs.docker.com/compose/).

### 2. Запуск проекта
1. Клонировать репозиторий:
   ```bash
   git clone https://github.com/Alryum/fast_api_todo_list.git
   ```
2. Создайть файл .env в корне проекта, можно просто скопировать и переименовать .env.example
3. Выполнить команду в коренвой директории проекта: 
    ```bash
    docker-compose up --build
    ```
4. После запуска приложение будет доступно по адресу: http://localhost:8000
5. Swagger-документация API доступна по адресу: http://localhost:8000/docs
  
## Инструкции по развертыванию на сервере
1. Аналогично с предыдущими пунктами склонировать репозиторий.
2. ```bash
   docker-compose up --build
   ```
3. Приложение будет доступно по домену или адресу сервера.  

## Примеры запросов curl   
1. Создание задачи
```bash
curl -X POST "http://localhost:8000/tasks/" \
-H "Content-Type: application/json" \
-d '{
    "title": "New Task",
    "description": "Description of the new task",
    "status": "todo"
}'
```
2. Получение списка задач с фильтрацией по статусу  
```bash
curl -X GET "http://localhost:8000/tasks/?status=todo" \
-H "Content-Type: application/json"
```  
3. Обновление задачи
```bash
curl -X PUT "http://localhost:8000/tasks/1/" \
-H "Content-Type: application/json" \
-d '{
    "title": "Updated Task",
    "description": "Updated description",
    "status": "in_progress"
}'
```  
4. Удаление задачи  
```bash
curl -X DELETE "http://localhost:8000/tasks/1/"
```  