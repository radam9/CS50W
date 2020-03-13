from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Network(models.Model):
    title = models.CharField(max_length=15)

    def __repr__(self):
        return self.title

    def __str__(self):
        return self.title


class Drama(models.Model):
    r = []
    for i in range(21):
        r.append((i / 2, i / 2))

    title = models.CharField(max_length=75)
    # country = models.CharField(max_length=25, default="South Korea")
    year = models.PositiveIntegerField(
        validators=[MinValueValidator(1900), MaxValueValidator(2100)]
    )
    network = models.ForeignKey(
        "Network", on_delete=models.CASCADE, related_name="Network"
    )
    rating = models.DecimalField(max_digits=3, decimal_places=1, choices=r)
    mdlurl = models.URLField()
    favorite = models.BooleanField()
    epcount = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(120)]
    )
    eplength = models.PositiveIntegerField(
        validators=[MinValueValidator(5), MaxValueValidator(120)]
    )
    watchdate = models.DateField()

    def __repr__(self):
        return self.title

    def __str__(self):
        return self.title
