FROM python:3.9-slim

WORKDIR /workdir

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install dependencies

COPY pyproject.toml /workdir/
COPY app/ workdir/app/

RUN pip install --upgrade pip && pip install -e .

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
