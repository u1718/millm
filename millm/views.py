from django.shortcuts import render

from photologue.models import Photo

def vote(request, photo_id):
    return HttpResponse(".%s." % photo_id)
def index(request):
    photo_list = Photo.objects.order_by('-date_added')[:5]
    context = {
        'photo_list': [(p.id, p.image_filename()) for p in  photo_list],
    }
    #breakpoint()
    return render(request, 'millm/index.html',  context)
