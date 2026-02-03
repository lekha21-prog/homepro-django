from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    is_admin = request.user .is_staff
    return render(request, 'home.html',
                  {'is_admin' : is_admin})

