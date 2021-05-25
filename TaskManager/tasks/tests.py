from django.test import TestCase
from rest_framework.test import APIRequestFactory



factory = APIRequestFactory()
# request = factory.get('/tasks/3')

# request = factory.post('/tasks/3', {'title': 'new idea'})
request = factory.post('/comments/3', {'body': 'new idea'}, format='json')
