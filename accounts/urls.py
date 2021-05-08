from django.urls import path, include
from . import views
# from django.contrib.auth import views as auth_views


urlpatterns = [
    path('logout/',views.handlelogout, name='logout'),
    path('login/',views.login, name='login'),
    path('register/',views.registration, name='register'),

    path('', include('django.contrib.auth.urls')),

    # path('login/password_reset/',views.password_reset, name='password_reset'),
    # path('reset/confirm/',views.password_reset_confirm, name='password_reset_confirm'),
    # path('reset/done/',views.password_reset_complete, name='password_reset_complete'),
    # path('login/reset/email',views.password_reset_email, name='password_reset_email'),
]