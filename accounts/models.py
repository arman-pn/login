from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser

class UserAccountsManager(BaseUserManager):    
    def create_user(self,email,name,password=None):
        if not email: 
            raise ValueError("Please provide an email address")
        else: 
            email = self.normalize_email(email)
            user = self.model(email = email,name = name)
            user.set_password(password)
            user.save()
            
            
            return user
    def create_superuser(self,email,name,password=None):
        user = self.create_user(email = email,name = name,password = password)    
        user.is_superuser = True
        user.is_staff = True
        user.save()
        
        
        return user
    
               
    












class UserAccounts(AbstractBaseUser):
    email = models.EmailField(max_length=255,unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    
    objects = UserAccountsManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']
    
    
    
    
    def has_perm(self,perm,obj=None):
        "Dose the user  have a specific permission?"
        return True
    def has_module_perms(self,app_lable):
        "Does the user have permission to viwe the app 'app_lable'?"
        return True
    
    def __str__(self):
        return self.email
        