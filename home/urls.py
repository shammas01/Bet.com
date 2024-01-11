from django.urls import path
from . views import BetCreatView,BetRetriveupdate

urlpatterns = [
    path('',BetCreatView.as_view(),name='bet_creat'),
    path('bet/<int:pk>/',BetRetriveupdate.as_view(),name='bet_update')
 
]