
from django.views.generic.base import TemplateView

from .models import Airport
from .serializers import AirportSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .tasks import task_bulk_create_update
from django.http import HttpResponse

#from django.http import JsonResponse
#from django.shortcuts import render
#from django.views import View
#from django.http import HttpResponseRedirect


@api_view(['GET','POST'])

def Airport_list(request):
    if request.method=='GET':
      if request.data:
        print(request.data)
        airports=Airport.objects.filter(ident=request.data['ident'])
        serializer= AirportSerializer(airports,many=True) #many=True -> serialize all records 
        #return JsonResponse({"airports":serializer.data}) #,safe=False
        if airports:
          return Response({"airports":serializer.data},status=status.HTTP_200_OK)
        else:
          return Response('{"Error":"Data not found"}',status=status.HTTP_404_NOT_FOUND)
      else:
        airports=Airport.objects.all()
        serializer= AirportSerializer(airports,many=True) #many=True -> serialize all records 
        #return JsonResponse({"airports":serializer.data}) #,safe=False
        return Response({"airports":serializer.data},status=status.HTTP_200_OK)
    
    if request.method=='POST':
        serializer=AirportSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response('{"Error":"Bad request"}',status=status.HTTP_400_BAD_REQUEST)

# Create your views here.
class IndexPage(TemplateView):
  template_name='index.html'

  def get_context_data(self, **kwargs):
    context= super().get_context_data(**kwargs)
    context['message']='This works!'
    return context

class UploadCSVpage(TemplateView):
  template_name='upload_csv.html'

  def get_context_data(self, **kwargs):
    context= super().get_context_data(**kwargs)
    return context



def TruncateModel(request):
    Airport.objects.all().delete()
    return HttpResponse('Airport model is empty!')

#Upload from url
def UploadCSVlink(request):
    task_bulk_create_update.delay(type='url')
    return HttpResponse("Celery task has been started. Watch celery's logs for more details.")


#Upload from file
def store_file(csvfile):
    with open("uploads/airports.csv", 'wb+') as dest:
        for chunk in csvfile.chunks():
            dest.write(chunk)

def UploadCSVpc(request):
        store_file(request.FILES['csv_file'])
        task_bulk_create_update.delay(type='file')
        return HttpResponse("Celery task has been started. Watch celery's logs for more details.")