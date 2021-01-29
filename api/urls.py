from django.urls import path
from . import views


urlpatterns = [
    path('events/<str:from_date>/<str:to_date>', views.events_view),
]
