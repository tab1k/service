from django.shortcuts import render
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet
from services.models import Subscription
from .serializers import *


class SubscriptionView(ReadOnlyModelViewSet):
    queryset = Subscription.objects.all().prefetch_related('client')
    serializer_class = SubscriptionSerializer
    permission_classes = [AllowAny]
