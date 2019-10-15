from luminus.models import User


class MyAuthenticationBackend:

    def authenticate(self, request, username=None, password=None):
        if username:
            user = User.objects.using("luminus")\
                .raw('SELECT * FROM Users WHERE uname = %s AND password = %s', [username, password])
            if user:
                return user[0]
        return None

    def get_user(self, user_id):
        user = User.objects.using("luminus").raw('SELECT * FROM Users WHERE uname = %s', [user_id])
        if user:
            return user[0]

        return None
