from django.urls import path
from api.views import user_views

urlpatterns =[
    path('', user_views.getUsers, name='users'),
    path('register/', user_views.registerUser, name='register')
]