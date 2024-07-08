# Example of products/views.py
from django.shortcuts import render
from django.http import HttpResponse

def product_list(request):
    return HttpResponse("This is a list of products.")
