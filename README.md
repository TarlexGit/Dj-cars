## started

cd Dj-cars/backend
docker-compose up --build

### 1)

http://127.0.0.1:8000/admin/
login: admin
pass: admin

### 2)

http://127.0.0.1:8000/admin/integration/task/
ставим галку в модели "Execute" и сохраняем - запустится таска по сбору и сохранению данных

### 3)

проверяем результаты в апи
http://127.0.0.1:8000/api/cars/?model=&brand=&price=
