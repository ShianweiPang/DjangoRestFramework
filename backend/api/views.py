from django.forms.models import model_to_dict
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.serializers import ProductSerializer
from products.models import Product

# Serializer can validate data

# DRF API view
# For API views of rest framework does not need CSRF token (when POST request)
# However, in Django we need that CSRF token for security purpose (when POST request)
@api_view(['GET','POST'])
def api_home(request, *args, **kwargs):
    # request is the HTTPRequest from Django
    # print(request.params)
    # body = request.body # byte string of JSON data
    if request.method =='GET':
        instance = Product.objects.all().order_by("?").first()
        data ={}
        if instance:
            data = ProductSerializer(instance).data
            # data = model_to_dict(model_data, fields=['id','brand','price'])
        return Response(data)
    elif request.method=='POST':
        print(request.data)
        data = request.data

        return Response(data)