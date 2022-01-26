from django.shortcuts import render

from django.views.generic.detail import DetailView

from photologue.models import Photo, Gallery
from photologue_custom.models import GalleryExtended

def index(request):
    photo_list = Photo.objects.on_site().is_public().order_by('-date_added') #[:5]
    gallery_list = Gallery.objects.on_site().is_public().order_by('-date_added') #[:5]
    galleri_list = Gallery.objects.filter(extended__isnull=False).order_by('-date_added') #[:5]
  
    context = {
        'photo_list': [(p, [g.slug for g in p.galleries.iterator()]) for p in photo_list],
        'gallery_list': gallery_list,
        'galleri_list': galleri_list,
    }
    #breakpoint()
    return render(request, 'millm/index.html',  context)

class PhDeView(DetailView):
    queryset = Photo.objects.on_site().is_public()
    template_name = 'millm/photo_detail.html'
    #breakpoint()

class GaliDeView(DetailView):
    queryset = Gallery.objects.on_site().is_public()
    template_name = 'millm/galleri_detail.html'
    #breakpoint()

def indexx(request):
    photo_list = Photo.objects.order_by('-date_added') #[:5]
    context = {
        'photo_list': [p for p in  photo_list],
    }
    #breakpoint()
    return render(request, 'millm/indexx.html',  context)
def portdet(request):
    context = {
    }
    #breakpoint()
    return render(request, 'millm/portfolio-details.html',  context)
