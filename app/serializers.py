from rest_framework import serializers
from .models import Parent, Child


class ParentSerializer(serializers.ModelSerializer):
    children = serializers.StringRelatedField(many=True, read_only=True)
    address = serializers.ReadOnlyField()
    class Meta:
        model = Parent
        fields = ['id', 'first_name', 'last_name', 'street', 'city', 'state', 'zip', 'children', 'address']


class ChildSerializer(serializers.ModelSerializer):
    address = serializers.ReadOnlyField()
    get_parent = serializers.ReadOnlyField()

    class Meta:
        model = Child
        fields = ['id', 'first_name', 'last_name', 'get_parent', 'address', 'parent']








