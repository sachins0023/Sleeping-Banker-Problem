from .views import api_user_create, api_user_list, api_session_list
from django.urls import path

app_name = "App"

urlpatterns = [
    path('user/', api_user_list, name="user_list"),
    path('createuser/', api_user_create, name="user_create"),
    path('session/', api_session_list, name="session_list"),
]

