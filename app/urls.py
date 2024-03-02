from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('',views.home, name='home'),
    path('resources/',views.resources, name='resources'),
    path('highlights/<int:pk>/',views.highlights, name='highlights'),
    path('login/', views.login_user, name='login-user'),
    path('sign-up/',views.register_user, name='register-user'),
    path('coming-soon/', views.coming_soon, name='coming-soon'),
    path('log-out/',views.logout_user, name='log-out'),
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)