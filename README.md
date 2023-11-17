# Django PDF Maker

This is a service designed to generate PDF files from a URL or HTML file. The service is built using Django, Django Rest Framework (DRF), Docker and Celery.

### Project Structure

The project includes the following components:

* Django: Web framework.
* Postgres: Database
* Celery: Task queue
* Redis: Message Broker, for Celery.
* Flower: Celery monitoring tool

### Installation

1. Clone the repository to your local machine.

2. Create an .env file in the root directory with the following contents:
```
# server
SECRET_KEY=sadpweomdonebicuvceuhbijcn
DEBUG=True

# database
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=database
DB_PORT=5432

POSTGRES_PASSWORD=postgres
POSTGRES_USER=postgres
POSTGRES_DB=postgres
POSTGRES_PORT=5432

# celery
CELERY_BROKER_URL=redis://redis:6379
CELERY_RESULT_BACKEND=redis://redis:6379
```

3. Build and run
```bash
docker-compose up --build
```

### Usage

* Access the admin panel at /admin with the following credentials:
```bash
Username: admin
Password: admin
```

* Swagger documentation is available at /swagger/.

### Endpoints

1. Generate PDF:

    * Endpoint: POST /api/core/generate-pdf/
    * Request: Submit either an HTML file or a URL.
    * Response:


```json
{
    "task_id": "2da82d6c-13a3-455d-a555-9d3c95caad5a",
    "result": "Processing started."
}
```

2. Check Task Status:

    * Endpoint: GET /api/core/tasks/{task_id}/
    * Response:

```json
{
    "id": "2da82d6c-13a3-455d-a555-9d3c95caad5a",
    "generated_pdf": {
    "id": 32,
    "pdf_file": "/media/generated_pdfs/2da82d6c-13a3-455d-a555-9d3c95caad5a.pdf",
    "created_at": "17.11.2023 06:02:16"
    },
    "status": "COMPLETED" | "IN_PROGRESS" | "ERROR",
    "status_message": "Task completed successfully.",
    "source_url": "....",
    "html_source_file": null,
    "created_at": "17.11.2023 06:01:45",
    "updated_at": "17.11.2023 06:01:45"
}
```

### Testin

Run the tests using the following command:

```bash
docker exec -it djangopdfmaker ./manage.py test
```
