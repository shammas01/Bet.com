from django.http import Http404
from django.shortcuts import render
from rest_framework.views import APIView
from . serializers import SelectSlotSerializer,ListSlotSerializer
from rest_framework.views import Response
from home.models import BetModel,Slot
# Create your views here.

class BetEnrolling(APIView):
    def get(self, request,pk):
        slots = BetModel.objects.filter(id=pk)
        print(slots,">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        serializer = ListSlotSerializer(slots,many=True)
        return Response(serializer.data)



class SlotSelectView(APIView):
    def get(self, request,pk):
        try:
            slot = Slot.objects.get(id=pk)
        except Slot.DoesNotExist:
            raise Http404
        print(slot,'><<><>><><><><><><><><<>><>><><')
        if slot:
            serializer = SelectSlotSerializer(slot)
            return Response(serializer.data)
        return Response('slot is not exist')
    
    

        