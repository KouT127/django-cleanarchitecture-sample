
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.urls import reverse
from django.views import View
from .forms import LoginForm

class LoginView(View):
    def get(self, request, *args, **kwargs):
        # if request.user.is_authenticated:
        #     return redirect(reverse('gas_mileages:index'))

        context = {
            'form': LoginForm(),
        }
        return render(request, 'users/login.html', context)

    def post(self, request, *args, **kwargs):
        print(request.POST)
        form = LoginForm(request.POST)
        if not form.is_valid():
            return render(request, 'users/login.html', {'form': form})
        user = form.get_user()
        login(request, user)
        # user.user_logged_in()
        messages.info(request, "ログインしました。")
        return redirect(reverse('gas_mileages:index'))
