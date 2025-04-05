from django.contrib import admin
from django.urls import path

from django.conf.urls.static import static
from django.conf import settings
from main.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('clubs/', ClubsView.as_view(), name='clubs'),
    path('clubs/<int:club_id>/', ClubDetailsView.as_view(), name='club-details'),
    path('latest-transfers/', LatestTransfersView.as_view(), name='latest-transfers'),
    path('players/', PlayerView.as_view(), name='players'),
    path('u20-players/', PlayerU20View.as_view(), name='u-20players'),
    path('tryouts/', TryoutsView.as_view(), name='tryouts'),
    path('about/', AboutView.as_view(), name='about'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
