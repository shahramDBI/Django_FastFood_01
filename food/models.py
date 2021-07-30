from django.db import models


class Item(models.Model):
    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=200)
    item_price = models.IntegerField()
    item_image = models.CharField(max_length=500, default="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR-_IXHpBmStVsAnXqctN_3u_ZIGLToyS-VjSWonFQRFYObK9vq0DuCscC_LiJvzfHSdFY&usqp=CAU")

    def __str__(self):
        return self.item_name

