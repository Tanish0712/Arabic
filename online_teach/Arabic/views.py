from django.shortcuts import render

def home(request):
    return render(request, "arabic/home.html")



def phase1(request):
    return render(request, 'arabic/Phase_1.html')

def easy(request):
    return render(request, "Phase_1/Easy.html")

def easyquiz(request):
    return render(request, 'Phase_1/Easyquiz.html')

def medium(request):
    return render(request, "Phase_1/Medium.html")

def mediumquiz(request):
    return render(request, 'Phase_1/Mediumquiz.html')

def hard(request):
    return render(request, "Phase_1/Hard.html")

def hardquiz(request):
    return render(request, 'Phase_1/Hardquiz.html')
