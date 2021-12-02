"""millm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
from photologue.views import GalleryListView, PhotoListView
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('l/', GalleryListView.as_view(paginate_by=5), name='photologue_custom-gallery-list'),
    path('p/', PhotoListView.as_view(paginate_by=5), name='photologue_custom-gallery-list'),
    path('<int:photo_id>/vote/', views.vote, name='vote'),
    path('admin/', admin.site.urls),
    path('photologue/', include('photologue.urls')),
    path('h/', TemplateView.as_view(template_name="homepage.html"), name='homepage'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
