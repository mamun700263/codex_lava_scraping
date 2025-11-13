# ---------- BASE IMAGE ----------
FROM mcr.microsoft.com/playwright/python:v1.50.0-jammy


# ---------- WORKDIR ----------
WORKDIR /app

# ---------- COPY LOCKED DEPENDENCIES ----------
COPY requirements.lock .

# Install exactly what you have on your device
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.lock

# ---------- COPY PROJECT ----------
COPY . .

# ---------- SECURITY ----------
RUN useradd -m appuser
USER appuser

# ---------- EXPOSE & RUN ----------
EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
