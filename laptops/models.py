from django.db import models

class Laptop(models.Model):
    brand = models.CharField(max_length=100, verbose_name="ბრენდი")
    model = models.CharField(max_length=100, verbose_name="მოდელი")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="ფასი")
    processor = models.CharField(max_length=100, verbose_name="პროცესორი")
    ram = models.IntegerField(verbose_name="ოპერატიული მეხსიერება (გბ)")
    storage = models.IntegerField(verbose_name="შიდა მეხსიერება (გბ)")
    display = models.CharField(max_length=100, verbose_name="ეკრანი")
    graphics = models.CharField(max_length=100, verbose_name="გრაფიკა")

    def __str__(self):
        return f"{self.brand} {self.model}"

    class Meta:
        verbose_name = "ლეპტოპი"
        verbose_name_plural = "ლეპტოპები"