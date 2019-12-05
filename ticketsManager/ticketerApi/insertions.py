from .models import Regjionet, Reshtat, Ulset, Cmimet, Shitja

    # regjioni = models.ForeignKey(Regjionet, on_delete=models.CASCADE)
    # reshti = models.ForeignKey(Reshtat, on_delete=models.CASCADE)
    # ulsa = models.CharField(max_length=10)
    # statusi = models.BooleanField(default = False)
insert1 = Ulset(regjioni="P101", reshti="A", ulsa=10, statusi=False)
insert1.save()