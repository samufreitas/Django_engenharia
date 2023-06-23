from django.contrib.auth.models import User, Group
from rest_framework import serializers
from agenda.models import Local, Convidado, Agenda


class UserSeriaLizer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class LocalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Local
        fields = ['nome', 'rua', 'numero']


class ConvidadoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Convidado
        fields = ['nome', 'email']


class AgendaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Agenda
        fields = ['compromisso', 'data_inicio', 'data_fim', 'local', 'convidados']
