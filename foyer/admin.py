from django.contrib import admin
from .models import Evenement, Reservation, Chambre, Pension, ReservationChambre, PlatJournalier

admin.site.register(Evenement)
admin.site.register(Reservation)
admin.site.register(Chambre)
admin.site.register(Pension)
admin.site.register(ReservationChambre)
admin.site.register(PlatJournalier)