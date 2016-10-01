from rest_framework import serializers
from deals import models

class DealSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Deal
        fields = ('id', 'name', 'image', 'rating', 'link', 'actual_price','discount','location')
        
        

