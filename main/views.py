from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2306240156',
        'name': 'Valiza Nadya Jatikansha',
        'class': 'PBP B',
        'appName': 'Doughsy'
    }

    return render(request, "main.html", context)