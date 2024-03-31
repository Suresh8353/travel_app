# Travel App

This is a Django project for managing travel destinations.

## Setup

1. Clone the repository:

   https://github.com/Suresh8353/travel_app.git

2. Install dependencies:

    pip install -r requirements.txt

3. Apply migrations (makemigrations and migrate):
    
    A. python manage.py makemigrations
    B. python manage.py migrate

4. Run the development server:

    python manage.py runserver

5. API Documentation
   Endpoints

   List Destinations: GET /api/destinations/
   Create Destination: POST /api/destinations/
   Retrieve Destination: GET /api/destinations/<destination_id>/
   Update Destination: PUT /api/destinations/<destination_id>/
   Delete Destination: DELETE /api/destinations/<destination_id>/