from django.urls import path, include
from .views import index

urlpatterns = [
    # path('transporte/', include('transporte.urls')),
    path('', index, name="transporte_index")
]
