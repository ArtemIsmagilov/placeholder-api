FROM python:alpine
WORKDIR /app
COPY . .
RUN pip install uv && \
  uv venv && \
  uv pip install -r pyproject.toml --extra prod && \
  uv run python manage.py migrate && \
  uv run python manage.py loaddata f.json
EXPOSE 8000
ENV DEBUG="False"
CMD ["uv", "run", "granian", "--workers", "4", "--host", "127.0.0.1", "--port", "8000", "--interface", "wsgi", "mysite.wsgi:application"]
