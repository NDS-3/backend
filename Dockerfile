FROM python:3.10-slim

ENV DB_USERNAME=${DB_USERNAME} \
    DB_PASSWORD=${DB_PASSWORD} \
    DB_HOST=${DB_HOST} \
    DB_PORT=${DB_PORT} \
    DB_DATABASE_NAME=${DB_DATABASE_NAME} \
    AWS_REGION=${AWS_REGION} \
    AWS_COGNITO_USERPOOL_ID=${AWS_COGNITO_USERPOOL_ID} \
    AWS_COGNITO_APP_CLIENT_ID=${AWS_COGNITO_APP_CLIENT_ID}

WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]