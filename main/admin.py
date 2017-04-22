from django.contrib import admin
from .models import Dom, Lics, Street, Nas_punkt, Kvartiry, Person, Lgoty, Tip_lgoty, Pribory, MarkiPriborov, Uslugi, Pribor_Lics


admin.site.register(Dom)
admin.site.register(Lics)
admin.site.register(Street)
admin.site.register(Nas_punkt)
admin.site.register(Kvartiry)
admin.site.register(Person)
admin.site.register(Lgoty)
admin.site.register(Tip_lgoty)
admin.site.register(Pribory)
admin.site.register(MarkiPriborov)
admin.site.register(Uslugi)


class Pribor_LicsAdmin(admin.ModelAdmin):
    filter_horizontal = ('pribor',)

admin.site.register(Pribor_Lics, Pribor_LicsAdmin)