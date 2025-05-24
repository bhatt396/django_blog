from django.shortcuts import render

def register(request):

    return render(request,'auth/register.html')

# In crud/views/auth_views.py

