from rest_framework import serializers
from addresses.models import Address


class AddressSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    line1 = serializers.CharField(max_length=256)
    line2 = serializers.CharField(required=False, allow_blank=True, max_length=256)
    city = serializers.CharField(max_length=256)
    state = serializers.CharField(max_length=2)
    zipcode = serializers.CharField(max_length=5)


    def create(self, validated_data):
        return Address.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.line1 = validated_data.get('line1', instance.line1)
        instance.line2 = validated_data.get('line2', instance.line2)
        instance.city = validated_data.get('city', instance.city)
        instance.state = validated_data.get('state', instance.state)
        instance.zipcode = validated_data.get('zipcode', instance.zipcode)
        instance.save()
        return instance