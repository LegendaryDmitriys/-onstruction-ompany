from django.db import models


class Test(models.Model):
    vopros = models.CharField(max_length=100)
    otvet = models.CharField(max_length=100)
    complexity = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.otvet} {self.vopros} {self.complexity}"

class Theme(models.Model):
    name = models.CharField(max_length=100)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} {self.test}"





