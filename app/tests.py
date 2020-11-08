from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Parent, Child
from .serializers import ParentSerializer, ChildSerializer

PARENT_URL = reverse('app:parent-list')
CHILD_URL = reverse('app:child-list')


class ParentApiTest(TestCase):  # Test the parent api

    def setUp(self):
        self.client = APIClient()

    def test_retrieve_parent_list(self):  # Test retrieving a list of parents
        Parent.objects.create(first_name='a', last_name='b', street='c', city='d', state='e', zip='f')
        Parent.objects.create(first_name='g', last_name='h', street='i', city='j', state='k', zip='l')

        res = self.client.get(PARENT_URL)
        parents = Parent.objects.all().order_by('first_name')
        serializer = ParentSerializer(parents, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)


class ChildApiTest(TestCase):  # Test the child api

    def test_retrieve_child_list(self):  # Test retrieving a list of children
        p1 = Parent.objects.create(first_name='a', last_name='b', street='c', city='d', state='e', zip='f')
        p2 = Parent.objects.create(first_name='g', last_name='h', street='i', city='j', state='k', zip='l')
        Child.objects.create(first_name='a', last_name='b', parent=p1)
        Child.objects.create(first_name='c', last_name='d', parent=p2)

        res = self.client.get(CHILD_URL)
        children = Child.objects.all()
        serializer = ChildSerializer(children, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)







