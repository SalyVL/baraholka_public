from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CreateAdForm, EditProfile, EditAd
from django.contrib import messages
from .decorators import unauth_user, login_required
from django.contrib.auth import authenticate, login, logout
from .models import User, Ad
from django.forms import inlineformset_factory
from .filters import AdFilter

# Create your views here.
def home(request):
    ads = Ad.objects.all()
    filter = AdFilter(request.GET, queryset=ads)
    ads = filter.qs
    context = {'ads': ads, 'filter':filter}
    return render(request, 'home.html', context)

@unauth_user
def register(request):
    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data['email']
            messages.success(request, 'Вы успешно зарегистрировались! Используйте ' + username + ' для авторизации')
            return redirect('login')
    context = {'form':form}
    return render(request, 'register.html', context)

@unauth_user
def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Логин либо пароль введен неверно.')
    context = {}
    return render(request, 'login.html', context)

def logoutUser(request):
    if request.user.is_anonymous:
        return redirect('login')
    else:
        logout(request)
        return redirect('home')

def userProfile(request, pk):
    ads = Ad.objects.filter(owner = pk)
    profile = User.objects.get(id=pk)
    user_name = f'{profile.first_name} {profile.last_name[0]}'
    filter = AdFilter(request.GET, queryset=ads)
    ads = filter.qs
    context = {'profile':profile, 'user_name':user_name, 'ads':ads, 'filter': filter}
    return render(request, 'profile.html', context)

@login_required
def create_ad(request):
    form = CreateAdForm()
    if request.method == 'POST':
        form = CreateAdForm(request.POST, request.FILES)
        if form.is_valid():
            ad = form.save(commit=False)
            ad.owner_id = request.user.id
            ad.save()
            return redirect(f'/profile/{request.user.id}')
    context = {'form':form}
    return render(request, 'create_ad.html', context)

def ad_page(request, pk):
    ad = Ad.objects.get(id = pk)
    owner = User.objects.get(id = ad.owner_id)
    user_name = f'{owner.first_name} {owner.last_name[0]}'
    if request.method == 'POST':
        if ad.owner_id == request.user.id:
            ad.delete()
            return redirect('userPage', pk = request.user.id)
        else:
            return redirect('profile', pk = request.user.id)
    context = {'ad':ad, 'owner':owner, 'user_name':user_name}
    return render(request, 'ad.html', context)

@login_required
def edit_profile(request):
    profile = request.user
    form = EditProfile(instance=profile)
    if request.method == 'POST':
        form = EditProfile(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect(f'/profile/{request.user.id}')

    context = {'form':form}
    return render(request, 'edit_profile.html', context)

def edit_ad(request, pk):
    ad = Ad.objects.get(id=pk)
    if ad.owner_id == request.user.id:
        form = EditAd(instance=ad)
        if request.method == 'POST':
            form = EditAd(request.POST, request.FILES, instance=ad)
            if form.is_valid():
                form.save()
                return redirect(f'/ad/{pk}')
        context = {'form':form}
        return render(request, 'edit_ad.html', context)
    else:
        return render(request, f'/profile/{request.user.id}')