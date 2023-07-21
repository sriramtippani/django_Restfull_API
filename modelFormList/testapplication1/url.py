from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.urls import path, include

urlpatterns = ''
urlpatterns += path('%s/' % settings.DAJAXICE_MEDIA_PREFIX, include('dajaxice.urls')),

urlpatterns += staticfiles_urlpatterns()