from django.urls import path
from . import views

urlpatterns = [
    path('personal_profile/education_update/<int:pk>/', views.personal_profile_education,name='personal_profile_education'),
    path('image_save/', views.personal_image_save,name='personal_image_save'),
    path('personal_profile/section/<str:section>/', views.personal_profile_section,name='personal_profile_section'),
    
    path('personal_profile/education_update/', views.education_profile,name='education_profile'),
    path('update_education_profile/<int:pk>/', views.update_education_profile,name='education_profile'),
    
    
    path('coding_profile/', views.coding_profile,name='coding_profile'),
    path('profile/',views.ClubProfiles,name='profile'),
    
    
    path('delete_skill/<int:pk>',views.delete_skill,name='delete_skill'),

    path('profile/<slug:the_slug>/',views.publicProfile,name='publicProfile'),
] 