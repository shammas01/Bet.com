from rest_framework import serializers
from . models import BetModel

class BetCreateSerailizer(serializers.ModelSerializer):
    class Meta:
        model = BetModel
        fields = '__all__'


class BetDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = BetModel
        fields = ['name','price','max_slot','reward','second_price','tird_price']

    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.price = validated_data.get('price',instance.price)
        instance.max_slot = validated_data.get('max_slot',instance.max_slot)
        instance.reward = validated_data.get('reward',instance.reward)
        instance.save()
        return instance