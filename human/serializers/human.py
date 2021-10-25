from rest_framework import serializers
from human.models import Human


class HumanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Human
        write_only_fields = ('id', 'created_at')
        fields = ['id',
                  'name',
                  'male',
                  'number',
                  'email',
                  'city',
                  'created_at']

