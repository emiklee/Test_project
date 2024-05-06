from django.http import HttpResponse
from rest_framework import generics
from .models import *
from .serializers import *
from rest_framework.permissions import IsAuthenticated


def homepage(request):
    return HttpResponse('<h1>Hello World</h1>')


class kafeGuestsList(generics.ListCreateAPIView):
    queryset = Guests.objects.all()
    serializer_class = GuestsSerializer
    permission_classes = (IsAuthenticated,)


class kafeGuestsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Guests.objects.all()
    serializer_class = GuestsSerializer
    permission_classes = (IsAuthenticated,)


class kafeTablesList(generics.ListCreateAPIView):
    queryset = Tables.objects.all()
    serializer_class = TablesSerializer
    permission_classes = (IsAuthenticated,)


class kafeTablesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tables.objects.all()
    serializer_class = TablesSerializer
    permission_classes = (IsAuthenticated,)
