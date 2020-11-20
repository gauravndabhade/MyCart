import peewee
from models import User

class UserSession(object):
    def read_current_user(self):
        """ Read user data from file (offline session for terminal)
            Return [username, is_admin]
        """

        try:
            with open(".current_user.dat", "r") as f:
                data = f.readline().split(',')
                if len(data) == 2:
                    return data
                else:
                    return None, None
        except FileNotFoundError:
            return None, None


    def write_current_user(self, username, is_admin):
        if username:
            with open(".current_user.dat", 'w', encoding='utf-8') as f:
                f.write(username + ',')
                f.write(str(is_admin))


    def current_user(self):
        try:
            username, _ = self.read_current_user()
            user = User.select().where(User.username == username).get()
            return user
            
        except peewee.DoesNotExist:
            return None
