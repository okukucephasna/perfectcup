# backend/Dockerfile

FROM python:3.11-slim

WORKDIR /app

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy backend code
COPY . .

# Copy frontend/build from host into container
COPY ./frontend_build ./frontend_build


# Tell Flask to serve from this folder instead
ENV FLASK_STATIC_FOLDER=frontend_build

CMD ["python", "app.py"]
