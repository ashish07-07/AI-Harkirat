
FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    MANIM_MEDIA_DIR=/app/media

WORKDIR /app


RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    gcc \
    pkg-config \
    python3-dev \
    libcairo2-dev \
    libpango1.0-dev \
    libgirepository1.0-dev \
    ffmpeg \
    libfreetype6-dev \
    libfontconfig1 \
    fonts-freefont-ttf \
    gir1.2-glib-2.0 \
    gobject-introspection \
    && rm -rf /var/lib/apt/lists/*


RUN mkdir -p /app/media/videos && \
    chmod -R 777 /app/media

COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

