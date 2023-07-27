from django.db import models

class Advertisiment(models.Model):
    title = models.CharField(verbose_name="Название", max_length=128)
    description = models.TextField("Описание")
    price = models.DecimalField("Цена", max_digits=10, decimal_places=3)
    auction = models.BooleanField("Торг", help_text="укажите, если возможен торг")
    create_at = models.DateTimeField(auto_now_add=True)
    update_add = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "advertisiments"
    def __str__(self):
        return f"Advertisement(id={self.id}, title={self.title}, price={self.price})"
