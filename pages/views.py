from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Listing
from realtors.models import Realtor
from listings.choices import bedroom_choice,price_choice,state_choice


# Create your viewas here.
def index(request):
    listings=Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    context={
        'listings':listings,
        'state_choice':state_choice,
        'price_choice':price_choice,
        'bedroom_choice':bedroom_choice
    }
    return render(request, 'pages_/index.html',context)

def about(request):
    realtors=Realtor.objects.order_by('-hire_date')

    mvp_realtors=Realtor.objects.all().filter(is_mvp=True)

    context={
        'realtors':realtors,
        'mvp_realtors':mvp_realtors
    }
    return render(request, 'pages_/about.html',context)
