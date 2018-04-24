# api/serializers.py

from rest_framework import serializers
from .models import Bucketlist
from django.contrib.auth.models import User


class BucketlistSerializer(serializers.ModelSerializer):
    """ Serializer to map the Model instance into JSON format """

    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        """
        Map this serializer to a model and their fields
        """
        model = Bucketlist
        fields = ('id', 'name', 'owner', 'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')


class UserSerializer(serializers.ModelSerializer):
    """ a user serializer to aid in authentication and authentication."""

    bucketlists = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Bucketlist.objects.all()
    )

    class Meta:
        """ Map this serializer to the defaul django user model. """
        model = User
        fields = ('id', 'username', 'bucketlists')
