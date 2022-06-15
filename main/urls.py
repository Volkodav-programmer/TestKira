from django.urls import path
from .views import start
app_name = 'main'

urlpatterns = [
    path('', start)
]