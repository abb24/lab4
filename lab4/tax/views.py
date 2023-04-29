from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
tax = 15

def index(request):
 return render(request, 'tax/index.html')


def anyNumber(request, num):
  total = num + num*tax/100

  return render(request, 'tax/taxcalc.html', context={"total":total, "initial":num, "tax":tax})

def taxrate(request):
    return render(request, 'tax/taxrate.html', context={"tax_rate":0.15})