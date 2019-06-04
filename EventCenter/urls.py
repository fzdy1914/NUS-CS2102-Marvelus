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
from django.conf.urls import url
from django.urls import path

from .views import auth_view, channel_view, event_view, comment_view, like_view

urlpatterns = [
    path('channels/', channel_view.channel_list, name='channels'),
    path('events/', event_view.event_list, name='events'),
    path('event/<int:pk>/', event_view.event_detail, name='event'),
    path('comments/<int:event_id>/', comment_view.comment_list, name='comments'),
    path('likes/<int:event_id>/', like_view.like_list, name='likes'),
    path('login/', auth_view.login, name='login'),
    path('logout/', auth_view.logout, name='logout'),
    path('reject/', auth_view.reject, name='reject'),
    url(r'', auth_view.default, name='default')
    # path('add/', views_helper.add_likes),
]
