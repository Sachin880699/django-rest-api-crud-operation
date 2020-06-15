from django.core import serializers
from .models import Product
from django.http import HttpResponse
from django.shortcuts import render,HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from.models import *
from.serializers import ProductSerializer
from rest_framework import status
from django.core import serializers
from django.http import HttpResponse

@api_view(['get','POST','DELETE'])
def home(request):
    if request.method=='GET':
        obj = Product.objects.all()
        serializer = ProductSerializer(obj,many=True)
        return Response(serializer.data)

    elif request.method=='POST':
        serializer = ProductSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = Product.objects.all().delete()
        return Response({'message': '{} Tutorials were deleted successfully!'.format(count[0])},
                            status=status.HTTP_204_NO_CONTENT)


@api_view(['GET','PUT','DELETE'])
def product_detail(request,pk):
    try:
        obj = Product.objects.get(id=pk)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='GET':


        serializer = ProductSerializer(obj)
        return Response(serializer.data)
    elif request.method=='PUT':
        serializer = ProductSerializer(obj,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        obj = Product.objects.get(id=pk)
        obj.delete()
        return Response( status=status.HTTP_204_NO_CONTENT)



def export(request):
    objects = Product.objects.all()
    with open(r'/home/sachin/Desktop/sachin.json', "w") as out:
        mast_point = serializers.serialize("json", objects)
        out.write(mast_point)

    return HttpResponse('All data has been export in json file')




def url_api(request):
    qs = Product.objects.all()
    qs_json = serializers.serialize('json', qs)
    return HttpResponse(qs_json, content_type='application/json')
