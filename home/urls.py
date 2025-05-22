from django.urls import path
from home import views
# from .views import upload_video

urlpatterns = [
    path('', views.home, name= 'home'),
    path('home/', views.home, name= 'home'),
    path('about/', views.about, name= 'about'),
    path('upload/', views.upload_video, name='upload_video')  # Ensure this is correct
]
