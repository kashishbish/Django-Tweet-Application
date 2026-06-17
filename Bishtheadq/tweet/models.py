from django.db import models
from django.contrib.auth.models import User
# Create your models here.
 
class Tweet(models.Model):

    #one to one
    user=models.ForeignKey(User,on_delete=models.CASCADE) #har ek tweet ek user se associated ho,bina user k tweet na ho,unknown tweets ni lere
    #user-->konsi table ko refer krre , Referential integrity maintain karta hai ,CASCADE ka matlab hai parent delete → child bhi delete.
    text= models.TextField(max_length=240) #isme hamare pass ek option or tha vo h CharField
    photo=models.ImageField(upload_to='photos/',blank=True,null=True) #blank=True,null=True -->bina photo k bhi tweet allowed h
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    #automatically add ho jaega or auto_now true jb add hoga tbi run hoga
    #databse m help krta h accountability rkhne k liye kb ky add hua

    def __str__(self):
        return f'{self.user.username}-{self.text[:10]}'
