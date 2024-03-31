from django.test import TestCase
from destinations.models import Destination


class DestinationModelTestCase(TestCase):
    def setUp(self):
        self.destination = Destination.objects.create(
            name='Test Destination',
            country='Test Country',
            description='Test Description',
            best_time_to_visit='Test Time',
            category='Beach',
            image_url='http://example.com/image.jpg'
        )

        self.destination = Destination.objects.create(
            name='Test Destination2',
            country='Test Country2',
            description='Test Description2',
            best_time_to_visit='Test Time',
            category='Mountain',
            image_url='http://example.com/image2.jpg'
        )

    def test_models_data1(self):
        destinations = Destination.objects.all()
        self.assertEqual(destinations.count(), 2)
        self.assertEqual(destinations[0].name, 'Test Destination')
        self.assertEqual(destinations[0].country, 'Test Country')
        self.assertEqual(destinations[0].description, 'Test Description')

    def test_models_data2(self):
        destinations = Destination.objects.filter(name='Test Destination2')
        self.assertEqual(destinations[0].country, 'Test Country2')
        self.assertEqual(destinations[0].description, 'Test Description2')
