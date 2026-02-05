from django.urls import path

from lections.views import lections

app_name = 'lections'

urlpatterns = [
    path('', lections, name='index')
]
