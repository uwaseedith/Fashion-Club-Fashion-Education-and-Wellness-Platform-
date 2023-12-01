from django.contrib.auth.models import BaseUserManager
class UserManager(BaseUserManager):
    def create_user(
        self,
        username,
        password=None,
    ):
        if not username:
            raise ValueError("Users Must Have A Phone Number")
        user = self.model(
            username=username,
        )
        password = username

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username,email, password=None):
        if not password:
            raise ValueError("User must have a password")
        if not username:
            raise ValueError("User must have a  username")
        # if not email:
        #     raise ValueError("User must have a  email")

        user = self.create_user(
            username=username,
            # email=email,
            password=password,
        )
        user.is_admin = True

        user.save(using=self._db)

        
        return user
