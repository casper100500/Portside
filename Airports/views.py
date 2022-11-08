from django.shortcuts import render
from django.views.generic.base import TemplateView

from django.http import JsonResponse
from .models import Airport
from .serializers import AirportSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET','POST'])

def Airport_list(request):
    if request.method=='GET':
      if request.data:
        print(request.data)
        airports=Airport.objects.filter(ident=request.data['ident'])
        serializer= AirportSerializer(airports,many=True) #many=True -> serialize all records 
        return JsonResponse({"airports":serializer.data}) #,safe=False
      else:
        airports=Airport.objects.all()
        serializer= AirportSerializer(airports,many=True) #many=True -> serialize all records 
        return JsonResponse({"airports":serializer.data}) #,safe=False
    
    if request.method=='POST':
        serializer=AirportSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)

# Create your views here.
class IndexPage(TemplateView):
  template_name='index.html'

  def get_context_data(self, **kwargs):
    context= super().get_context_data(**kwargs)
    context['message']='This works!'
    return context