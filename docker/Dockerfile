FROM python:3.10.7

COPY ./src .
COPY ./requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt
RUN pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
