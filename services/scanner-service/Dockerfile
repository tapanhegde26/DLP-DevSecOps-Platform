FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip setuptools \
    && pip install --no-cache-dir -r requirements.txt

COPY . .

# Create non-root user
RUN useradd -m appuser
USER appuser

EXPOSE 8080

CMD ["uvicorn", "dlp_scanner.main:app", "--host", "0.0.0.0", "--port", "8080"]
