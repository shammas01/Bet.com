from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class BetModel(models.Model):
    name = models.CharField(max_length=200)
    price = models.PositiveIntegerField()
    max_slot = models.PositiveIntegerField()
    max_enroll = models.PositiveIntegerField(default=5)
    reward = models.PositiveIntegerField()
    second_price = models.PositiveIntegerField(null=True)
    tird_price = models.PositiveIntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    expeire = models.DateTimeField(null=True,blank=True)
    is_active = models.BooleanField(default=True)


    def __str__(self):
        return self.name
    

    def save(self, *args, **kwargs):
        self.second_price = self.reward // 2
        self.tird_price = self.reward // 5
        super().save(*args, **kwargs)


    
class Slot(models.Model):
    bet = models.ForeignKey(BetModel, on_delete=models.CASCADE)
    slot_number = models.PositiveIntegerField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self) -> str:
        return f"Slot {self.pk} for {self.bet.name}"




class WalletModel(models.Model):
    user = models.OneToOneField(User,on_delete=models.SET_NULL,null=True)
    amount = models.DecimalField(decimal_places=2,default=0.00,max_digits=15)
    last_update = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user)
    


