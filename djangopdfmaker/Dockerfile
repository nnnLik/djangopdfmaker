FROM python:3.11-slim AS builder

RUN apt-get update && \
    apt-get install --no-install-recommends -y \
    build-essential \
    python3-dev \
    python3-pip \
    python3-cffi \
    libcairo2 \
    libpango-1.0-0 \
    libpangocairo-1.0-0 \
    libgdk-pixbuf2.0-0 \
    libffi-dev \
    shared-mime-info \
    && apt-get autoremove -y && apt-get clean -y && rm -rf /var/lib/apt/lists/*

FROM builder AS dependencies

WORKDIR /usr/src/app

COPY ./requirements.txt ./

RUN pip install --upgrade pip && pip install -r requirements.txt

FROM dependencies AS final

COPY . /usr/src/app/

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
