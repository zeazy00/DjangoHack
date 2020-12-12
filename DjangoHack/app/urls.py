from .views import ReviewViewSet, Review_SourceViewSet
#from .views import    RegisterView, LoginView, LogoutView, UserView
#from .views import RegistrationAPIView, LoginAPIView
from rest_framework.routers import DefaultRouter
from django.urls import path, include
#from django.urls import re_path
from rest_framework_simplejwt.views import TokenVerifyView

app_name = "app"

router = DefaultRouter()
router.register(r'review', ReviewViewSet)
router.register(r'review_source', Review_SourceViewSet)

urlpatterns = [
    path('', include(router.urls)),
]



