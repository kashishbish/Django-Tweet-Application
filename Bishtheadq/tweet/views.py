from django.shortcuts import render
from .models import Tweet
from .forms import TweetForm ,UserRegistrationForm
from django.shortcuts import get_object_or_404,redirect

from django.contrib.auth.decorators import login_required

from django.contrib.auth import login

# Create your views here.
def index(request):
    return render(request,'index.html')

def tweet_list(request):
    tweets=Tweet.objects.all().order_by('-created_at')
    return render(request,'tweet_list.html',{'tweets':tweets})

@login_required
def tweet_create(request):
    #form se request  request ko handle krna
    #user ko empty form dere h
    #user k pass sara form data vgera hamare pass aa chuka h toh usko render krana h
    if request.method=="POST":
        form=TweetForm(request.POST,request.FILES) #isse hum ab file b accept krre h
        #django m built in security features deta h jisse hum bta skte h form valid h ya ni h
        if form.is_valid(): #handles security measures
            #form kisne bhara h vo user v hamein chaiye
            tweet=form.save(commit=False)  #poora form save kr lia h ,lakin commit=False krne se hum usse btare h database m save ni krna h
            tweet.user=request.user
            tweet.save()
            #redirect kr dete ,through redirect import from shortcuts 
            return redirect('tweet_list')
    else:
        form=TweetForm()
    
    return render(request,'tweet_form.html',{'form': form})
    

@login_required
def tweet_edit(request,tweet_id):
    tweet=get_object_or_404(Tweet,pk=tweet_id,user=request.user)   #(model,primary key,user jo logged in ho -->apna hi tweet edit kr paye)

    if request.method=='POST':
        form=TweetForm(request.POST,request.FILES,instance=tweet) #jb b edit krre h toh instance dena pdta h taaki pta chale ki purana hi tweet edit kre ho
        if form.is_valid():
            tweet=form.save(commit=False)
            tweet.user=request.user
            tweet.save()
            return redirect('tweet_list')
    else:
        form=TweetForm(instance=tweet) #jitna b data h form use prefill dena h qki editable data h
    return render(request,'tweet_form.html',{'form': form})
    
@login_required    
def tweet_delete(request,tweet_id):
    tweet=get_object_or_404(Tweet,pk=tweet_id,user=request.user)
    if request.method=='POST':
        tweet.delete()
        return redirect('tweet_list')
    
    #POST request aane se pehle toh kuch na kuch toh show hoga hi ya render hoga
    return render(request,'tweet_confirm_delete.html',{'tweet': tweet})

def register(request): #taki user register kr paye
    #templates k andr poora ke registration krke folder bnayenge jb b  django ke default behviour ko hum tweak krre h accordingly

    if request.method=="POST":
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            #cleaned_data is used to take information from form inbuilt method

            user.save()

            login(request,user) #login ko auth se import kr lnge ye method
            #login k andr user pass kr denge
            #save krne k baad user login ho jae

            return redirect('tweet_list')
    else:
        form=UserRegistrationForm() #import kra lena oopr
    return render(request,'registration/register.html',{'form': form})

#ab hamein urls.py  se isko urls p le jaenge