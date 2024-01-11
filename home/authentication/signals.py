from django.dispatch import receiver
from django.db.models.signals import post_save
from home.models import User, WalletModel



@receiver(post_save, sender=User)
def create_user_wallet_for_registerd_user(sender, instance, created, **kwargs):
    if created:
        # UserProfile.objects.create(user=instance)
        WalletModel.objects.create(user=instance)




# @receiver(post_save, sender=User)
# def create_user_wallet_for_registerd_user(sender, instance, created, **kwargs):
#     if created:
#         # UserProfile.objects.create(user=instance)
#         WalletModel.objects.create(user=instance)