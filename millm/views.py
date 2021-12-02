from django.http import HttpResponse

from photologue.models import Photo

def vote(request, photo_id):
    return HttpResponse(".%s." % photo_id)
def index(request):
    #breakpoint()
    photo_list = Photo.objects.order_by('-date_added')[:5]
    output = ', '.join([p.image_filename() for p in photo_list])
    return HttpResponse(output)
