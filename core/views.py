from django.shortcuts import render

# Create your views here.
def driver_callback(request):
    if request.user.is_superuser:
        return "Super User"
    else:
        return "Staff User"
