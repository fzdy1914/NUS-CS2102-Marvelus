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

from luminus.views import views
from luminus.views import prof_view
from luminus.views import student_view
from luminus.views import TA_view

urlpatterns = [
    path('test/', views.template),

    path('course/<code>/', views.get_course),

    path('prof/<code>/', prof_view.get_profs_by_coursecode),
    path('prof/<username>/', prof_view.get_profs_by_username),
    path('TA/<code>/', TA_view.get_TAs_by_coursecode),
    path('TA/<code>/group_num/', TA_view.get_TAs_by_coursecode_and_groupnum),
    path('student/<code>/', student_view.get_students_by_coursecode),
    path('student/<code>/<group_num>/', student_view.get_students_by_coursecode_and_groupnum)

]
