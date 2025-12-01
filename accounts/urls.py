from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('profile/', views.profile_view, name='profile'),
    path('profile/upload-image/', views.upload_profile_image, name='upload_profile_image'),
    path('change-password/', views.change_password_view, name='change_password'),
]