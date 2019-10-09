"""EntryTask URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path

from luminus.views import course_view,tut_view


urlpatterns = [
    path('test/', course_view.template),

    path('course/<code>/', course_view.get_course),


    path('tutorial/<code>/',tut_view.get_tutorials_by_coursecode),
    path('tutorial/<code>/<num>/',tut_view.get_tutorials_by_course_and_group),
    path('tutorial/<username>/',tut_view.get_tutorials_by_student),
    path('tutorial/<username>/<code>/',tut_view.get_tutorials_by_tA_and_course),
]
