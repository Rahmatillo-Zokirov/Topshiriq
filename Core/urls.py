from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static


from mainApp.views import *
from statsApp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home.as_view(), name="home"),
    path('about/', About.as_view()),
    path('tryouts/', Tryouts.as_view(), name='tr'),
    path('clublar/', Clubs.as_view(), name='clublar'),
    path('transfers/', LatestTransfers.as_view(), name='transfers'),
    path('players/', Players.as_view(), name='players'),
    path('player_20/', Player_20.as_view(), name='player_20'),
    path('transfers_r/', Transfers_record.as_view(), name='transfers_r'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
