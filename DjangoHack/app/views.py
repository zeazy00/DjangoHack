from rest_framework import viewsets
#from rest_framework import views, generics, response, permissions, authentication
from .models import review_source, review
from rest_framework.decorators import action
from .serializers import ReviewSerializer, Review_SourceSerializer
        
#from .serializers import DbUserSerializer, LoginSerializer
from rest_framework.response import Response
#from django.contrib.auth import login, logout
#from django.conf import settings
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
#from rest_framework.permissions import IsAuthenticated
import requests as req

import _datetime

import pymssql 
 
class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    queryset = review.objects.all()

class Review_SourceViewSet(viewsets.ModelViewSet):
    serializer_class = Review_SourceSerializer
    queryset = review_source.objects.all()

#from rest_framework.response import Response
#from rest_framework.decorators import api_view
#from rest_framework import status

#from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
#from .models import review_source, review
#from .serializers import ReviewSerializer, Review_SourceSerializer

#@api_view(['GET', 'POST'])
#def reviews_list(request):
#    """
# List  customers, or create a new customer.
# """
#    if request.method == 'GET':
#        data = []
#        nextPage = 1
#        previousPage = 1
#        customers = Customer.objects.all()
#        page = request.GET.get('page', 1)
#        paginator = Paginator(customers, 10)
#        try:
#            data = paginator.page(page)
#        except PageNotAnInteger:
#            data = paginator.page(1)
#        except EmptyPage:
#            data = paginator.page(paginator.num_pages)

#        serializer = CustomerSerializer(data,context={'request': request} ,many=True)
#        if data.has_next():
#            nextPage = data.next_page_number()
#        if data.has_previous():
#            previousPage = data.previous_page_number()

#        return Response({'data': serializer.data , 'count': paginator.count, 'numpages' : paginator.num_pages, 'nextlink': '/api/customers/?page=' + str(nextPage), 'prevlink': '/api/customers/?page=' + str(previousPage)})

#    elif request.method == 'POST':
#        serializer = CustomerSerializer(data=request.data)
#        if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data, status=status.HTTP_201_CREATED)
#        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)