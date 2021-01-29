from django.http import HttpResponse, JsonResponse, Http404
from django.template import loader
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt
from landing.forms import OrderForm


def index(request):
    template = loader.get_template('index.html')
    context = {}
    return HttpResponse(template.render(context, request))


@csrf_exempt
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
