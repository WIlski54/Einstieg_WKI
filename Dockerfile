FROM python:3.11-slim
WORKDIR /app
RUN apt-get update && apt-get install -y --no-install-recommends curl \
    && rm -rf /var/lib/apt/lists/*
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
# Muster statt Aufzählung: ein neues Modul wird nie vergessen.
COPY *.py ./
COPY templates/ templates/
COPY static/ static/
# Frühwarnung: fehlt ein Modul oder ein Paket, scheitert der Build statt erst der Container.
RUN python -c "import app" && rm -rf /app/data
RUN mkdir -p /app/data \
    && useradd -m -u 1000 appuser \
    && chown -R appuser:appuser /app
USER appuser
ENV PORT=5000
EXPOSE 5000
HEALTHCHECK --interval=30s --timeout=10s --start-period=15s --retries=3 \
    CMD curl -fsS "http://localhost:${PORT:-5000}/health" || exit 1
CMD ["gunicorn", "--config", "gunicorn.conf.py", "app:app"]
