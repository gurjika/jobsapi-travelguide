# Job Listing App

A Django-based web application for managing and interacting with companies and job listings. The app uses Django REST Framework to create APIs for companies and job listings, and includes user authentication and permissions.

## Features

- **Job Management**: Create, update, and delete job listings.
- **Company Management**: Create, update, and delete company profiles.
- **User Authentication**: Secure endpoints with authentication and permissions.
- **Filtering**: Filter job listings based on title.

## Tools Used

- **Django**: High-level Python web framework.
- **Django REST Framework (DRF)**: Toolkit for building Web APIs.
- **Django Filters**: Powerful filtering engine for DRF.
- **Nginx**: Configured as a reverse proxy to serve static and media files.
- **Gunicorn**: WSGI HTTP server for serving the Django application.
- **Docker**: Containerized the application for consistent development and deployment.
- **PostgreSQL**: Used as the database for the application.

## Swagger Documentation

To explore and test the API endpoints, visit the Swagger documentation at [http://localhost/swagger/schema](http://localhost/swagger/schema). This interactive documentation provides detailed information about each endpoint, including the expected request bodies, response formats, and query parameters.

## Setup

1. **Clone the Repository**

   ```bash
   git clone https://github.com/gurjika/jobsapi-travelguide


2. Change into the project directory:
    ```sh
    cd jobsapi-travelguide
    ```

3. Create a `.env` file and specify the required environment variables:
    ```env
    POSTGRES_PASSWORD=your_db_password
    POSTGRES_USER=user
    ```

4. Run the application using Docker Compose:
    ```sh
    docker-compose up -d
    ```

5. Run the database migrations:
    ```sh
    docker-compose run django python manage.py migrate
    ```
6. Collect Static files:
    ```sh
    docker-compose run django python manage.py collectstatic --no-input
    ```

7. Create a superuser:
    ```sh
    docker-compose run django python manage.py createsuperuser
    ```

8. Access the development server at [http://localhost/api](http://localhost/api).