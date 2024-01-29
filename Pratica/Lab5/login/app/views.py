from django.shortcuts import render, redirect

# Create your views here.
def authorins(request):
    if not request.user.is_authenticated or request.user.username != 'admin':
        return redirect('/login')
    
    # if POST request, process form data
    if request.method == 'POST':
        # create form instance and pass data to it
        pass