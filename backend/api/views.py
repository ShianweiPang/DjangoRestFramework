import json
from django.forms.models import model_to_dict
from django.http import JsonResponse

from rest_framework.response import Response

from products.models import Product

def api_home(request, *args, **kwargs):
    # request is the HTTPRequest from Django
    # request.body
    # body = request.body # byte string of JSON data
    model_data = Product.objects.all().order_by("?").first()
    data ={}
    if model_data:
        data = model_to_dict(model_data, fields=['id','brand','price'])
    return JsonResponse(data)