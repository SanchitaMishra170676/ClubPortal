from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.home, name='home'),
    path('achievements/',views.achievement,name='achievement'),
    path('recruitment/', views.recruitment, name = 'recruitment'),
    path('contact/',views.contact,name='contact'),
    path('gallery/',views.gallery, name='gallery'),
    path('team/',views.team, name='team'),
    path('blog/<slug:the_slug>/',views.blog, name='blog_article'), #for partiular bolg
    path('blogs/<slug:category>/',views.blog_list_category, name='blog_list_category'), # for listing according to category
    path('blogs/',views.blog_list, name='blog_list_category'), # for listing all articles    
    # path('password_reset/', views.password_reset_request, name="password_reset"),
    path('password_reset/',auth_views.PasswordResetView.as_view(template_name='home/password_reset_email.html'), name='password_reset_email' ),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='home/password_reset_confirm.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="home/password_reset.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='home/password_reset_complete.html'), name='password_reset_complete'),      

]