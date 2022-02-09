from django.shortcuts import render, redirect

from django.views.generic.detail import DetailView

from photologue.models import Photo, Gallery
from photologue_custom.models import GalleryExtended

from millm.forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse

from django.urls import reverse

def index(request):
    photo_list = Photo.objects.on_site().is_public().order_by('-date_added') #[:5]
    gallery_list = Gallery.objects.on_site().is_public().order_by('-date_added') #[:5]
    galleri_list = Gallery.objects.filter(extended__isnull=False).order_by('-date_added') #[:5]
  
    context = {
        'photo_list': [(p, [g.slug for g in p.galleries.iterator()]) for p in photo_list],
        'gallery_list': gallery_list,
        'galleri_list': galleri_list,
        'form': ContactForm(),
    }

    #breakpoint()
    return render(request, 'millm/index.html',  context)

class PhDeView(DetailView):
    queryset = Photo.objects.on_site().is_public()
    template_name = 'millm/photo_detail.html'
    #breakpoint()

class GaliDeView(DetailView):
    queryset = Gallery.objects.filter(extended__isnull=False)
    template_name = 'millm/galleri_detail.html'
    #breakpoint()

def contact_email(request):
    #breakpoint()
    form = ContactForm(request.POST)
    if form.is_valid():
        body = {
            'name': form.cleaned_data['name'], 
            'subject': form.cleaned_data['subject'], 
            'email': form.cleaned_data['email'], 
            'message':form.cleaned_data['message'], 
        }
        subject = body['subject']
        message = "\n".join(body.values())

        send_mail(subject, message, 'drizla@inbox.ru', ['drizla@inbox.ru'], fail_silently=False) 

    #breakpoint()
    return redirect("index")

def portdet(request):
    context = {
    }
    #breakpoint()
    return render(request, 'millm/portfolio-details.html',  context)
