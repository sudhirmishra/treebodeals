from django.shortcuts import render

from deals import models
from deals import serializers

from rest_framework import viewsets
from rest_framework import filters

from django.http import JsonResponse

from django.db.models import Max,Min,Avg,Count
from itertools import groupby
from rest_framework_word_filter import FullWordSearchFilter

class DealsViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = models.Deal.objects.all()
    serializer_class = serializers.DealSerializer
    filter_backends = (filters.SearchFilter, )
    #filter_fields  = ('location', 'name',)
    search_fields = ('location', 'name',)
    #word_fields = ('location','name',)

    
# Create your views here.
def index(request):
    return render(request,"deals/index.html")
    
def stat(request):
    
    max_price = models.Deal.objects.all().aggregate(Max('actual_price'))    
    min_price = models.Deal.objects.all().aggregate(Min('actual_price'))
    
    avg_price = models.Deal.objects.all().aggregate(Avg('rating'))
    
    area_wise_count = models.Deal.objects.values_list('location',flat=True)
    
    area_wise_count = [str(x.split(',')[-2])[1:] for x in area_wise_count]
    
    result = list((key, len(list(group))) for key, group in groupby(sorted(area_wise_count)))
    
    
    data = {
        'price' :     {
            "minimum":min_price['actual_price__min'],
            "maximum":max_price['actual_price__max']
            },
        'average_rating' : avg_price['rating__avg'],
        'area-wise-hotel-distribution':result
    }
    
    return JsonResponse(data)
