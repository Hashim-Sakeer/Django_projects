from django.urls import path
from django.http import HttpResponse
from schoolapp import views
app_name='schoolapp'
urlpatterns = [
    path('', views.home, name='home'),
    path('user/',views.user,name='user'),
    path('login/', views.login, name='login'),
    path('registration/', views.register, name='registration'),  # Ensure the name is 'register'
    path("logout",views.logout,name='logout'),
    path('student-form/', views.student_form, name='student_form'),
    path('success/',views.success,name='success'),
    path('get_courses/', views.get_courses, name='get_courses'),

]
