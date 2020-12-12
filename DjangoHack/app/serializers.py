from rest_framework import serializers
from .models import review_source, review
from django.contrib.auth import authenticate
#from .validators import validate_username

class ReviewSerializer(serializers.ModelSerializer):
	class Meta:
		model = review
		fields = ('id','text','source','url','sence')

class Review_SourceSerializer(serializers.ModelSerializer):
	class Meta:
		model = review_source
		fields = ('id','name','url')
	