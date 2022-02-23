from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.
class MyAccountManager(BaseUserManager):
    #Método para crear usuario
    def create_user(self, user_name, first_name, last_name, email, password=None):
        if not email:
            raise ValueError('El usuario necesita un email')
        if not user_name:
            raise ValueError('El usuario necesita un username')

        user = self.model(
            email = self.normalize_email(email),
            user_name = user_name,
            first_name = first_name,
            last_name = last_name,
        )
        user.set_password(password)
        user.save(using=self._db)

        return user
    #Método para crear super usuario
    def create_superuser(self, user_name, first_name, last_name, email, password):
        user = self.create_user(
            email      = self.normalize_email(email),
            user_name  = user_name,
            first_name = first_name,
            last_name  = last_name,
            password   = password,
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff  = True
        user.is_superadmin = True
        user.save(using = self._db)

        return user

class Account(AbstractBaseUser):
    
    #personalizadas
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    user_name = models.CharField(max_length=50, unique=True)
    email = models.CharField(max_length=100, unique=True)
    phone_number= models.CharField(max_length=100, unique=True)

    #campos obligatorios
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_superadmin = models.BooleanField(default=True)

    #configuración de username, cambia el nombre de usuario por el email
    USERNAME_FIELD  = 'email'
    REQUIRED_FIELDS = ['user_name', 'first_name', 'last_name']

    #instancia de clase  MyAccountManager para crear usuarios
    objects =  MyAccountManager()

    #elemento a listar en el admin del django
    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, add_label):
        return True