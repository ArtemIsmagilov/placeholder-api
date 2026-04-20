# Alternative jsonplaceholder with django

- Создать проект API как [jsonplaceholder](https://jsonplaceholder.typicode.com) на Django и DRF.

## Метрики производительности
- ![metrics](https://github.com/ArtemIsmagilov/placeholder-api/actions/runs/24561334193/attempts/1#summary-71810444885)

## Запуск проекта локально

- Активируем окружение
  ```bash
  cd djangotutorial
  python3 -m venv .venv
  . .venv/bin/activate
  ```
- Скачиваем зависимости
  ```bash
  pip install uv
  uv pip install -r pyproject.toml --all-extras
  ```
- Запускаем проект
  ```bash
  python manage.py migrate
  python manage.py loaddata f.json
  python manage.py runserver
  ```
- Запускаем тесты
  ```bash
  python manage.py test --parallel
  ```
- Запускаем тесты на покрытие кода
  ```bash
  coverage run -p --source='.' manage.py test --parallel
  coverage combine
  coverage report
  ```
- Проверяем стили кода
  ```bash
  ruff check
  ruff format --check
  ```
- Проверяем производительность конечной точки
  ```bash
  wrk -c 100 -t 4 -d 60 http://127.0.0.1:8000/placeholder_api/comments_list
  ```
- Запустить проект в докере
  ```bash
  docker compose up --build
  ```
- Проверяем работу OpenAPI
  ```bash
  open http://127.0.0.1:8000/api/schema/swagger-ui/
  ```
