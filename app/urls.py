from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('',views.home, name='home'),
    path('resources/',views.resources, name='resources'),
    path('highlights/<int:pk>/',views.highlights, name='highlights'),
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)