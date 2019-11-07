from luminus.models import User
import hashlib

class MyAuthenticationBackend:

    def authenticate(self, request, username=None, password=None):
        if username:
            password = hashlib.md5(password).hexdigest()
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
