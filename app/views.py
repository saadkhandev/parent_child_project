from .models import Parent, Child
from .serializers import ParentSerializer, ChildSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action


class ParentViewSet(viewsets.ModelViewSet):
    serializer_class = ParentSerializer
    queryset = Parent.objects.all()


class ChildViewSet(viewsets.ModelViewSet):
    serializer_class = ChildSerializer
    queryset = Child.objects.all()




