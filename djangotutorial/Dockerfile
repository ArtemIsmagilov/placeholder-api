FROM python:alpine
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/
WORKDIR /app
COPY . .
ENV DEBUG="False"
RUN uv venv && \
  uv pip install -r pyproject.toml --extra prod && \
  uv run python manage.py migrate && \
  uv run python manage.py loaddata chats.json dummy.json placeholder.json tasks.json
EXPOSE 8000
CMD ["uv", "run", "granian", "--workers", "4", "--interface", "wsgi", "mysite.wsgi:application"]
