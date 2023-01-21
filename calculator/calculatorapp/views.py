from django.shortcuts import render

def calculator(request):
    return render(request,"calculatorapp/calculator.html")

# Create your views here.
