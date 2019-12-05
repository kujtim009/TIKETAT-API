from django.db import models
from datetime import datetime, date

class Regjionet(models.Model):
    emri = models.CharField(db_index=True, max_length=10)
    hyrja = models.CharField(max_length=100, null=True, default="A", blank=True)

    def __str__(self):
        return self.emri


class Reshtat(models.Model):
    emri = models.CharField(db_index=True, max_length=5)
    def __str__(self):
        return self.emri


class Cmimet(models.Model):
    regjioni = models.ForeignKey(Regjionet, on_delete=models.CASCADE, related_name='relateds')
    reshti = models.ForeignKey(Reshtat, on_delete=models.CASCADE)
    cmimi = models.DecimalField(db_index=True, max_digits=6, decimal_places=2)

    @property
    def emri_i_regjionit(self):
        queryset = Regjionet.objects.filter(id=self.regjioni)
        return queryset[0].emri

    def __str__(self):
        return str(self.cmimi)


class Ulset(models.Model):
    regjioni = models.ForeignKey(Regjionet, on_delete=models.CASCADE)
    reshti = models.ForeignKey(Reshtat, on_delete=models.CASCADE)
    ulsa = models.CharField(max_length=10)
    statusi = models.BooleanField(default = False)
    cordinata = models.CharField(max_length=200, default=None, blank=True, null=True)
    class Metta:
        indexes = [
            models.Index(fields=['Regjioni', 'ulsa']),
            models.Index(fields=['Regjioni'], name='regjioni_idx'),
        ]

    @property
    def cmimi(self):
        queryset = Cmimet.objects.filter(regjioni=self.regjioni, reshti=self.reshti)
        return queryset[0].cmimi

    def __str__(self):
        return self.ulsa


class LlojiIndeshjeve(models.Model):
    titulli = models.CharField(max_length=100)
    def __str__(self):
        return str(self.titulli)

class Ndeshjet(models.Model):
    titulli = models.CharField(max_length=200)
    ndeshja = models.ForeignKey(LlojiIndeshjeve, on_delete=models.CASCADE)
    data = models.DateField(default=datetime.now().strftime("%m/%d/%Y"), blank=True)
    ora = models.TimeField(default=datetime.now().strftime("%H:%M"), blank=True)

    def __str__(self):
        return str(self.titulli)


class Shitja(models.Model):
    fatura = models.CharField(max_length=10)
    ndeshja = models.ForeignKey(Ndeshjet, on_delete=models.CASCADE)
    ulsa = models.ForeignKey(Ulset, on_delete=models.CASCADE)

    @property
    def cmimi(self):
        queryset = Cmimet.objects.filter(regjioni=self.ulsa.regjioni, reshti=self.ulsa.reshti)
        return queryset[0].cmimi