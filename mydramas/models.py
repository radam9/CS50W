from django.db import models


class Network(models.Model):
    title = models.CharField(max_length=15)

    def __repr__(self):
        return self.title

    def __str__(self):
        return self.title


class Drama(models.Model):
    title = models.CharField(max_length=75)
    # country = models.CharField(max_length=25, default="South Korea")
    year = models.PositiveIntegerField()
    network = models.ForeignKey(
        "Network", on_delete=models.CASCADE, related_name="Network"
    )
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    mdlurl = models.URLField()
    favorite = models.BooleanField()
    epcount = models.PositiveIntegerField()
    eplength = models.PositiveIntegerField()
    watchdate = models.DateField()

    def __repr__(self):
        return self.title

    def __str__(self):
        return self.title
