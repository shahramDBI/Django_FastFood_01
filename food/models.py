from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Item(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=200)
    item_price = models.IntegerField()
    item_image = models.CharField(max_length=500, default="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR-_IXHpBmStVsAnXqctN_3u_ZIGLToyS-VjSWonFQRFYObK9vq0DuCscC_LiJvzfHSdFY&usqp=CAU")

    def __str__(self):
        return self.item_name

    def get_absolute_url(self):
        return reverse("food:detail", kwargs={"pk": self.pk})

