from django.db import models


class CarMarka(models.Model):
    marka_name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.marka_name


class CarModel(models.Model):
    model_name = models.CharField(max_length=20)
    marka_name =models.ForeignKey(CarMarka, on_delete=models.CASCADE)

    def __str__(self):
        return self.model_name


class Car(models.Model):
    car_name = models.CharField(max_length=50)
    marka_name = models.ForeignKey(CarMarka, on_delete=models.CASCADE)
    model_name = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    year = models.PositiveIntegerField()
    color = models.CharField(max_length=15)
    millage = models.FloatField()
    price = models.PositiveIntegerField()
    volume = models.DecimalField(max_digits=20, decimal_places=1)
    have = models.BooleanField(default=True)
    description =models.TextField()
    video = models.FileField(upload_to='vid/', null=True, blank=True)
    image = models.ImageField(upload_to='img/', null=True, blank=True)

    def __str__(self):
        return self.car_name