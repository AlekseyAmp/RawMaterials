FROM python:3.11.3

WORKDIR /app

COPY server/requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY server ./

EXPOSE 8000

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
