from django.http import HttpResponse, JsonResponse, Http404
from django.template import loader
from landing.forms import OrderForm
from django.conf import settings
from landing.models import ImageGallery
import os


def index(request):
    template = loader.get_template('index.html')
    images = ImageGallery.objects.all()
    context = {
        'images': images
    }
    return HttpResponse(template.render(context, request))


def test_template(request):
    template = loader.get_template('template.html')
    images = ImageGallery.objects.all()
    context = {
        'images': images
    }
    return HttpResponse(template.render(context, request))



def submit_form(request):
    if request.method == 'POST' and request.is_ajax():
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({"success": True}, status=200)
        else:
            context = {'success': False, 'error': form.errors}
            return JsonResponse(context, status=400)
    else:
        raise Http404
