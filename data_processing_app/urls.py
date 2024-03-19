from django.urls import path
from data_processing_app.api.views import process_data_view

urlpatterns = [
    path('process-data/', process_data_view, name='process_data'),
]
