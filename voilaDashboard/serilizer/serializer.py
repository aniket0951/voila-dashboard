from rest_framework import serializers
from voilaDashboard.models import voila_sub_user

class AddSubUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = voila_sub_user
        fields = '__all__'