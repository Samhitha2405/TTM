from django.shortcuts import render, redirect
from django.shortcuts import render
from django.contrib.auth.models import User, auth
from .forms import *
from .models import *
#from djangoproject.TTM.reviews.forms import ReviewForm
#from djangoproject.TTM.reviews.models import TouristReview


# Create your views here.
def review_list(request):
    if request.method=='GET':
        reviews = TouristReview.objects.all()
        return render(request,'reviewpage.html',{'reviews':reviews})

def add_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST,request.FILES)
        if form.is_valid():
            review = form.save(commit=False)
            review.user=request.user
            review.save()
            return redirect('review_list')
    else:
        form = ReviewForm()

    return render(request,'reviewpage.html',{'form':form})
