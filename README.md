# Travel App

This is a Django project for managing travel destinations.

## Project Setup

1. Clone the repository:

   https://github.com/Suresh8353/travel_app.git

2. Create virtual environment

3. Install dependencies:

    pip install -r requirements.txt

4. Apply migrations (makemigrations and migrate):
    
    A. python manage.py makemigrations
    B. python manage.py migrate

5. Run the development server:

    python manage.py runserver

6. Run test case
   python manage.py test

7. API Documentation
   Endpoints

   List Destinations: GET /api/destinations/
   Create Destination: POST /api/destinations/
   Retrieve Destination: GET /api/destinations/<destination_id>/
   Update Destination: PUT /api/destinations/<destination_id>/
   Delete Destination: DELETE /api/destinations/<destination_id>/


## Postman setup

1. Open Postman.
2. Select the Endpoint and paste in link bar or write endpoint here.
3. Send the Request: Click on the "Send" button to send the request to the API endpoint.
4. Review the Response: Once the request is sent, review the response received from the server. 