from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import News, BookMarks
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
from django.core.paginator import Paginator
from .forms import NewsForm

# Register User
def user_register(request):
    if request.method == "GET":
        return render(request, 'register.html')
    else:
        uname = request.POST.get('uname')

        if User.objects.filter(username=uname).exists():
            umessage = "Username " + '"' + uname + '"' + " already exists"
            print(umessage)
            return render(request, 'register.html', {'umessage': umessage, 'title': 'Sign up page'})
        else:
            password = request.POST.get('password1')
            user = User.objects.create_user(uname)
            user.set_password(password)
            user.save()
            print('User created')
            return render(request, 'login.html')

#Login User
def User_login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        uname = request.POST.get('uname')
        password = request.POST.get('password')
        user = authenticate(username=uname, password=password)

        if user is not None:
            login(request, user)
            return redirect(index)
        else:
            return redirect(User_login)

def User_logout(request):
    logout(request)
    return redirect(index)

#Landing Page
def index(request):
    #books = BookMarks.objects.all().filter(user=request.user).values('news')
    #print(books)
    newses = News.objects.all()
    
    paginator = Paginator(newses, 10) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = { 'news':newses,
                'page_obj': page_obj}
    
    return render(request, 'Welcome.html', context)

#Full news
def full(request, id):
    
    news = News.objects.all().filter(id=id)
    return render(request, 'full.html', {'news':news})

#Add Bookmark
def create_bookmark(request, n_id):
    user = User.objects.get(id=request.user.id)
    news = News.objects.get(id=n_id)
    if BookMarks.objects.filter(user=user, news=news).exists():
        print('Not added')
    else:
        b = BookMarks(user = user, news=news)
        b.save()
    return redirect(index)

def get_bookmark(request):
    
    b = BookMarks.objects.all().filter(user = request.user.id).values('news')
    print(b)
    arr = []
    
    for a in b:
        arr.append(a['news'])
    
    N = News.objects.all().filter(id__in = arr)
    context = {'Books': N}

    return render(request, "bookmarks.html", context)


def Editor(request):

    if request.method == "GET":
        if request.user.is_staff:
            items = News.objects.all()
            context = {'items':items}
            return render(request, 'editor.html', context)
        else:
            return HttpResponse("You don't have permission to view this page")
   

def AddNews(request):
     if request.method=='GET':
         form = NewsForm()
         context = {'form': form}
         return render(request, 'AddNews.html', context)
     else:
        form = NewsForm(request.POST or None)
        if form.is_valid():
            obj = form.save()
        return redirect(index)

def EditNews(request, id):
    if request.method == "GET":
        news = News.objects.get(id=id)
        form = NewsForm(instance=news)  # No request.POST
        context = {'form': form, 'id':id}
        return render(request, 'EditNews.html', context)
    else:
        instance = News.objects.get(id=id)
        form = NewsForm(request.POST or None, instance=instance)
        if form.is_valid():
            form.save()
            return redirect(index)