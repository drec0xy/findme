from django.urls import path
from .views import login_view, create_user_view, home_view, logout_view

urlpatterns = [
    path('login/', login_view, name='login'),
    path('signup/', create_user_view, name='signup'),
    path('', home_view, name='home'),
    path('logout/', logout_view, name='logout'),
]
