from django.db import models

class LocationVO(models.Model):
    import_href = models.CharField(max_length=200, unique=True)
    closet_name = models.CharField(max_length=100)
    section_number = models.PositiveSmallIntegerField(null=True)
    shelf_number = models.PositiveSmallIntegerField(null=True)

    def __str__(self):
        return self.closet_name

class Hat(models.Model):
    style_name = models.CharField(max_length=100)
    fabric = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    picture_url = models.CharField(null=True)

    location = models.ForeignKey(
        LocationVO,
        related_name='hats',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.style_name
