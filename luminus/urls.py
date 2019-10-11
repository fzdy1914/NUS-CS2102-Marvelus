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

from luminus.views import views, course_view, prof_view, TA_view, student_view

urlpatterns = [
    path('test/', views.template),

    path('prof/code/<code>/', prof_view.get_profs_by_coursecode),
    path('prof/uname/<username>/', prof_view.get_profs_by_username),
    path('TA/code/<code>/', TA_view.get_TAs_by_coursecode),
    path('TA/<code>/<group_num>/', TA_view.get_TAs_by_coursecode_and_groupnum),
    path('student/code/<code>/', student_view.get_students_by_coursecode),
    path('student/<code>/<group_num>/', student_view.get_students_by_coursecode_and_groupnum),

    path('course/code/<code>/', course_view.get_course_by_code),
    path('course/puname/<puname>/', course_view.get_course_by_puname),
    path('course/tuname/<tuname>/', course_view.get_course_by_tuname),
    path('course/suname/<suname>/', course_view.get_course_by_suname),
]
