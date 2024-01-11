from django.db import models
from django.contrib.auth.models import User
from home.models import BetModel,Slot
# Create your models here.



class EnrollModel(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    bet = models.ForeignKey(BetModel,on_delete=models.CASCADE,null=True)
    slot = models.ForeignKey(Slot,on_delete=models.CASCADE)
    transaction_id = models.CharField(max_length=100, null=True, blank=True)

    name = models.CharField()
    
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} enrolled in {self.bet.name} for slot {self.slot.pk}"
    
    