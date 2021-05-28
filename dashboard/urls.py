from django.shortcuts import redirect
from django.urls import path
from . import views

urlpatterns = [
#  """ URL Pattern for achievement section """ 
    path('add_achievement/',views.add_achievement,name='add_achievement'),
    path('update_achievement/<int:pk>/',views.update_achievement,name='update_achievement'),
    path('delete_achievement/<int:pk>/',views.delete_achievement,name='delete_achievement'),
    path('achievement/',views.achievement,name='achievement'),

# """ URL Pattern for profile """
    path('personal_profile/',views.personal_profile,name='personal_profile'),
    path('hackathon/',views.hackathon,name='hackathon'),
    path('public_profile/',views.publicProfileRedirect,name='publicProfileRedirect'),
    # path('coding_profile/',views.coding_profile,name='coding_profile'),
    # path('resume/',views.resume,name='resume'),
    
# """ URL pattern for hackathon """
    path('add_hackathon/',views.add_hackathon,name='add_hackathon'),
    path('update_hackathon/<int:pk>/',views.update_hackathon,name='update_hackathon'),
    path('delete_hackathon/<int:pk>/',views.delete_hackathon,name='delete_hackathon'),
    path('hackathon_list/',views.hackathon_list,name='hackathon_list'),

# """ URL pattern for project """
    path('add_project/',views.add_project,name='add_project'),
    path('project/',views.project,name='project'),
    path('update_project/<int:pk>/',views.update_project,name='update_project'),
    path('delete_project/<int:pk>/',views.delete_project,name='delete_project'),

# """ URL pattern for resources """
    path('resources/links/<str:category>/<str:subtopic>/',views.resources_links, name='resource_links'),
    path('resources/home/<str:category>/', views.resource_home, name ='resource_home'),
    
# """ URL pattern for articles """ 
    path('add_articles/',views.add_articles,name='add_articles'),
    path('article_list/',views.article_list,name='article_list'),
    path('update_article/<int:pk>/',views.update_article,name='update_article'),
    path('delete_article/<int:pk>/',views.delete_article,name='delete_article'),
   
# """ URL pattern for mentors """ 
    #  path('assign-task/',views.assign_task,name='assign_task'),
    #  path('manage-task/',views.manage_task,name='manage_task'),
    #  path('student-task/',views.student_task,name='student_task'),
    #  path('mentor-update/',views.mentor_update,name='mentor_update'),
    #  path('student-section/',views.student_section,name='student_section'),

#  """URL pattern for feedback """
    # path('feedback/', views.feedback, name='feedback'),

# """ URL pattern 404 """
    path('404_not_found/', views.not_found404,name='404_not_found'),
]
