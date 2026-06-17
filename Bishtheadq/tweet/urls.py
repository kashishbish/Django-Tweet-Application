from django.urls import path

from . import views

urlpatterns = [
    # path('',views.index,name='index'),
    path('',views.tweet_list,name='tweet_list'),
    path('create/',views.tweet_create,name='tweet_create'),
    # tweet_id ese hi likhna pdega qki views k andr vese likha hua h
    #ye syntax directly data pass on kr deta h views ko--><int:tweet_id>/edit/
    path('<int:tweet_id>/delete/',views.tweet_delete,name='tweet_delete'),
     path('<int:tweet_id>/edit/',views.tweet_edit,name='tweet_edit'),
     path('register/',views.register,name='register'),
]

#settings.py m sb btana pdega define krna pdega ki kaha pr url aare h ,otherwise error aaega runtime pe 
#error->Request URL:	http://127.0.0.1:8000/accounts/login/?next=/tweet/create/
#login pe jara h other than register
#kaha kaha pr login logout redirect h