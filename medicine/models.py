from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=200, verbose_name="Имя доктора")

    def __str__(self):
        return self.name

class Visit(models.Model):
    doctor = models.ForeignKey(Doctor, related_name='visits', verbose_name="Doctor")
    name = models.CharField(max_length=200, verbose_name="Your name")
    datetime = models.DateTimeField(verbose_name="Date")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created")

    def __str__(self):
        return "%s -> %s (%s)" % (self.name, self.doctor, self.datetime.strftime("%d.%m.%Y %H:%M:%S"))