FROM python:alpine
WORKDIR /app
COPY . .
RUN pip install uv && \
  uv venv && \
  uv pip install -r pyproject.toml --extra prod
EXPOSE 8000
CMD ["uv", "run", "granian", "--host", "127.0.0.1", "--port", "8000", "--interface", "wsgi", "mysite.wsgi:application"]
