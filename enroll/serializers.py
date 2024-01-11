from rest_framework import serializers
from home.models import BetModel,Slot
from home.serializres import BetCreateSerailizer



class SlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slot
        fields = '__all__'


class ListSlotSerializer(serializers.ModelSerializer):
    slot_set = SlotSerializer(many=True)
    class Meta:
        model = BetModel
        fields = ['id','name','slot_set']



class SelectSlotSerializer(serializers.ModelSerializer):
    bet = serializers.SerializerMethodField()
    class Meta:
        model = Slot
        fields = ['id','slot_number','bet']

    def get_bet(self, obj):
        bet = obj.bet
        return {
            'name': bet.name,
            'first_price': bet.price,
            'second_price': bet.second_price,
            'tird_price': bet.tird_price,
            'max_slot': bet.max_slot,
            'max_enroll': bet.max_enroll,
            'reward': bet.reward,
        }


