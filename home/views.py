from django.http import Http404
from django.shortcuts import render
from rest_framework.views import APIView
from . serializres import BetCreateSerailizer,BetDetailSerializer
from . models import BetModel
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated,IsAdminUser
# Create your views here.

class BetCreatView(APIView):
    # permission_classes = IsAdminUser

    def post(self, request):
        serializer = BetCreateSerailizer(data=request.data)
        if serializer.is_valid():
            data = BetModel.objects.create(
                name = serializer.validated_data.get('name'),
                price = serializer.validated_data.get('price'),
                max_slot = serializer.validated_data.get('max_slot'),
                reward = serializer.validated_data.get('reward'),
                
            )
            response = {'data':serializer.data,'msg':'bet created successfully'}
            return Response(response, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

    def get(self, request):
        data = BetModel.objects.all()
        serializer = BetCreateSerailizer(data,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    

class BetRetriveupdate(APIView):
    # permission_classes = IsAdminUser

    def get_object(self,pk):
        try:
             return BetModel.objects.get(id=pk)
        except BetModel.DoesNotExist:
            raise Http404


    def get(self, request, pk):
        bet = self.get_object(pk)
        serializer = BetDetailSerializer(bet)
        return Response(serializer.data,status=status.HTTP_200_OK)


    def put(self, request, pk):
        bet = self.get_object(pk)
        print(bet)
        serializer = BetDetailSerializer(bet, data=request.data)
        
        if serializer.is_valid():
            # reward = serializer.validated_data.get('reward')
            # if reward:
            #     bet.second_price = bet.reward // 2
            #     bet.tird_price = bet.reward // 5
            serializer.save()
            return Response({"messege":"bet is updated","data":serializer.data},status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk):
        bet = self.get_object(pk)
        bet.delete()
        return Response("bet was deleted")
    





