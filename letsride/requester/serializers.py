from rest_framework import serializers
from  .models import Requester, Matching

class RequesterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Requester
        fields = "__all__"

class MatchingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matching
        fields = "__all__"
