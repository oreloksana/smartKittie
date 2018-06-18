
from landing import views
from django.urls import path

urlpatterns = [
    path('mrrr/', views.landing, name='landing'),
]
