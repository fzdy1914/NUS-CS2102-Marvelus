from django.contrib.auth.models import User


def is_user_exists(pk):
    return User.objects.filter(pk=pk).exists()


def get_user(pk):
    return User.objects.get(pk=pk)
