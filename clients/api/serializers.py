from rest_framework import serializers
from ..models import Client
#from django.contrib.auth.models import User


class ClientSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    email = serializers.ReadOnlyField(source='user.email')
    first_name = serializers.ReadOnlyField(source='user.first_name')
    last_name = serializers.ReadOnlyField(source='user.last_name')
    class Meta:
        model = Client
        fields = ['user_id','user','email','first_name','last_name','photo','sex']