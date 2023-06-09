"""changes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from tasks import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main, name='main'),
    path('register/', views.register, name='register'),
    path('tasks/', views.tasks, name='tasks'),
    path('tasks/completed/', views.tasks_completed, name='task_completed'),
    path('create/task/', views.save_task, name="create"),
    path('task/<int:id>', views.task_by_id, name="id"),
    path('task/<int:id>/complete', views.complete_task, name="complete"),
    path('task/<int:id>/delete', views.delete_task, name="delete"),
    path('logout/', views.singout, name='logout'),
    path('login/', views.login_user, name='login')
]
