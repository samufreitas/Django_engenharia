from django.shortcuts import render
from rest_framework import viewsets, permissions
from django.contrib.auth.models import User, Group
from agenda.models import Local, Convidado, Agenda
from agenda.serializers import UserSeriaLizer, GroupSerializer, LocalSerializer, ConvidadoSerializer, AgendaSerializer


# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSeriaLizer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class LocalViewSet(viewsets.ModelViewSet):
    queryset = Local.objects.all()
    serializer_class = LocalSerializer
    permission_classes = [permissions.IsAuthenticated]


class ConvidadoViewSet(viewsets.ModelViewSet):
    queryset = Convidado.objects.all()
    serializer_class = ConvidadoSerializer
    permission_classes = [permissions.IsAuthenticated]


class AgendaViewSet(viewsets.ModelViewSet):
    queryset = Agenda.objects.all()
    serializer_class = AgendaSerializer
    permission_classes = [permissions.IsAuthenticated]
