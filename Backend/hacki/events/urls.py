from django.contrib import admin
from django.urls import path,include
from . import views
from .views import *
from .views import CommitteeListCreateView, CommitteeRetrieveUpdateDestroyView
from .views import StudentListCreateView, StudentRetrieveUpdateDestroyView
from .views import EventListCreateView, EventRetrieveUpdateDestroyView

urlpatterns = [
    path('api/committees/', CommitteeListCreateView.as_view(), name='committee-list-create'),
    path('api/committees/<int:pk>/', CommitteeRetrieveUpdateDestroyView.as_view(), name='committee-retrieve-update-destroy'),

    path('api/students/', StudentListCreateView.as_view(), name='student-list-create'),
    path('api/students/<int:pk>/', StudentRetrieveUpdateDestroyView.as_view(), name='student-retrieve-update-destroy'),

    path('api/events/', EventListCreateView.as_view(), name='event-list-create'),
    path('api/events/<int:pk>/', EventRetrieveUpdateDestroyView.as_view(), name='event-retrieve-update-destroy'),
    path('',views.index,name='index'),
]
