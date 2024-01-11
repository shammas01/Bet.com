from django.urls import path
from . views import BetEnrolling,SlotSelectView

urlpatterns = [
    path('list/<int:pk>/',BetEnrolling.as_view()),
    path("slot/<int:pk>/",SlotSelectView.as_view())
]
