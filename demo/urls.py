from django.urls import path
from demo import views

urlpatterns = [
    path('rooms/', views.RoomList.as_view())
]
