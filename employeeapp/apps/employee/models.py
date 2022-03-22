from django.db import models
from apps.department.models import Department


class Employee(models.Model):
    
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    first_name = models.CharField("employee first name", max_length=32)
    last_name = models.CharField("employee last name", max_length=32)
    job = models.CharField("employee job",max_length=50)
    avatar = models.ImageField("employee image",upload_to="image-database/emoloyee", blank=True, null="True")

    
    class Meta:
        verbose_name = "Employee"
        verbose_name_plural = "Employees"


    def full_name(self):
        return f'{self.first_name} {self.last_name}'
    

    def __str__(self) -> str:
        return f'id:{self.id} - {self.first_name} - {self.job}'