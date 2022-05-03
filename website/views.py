from django.http import HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from django.shortcuts import render
from website.forms import NewsletterForm,ContactForm
from django.contrib import messages

def home_view(request):
    return render(request,'website/index.html')

def about_view(request):
    return render(request,'website/about.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid(): 
            # changing name to unknown  in three lines below 
            post = form.save(commit=False)
            post.name ='unknown'
            form.save()
            messages.add_message(request,messages.SUCCESS,'Your ticket submited successfully.')
        else:
            messages.add_message(request,messages.ERROR,"Your ticket didn't submited .")
    form = ContactForm()
    return render(request,'website/contact.html',{'form':form})

def elements_view(request):
    return  render(request,'website/elements.html')

def test_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('done')
        else:
            return HttpResponse('not valid inputs')
    form = ContactForm()
    return render(request,'website/test.html',{'form':form})


def newsletter_view(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            # return HttpResponseRedirect('/')
            messages.add_message(request,messages.SUCCESS,'You are added to Newsletter successfully.')
        else:
            messages.add_message(request,messages.ERROR,"unfortunately, You are not added to Newsletter successfully.")
            # return HttpResponseRedirect('/')
    form = NewsletterForm()
    return render(request,'website/index.html',{'form':form})