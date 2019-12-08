from rest_framework import serializers
from .models import (Regjionet, 
                        Reshtat, 
                        Ulset, 
                        Cmimet, 
                        Shitja, 
                        Ndeshjet, 
                        LlojiIndeshjeve
                        )

from rest_framework_bulk import (
    BulkListSerializer,
    BulkSerializerMixin,
)
# Create your views here.

class RegjionetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Regjionet
        fields = ('id', 'emri')


class ReshtatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reshtat
        fields = ('id', 'emri')

class CmimetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cmimet
        fields = ('id', 'regjioni', 'cmimi')


class LlojiIndeshjeveSerializer(serializers.ModelSerializer):
    class Meta:
        model = LlojiIndeshjeve
        fields = ('id', 'titulli',) 


class NdeshjetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ndeshjet
        fields = ("id", 'titulli', 'ndeshja', 'data', 'ora')


class ShitjaInsertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shitja
        fields = ('fatura', 'ndeshja', 'ulsa', 'cmimi')
        # depth = 2


class ShitjaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shitja
        fields = ('fatura', 'ndeshja', 'ulsa', 'cmimi')
        depth = 2
        


class UlsetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ulset
        fields = ('id', 'regjioni', 'reshti', 'ulsa', 'statusi', 'cordinata')


class UlsetRegjionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ulset
        fields = ('id', 'regjioni', 'reshti', 'ulsa', 'cmimi', 'statusi')
        depth = 2

class UlsetUpdateSerializer(BulkSerializerMixin, serializers.ModelSerializer):
    class Meta(object):
        model = Ulset
        fields = ('id', 'regjioni', 'reshti', 'ulsa', 'statusi', 'cordinata')
        # only necessary in DRF3
        list_serializer_class = BulkListSerializer