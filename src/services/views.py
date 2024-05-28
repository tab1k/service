from django.db.models import Prefetch
from django.shortcuts import render
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet
from clients.models import Client
from services.models import Subscription
from .serializers import *


class SubscriptionView(ReadOnlyModelViewSet):
    queryset = Subscription.objects.all().prefetch_related(
        'plan',
        Prefetch(
            'client', queryset=Client.objects.all().select_related('user').only('company_name',
                                                         'user__email')
        ))
    serializer_class = SubscriptionSerializer
    permission_classes = [AllowAny]
