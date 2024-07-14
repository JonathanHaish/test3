from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login


def home(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not null:
                login(request, user)
                return redirect('dashboard')  # Redirect to a dashboard page after login
            else:
                return render(request, 'home.html', {'form': form, 'error': 'Invalid credentials'})
    
        
    return render(request, 'home.html', {'form': 'ddd'})
