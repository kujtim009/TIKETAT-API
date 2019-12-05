from django.shortcuts import render
from rest_framework import viewsets, generics, authentication, permissions
from rest_framework.views import APIView 
from django.db.models import Sum, Max
from .permissions import CustomDjangoModelPermissions
from .models import (Regjionet, 
                     Reshtat, 
                     Ulset, 
                     Cmimet, 
                     Shitja, 
                     Ndeshjet, 
                     LlojiIndeshjeve
                    )
from .serializers import (RegjionetSerializer, 
                            ReshtatSerializer, 
                            UlsetSerializer, 
                            UlsetRegjionSerializer, 
                            CmimetSerializer,  
                            UlsetUpdateSerializer, 
                            ShitjaSerializer,
                            ShitjaInsertSerializer,
                            NdeshjetSerializer, 
                            LlojiIndeshjeveSerializer
                            )
from rest_framework.response import Response
from rest_framework_bulk import ListBulkCreateUpdateDestroyAPIView


class RegjionetView(viewsets.ModelViewSet):
    queryset = Regjionet.objects.all()
    serializer_class = RegjionetSerializer
    permission_classes = (CustomDjangoModelPermissions,)
    # # REQUIRES AUTHENTICATION AND PERMISIONS
    # authentication_classes = (authentication.TokenAuthentication,)
    # permission_classes = (permissions.IsAuthenticated, )

class ReshtatView(viewsets.ModelViewSet):
    queryset = Reshtat.objects.all()
    serializer_class = ReshtatSerializer
    permission_classes = (CustomDjangoModelPermissions,)

class UlsetView(viewsets.ModelViewSet):
    queryset = Ulset.objects.all()
    serializer_class = UlsetSerializer
    permission_classes = (CustomDjangoModelPermissions,)


class CmimetView(viewsets.ModelViewSet):
    queryset = Cmimet.objects.all()
    serializer_class = CmimetSerializer
    permission_classes = (CustomDjangoModelPermissions,)



class ShitjaViewCheck(viewsets.ModelViewSet):
    queryset = Shitja.objects.all()
    serializer_class = ShitjaSerializer
    permission_classes = (CustomDjangoModelPermissions,)


class ShitjaView(generics.ListAPIView):
    # queryset = Ulset.objects.all()
    serializer_class = ShitjaSerializer
    permission_classes = (CustomDjangoModelPermissions,)
    
    def get_queryset(self):
        game = self.request.query_params.get('ndeshja', None)

        queryset = Shitja.objects.filter(ndeshja__id=game)
        return queryset


class LlojiIndeshjeveView(viewsets.ModelViewSet):
    queryset = LlojiIndeshjeve.objects.all()
    serializer_class = LlojiIndeshjeveSerializer
    permission_classes = (CustomDjangoModelPermissions,)


class NdeshjetView(viewsets.ModelViewSet):
    queryset = Ndeshjet.objects.all().order_by('-id')
    serializer_class = NdeshjetSerializer
    permission_classes = (CustomDjangoModelPermissions,)



class NdeshjetCurrentView(viewsets.ModelViewSet):
    queryset = Ndeshjet.objects.all()
    serializer_class = NdeshjetSerializer
    permission_classes = (CustomDjangoModelPermissions,)
    

    def list(self, request, *args, **kwargs):
        queryset = Ndeshjet.objects.all().last()
        serializer = NdeshjetSerializer(queryset)
        return Response(serializer.data)

class UpdateUlsetView(APIView):
    # queryset = Ulset.objects.all().last()
    # permission_classes = (CustomDjangoModelPermissions,)
    def get(self, request):
        queryset = Ulset.objects.all().update(statusi=False)
        return Response({"message":"update finished!"})


# class UpdateUlsetView(generics.UpdateAPIView):
#     queryset = Ulset.objects.all()
#     serializer_class = UlsetSerializer

#     def update(self, request, *args, **kwargs):
#         instance = self.get_object()
#         instance.statusi = False
#         instance.save()

#         serializer = self.get_serializer(instance)
#         serializer.is_valid(raise_exception=True)
#         self.perform_update(serializer)
#         return Response(serializer.data)



class UlsetRegjionView(generics.ListAPIView):
    # queryset = Ulset.objects.all()
    serializer_class = UlsetRegjionSerializer
    permission_classes = (CustomDjangoModelPermissions,)
    
    def get_queryset(self):
        region = self.request.query_params.get('regjion', None)
        reshti = self.request.query_params.get('reshti', None)

        if region:
            regjioniId = Regjionet.objects.filter(emri=region)[0].id
        if reshti:
            reshtiId = Reshtat.objects.filter(emri=reshti)[0].id


        if region is not None and reshti is not None:
            queryset = Ulset.objects.filter(regjioni=regjioniId, reshti=reshtiId)
        elif region is not None and reshti is None: 
            queryset = Ulset.objects.filter(regjioni=regjioniId)
        return queryset
    

class ShitjaInsertView(APIView):
    permission_classes = (CustomDjangoModelPermissions,)
    queryset = Shitja.objects.filter(ulsa = 6872)
    def post(self, request):
        # queryset = Ulset.objects.all()
        print(request.data)
        serializer_class = ShitjaInsertSerializer(data = request.data, many=True, partial=True)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data)

        return Response({"ERROR":"JSON NOT VALID"})


class CmimetGroupView(APIView):
    permission_classes = (CustomDjangoModelPermissions,)
    queryset = Cmimet.objects.all()
    def post(self, request):
        queryset = Cmimet.objects.filter(regjioni=request.data['regjioni']).update(cmimi=request.data['cmimi'])
        return Response({"message":"update finished!"})

    def get(self, request):
        queryset = Cmimet.objects.values('regjioni','regjioni__emri').annotate(cmimi=Max('cmimi'))
        return Response(queryset)


class UlsetEzenaView(viewsets.ModelViewSet):
    queryset = Ulset.objects.filter(statusi=True)
    serializer_class = UlsetUpdateSerializer
    permission_classes = (CustomDjangoModelPermissions,)


class UlsetUpdateStatus(ListBulkCreateUpdateDestroyAPIView):
    queryset = Ulset.objects.all()
    serializer_class = UlsetUpdateSerializer
    permission_classes = (CustomDjangoModelPermissions,)