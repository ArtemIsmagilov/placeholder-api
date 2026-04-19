FROM python:alpine
WORKDIR /app
COPY . .
ENV DEBUG="False"
RUN pip install uv && \
  uv venv && \
  uv pip install -r pyproject.toml --extra prod && \
  uv run python manage.py migrate && \
  uv run python manage.py loaddata f.json
EXPOSE 8000
CMD ["uv", "run", "granian", "--workers", "4", "--interface", "wsgi", "mysite.wsgi:application"]
