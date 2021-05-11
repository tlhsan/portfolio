from django.shortcuts import render, resolve_url

# Create your views here.
def main(request):
    return render(request, 'home/index.html')