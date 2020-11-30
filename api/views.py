from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from.models import Subscriber
from.serializers import SubscriberSerializer
# Create your views here.

@api_view(['GET'])
def api_overview(request):
    api_urls = {
        'subscribers': {
            'all subscribers': 'subscriber/list/',
            'create': 'subscriber/create/',
            'delete': 'subscriber/<email>/delete/'
        }
    }
    return Response(api_urls)

@api_view(['GET'])
def subscriber_list(request):
    subscribers = Subscriber.objects.all()
    serializer = SubscriberSerializer(subscribers, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_subscriber(request):
    serializer = SubscriberSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def delete_subscriber(request, email):
    subscriber = Subscriber.objects.get(email=email)
    subscriber.delete()
    return Response('Item successfully deleted')