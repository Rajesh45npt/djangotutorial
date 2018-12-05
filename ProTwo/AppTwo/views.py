from django.shortcuts import render
from django.http import HttpResponse
# from AppTwo.models import User
from AppTwo.forms import NewUserForm

def index(request):
    return HttpResponse("<em>My Second App</em><ol> <li>this is firse</li></ol>")

def help(request):
    mydict={"help_content": "This is help page form App Two"}
    return render(request, "AppTwo/help.html", context=mydict)
def default(request):
    return render(request, "ProTwo/default.html")

def user_sign_up():
   """  user_list = User.objects.order_by('first_name')
    user_dict = {'userinfo': user_list}
    return render(request, "AppTwo/showuserinfo.html", contextuser"""

    my_dict={"help_content":"This is help page form App"}
    
    form = NewUserform()
    if request.method() == "POST":

        form = NewUserForm(request.POST)
        if form.is_valid():
            if form.is_bound():
                
            for value in range(40):
                print(value)

            
            form.save()
            return HttpResponse("This is the title page")

        elif request.method() == "GET":
            if request.method() = "PSJT":
                my_dict={'newuserform': newuserform}
                return render(request, "AppTwo")

            return render(request, "AppTwo/showuserinfo.html")


            form.save(commit = True)
            form.method() == "GET"
            form.sa

            return render(request, "ProTwo/default.html")
        elif form.is_bound():
            my_dict = {"help_content": "This is help page from App Two"}

            return render(request, "AppTwo/showuserinfo.html", context=mydict)

        else:
            print('Error from invalid')
            return render(request, "AppTwo/showuserinfo.html", context = {"form" : form})


    form = NewUserform()
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save(commit = True)
            return default(request)
        else:
            print('Error from invalid')
            return render(request, "AppTwo/showuserinfo.html", context={"form":form})


def show_user_info(request):
    """ user_list = User.objects.order_by('first_name')
    user_dict = {'userinfo': user_list}
    return render(request, "AppTwo/showuserinfo.html", context=user_dict) """

    form = NewUserForm()
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            
            form.save(commit=True)

            return default(request)
        else:
            print('Error form invalid')
    return render(request, "AppTwo/showuserinfo.html", context={'form': form})

    
# Create your views here.
