from django.urls import reverse
from rest_framework.test import APIClient, APITestCase
from rest_framework import status


class DestinationAPITestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()

    def test_destination_list(self):
        url = reverse('destinations-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_destination_create(self):
        url = reverse('destinations-list')
        data = {
            'name': 'New Destination',
            'country': 'New Country',
            'description': 'New Description',
            'best_time_to_visit': 'New Time',
            'category': 'Beach',
            'image_url': 'http://example.com/new_image.jpg'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], data['name'])

    def test_destination_update(self):
        # Create a destination first
        create_url = reverse('destinations-list')
        create_data = {
            'name': 'Test Destination',
            'country': 'Test Country',
            'description': 'Test Description',
            'best_time_to_visit': 'Test Time',
            'category': 'Mountain',
            'image_url': 'http://example.com/test_image.jpg'
        }
        create_response = self.client.post(create_url, create_data, format='json')
        self.assertEqual(create_response.status_code, status.HTTP_201_CREATED)
        destination_id = create_response.data['id']

        # Update the destination
        update_url = reverse('destinations-detail', kwargs={'pk': destination_id})
        update_data = {
            'name': 'Updated Destination',
            'country': 'Updated Country',
            'description': 'Updated Description',
            'best_time_to_visit': 'Updated Time',
            'category': 'City',
            'image_url': 'http://example.com/updated_image.jpg'
        }
        response = self.client.put(update_url, update_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['Detail']['name'], update_data['name'])
