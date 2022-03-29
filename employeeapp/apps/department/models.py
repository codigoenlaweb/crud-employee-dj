from django.db import models

# Create your models here.
class Department(models.Model):
    name = models.CharField("Department name",max_length=50)
    short_name = models.CharField("department short name", max_length=20, unique=True)
    active = models.BooleanField("department in operation", default=True)


    class Meta:
        verbose_name = "Deparment"
        verbose_name_plural = "Deparments"


    def activate_or_not(self) -> str:
        return "department activate" if self.active else "department desactivate"

    def deparment_activate(self) -> str:
            return "active" if self.active else "inactive"

    def __str__(self) -> str:
        return f'{self.short_name}: {self.activate_or_not()}'