from django.urls import path
from . import views

urlpatterns = [
    path('',views.IndexPage.as_view()),
    
    #API
    path('airports/',views.Airport_list), 

    #Celery
    path('upload_csv/',views.UploadCSVpage.as_view()),
    path("csv_upload_PC",views.UploadCSVpc),
    path("csv_upload_link",views.UploadCSVlink),
    path("tuncate_model",views.TruncateModel)
]