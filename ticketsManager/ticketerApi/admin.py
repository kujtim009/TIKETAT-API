from django.contrib import admin
from .models import (Regjionet, 
                        Reshtat, 
                        Ulset, 
                        Cmimet, 
                        Shitja, 
                        Ndeshjet, 
                        LlojiIndeshjeve
                        )


admin.site.register(Regjionet)
admin.site.register(Reshtat)
admin.site.register(Ulset)
admin.site.register(Cmimet)
admin.site.register(Shitja)
admin.site.register(LlojiIndeshjeve)
admin.site.register(Ndeshjet)

# Register your models here.
