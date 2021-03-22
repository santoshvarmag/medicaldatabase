from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404, ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import *

# Create your views here.
class CompanyViewSet(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def list(self, request):
        company = Company.objects.all()
        serializer = CompanySerializer(company, many=True, context={"request":request})
        response_dict = {"error": False, "message": "All companies data", "data": serializer.data}
        return Response(response_dict)

    def create(self, request):
        try:
            serializer = CompanySerializer(data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response={
                "error":False, 
                "message":"Company data added successfully!"
                }
        except:
            dict_response = {
                "error": True,
                "message": "Couldnt add the data",
            }
        return Response(dict_response)
    
    def update(self, request, pk=None):
        try:
            queryset = Company.objects.all()
            company = get_object_or_404(queryset, pk=pk)
            serializer = CompanySerializer(company, data=request.data, context={"request":request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response = {
                "error": False,
                "message": "Company data updated successfully!",
            }
        except:
            dict_response = {
                "error": True,
                "message": "Couldnt add the data",
            }
        return Response(dict_response)

class CompanyBankViewSet(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def create(self, request):
        try:
            serializer = CompanyBankSerializer(
                data=request.data, 
                context={"request":request}
                )
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response = {
                "error": False,
                "message": "Bank Details created!"
            }
        except:
            dict_response = {
                "error": True,
                "message": "Unable to create Bank details!"
            }
        return Response(dict_response)

    def list(self, request):
        company_bank = CompanyBank.objects.all()
        serializer = CompanyBankSerializer(company_bank, many=True, context={"request":request})
        dict_response = {
            "error": False,
            "message": "All company bank details",
            "data": serializer.data
        }

        return Response(dict_response)

    def retrieve(self, request, pk=None):
        queryset = CompanyBank.objects.all()
        company_bank = get_object_or_404(queryset, pk=pk)
        serializer = CompanyBankSerializer(company_bank, context={"request": request})
        dict_response = {
            "error": False,
            "message": "Single company Bank details!",
            "data": serializer.data
        }

        return Response(dict_response)
    
    def update(self, request, pk=None):
        try:
            queryset = CompanyBank.objects.all()
            company_bank = get_object_or_404(queryset, pk=pk)
            serializer = CompanyBankSerializer(
                company_bank,
                data=request.data,
                context={"request": request} 
                )
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response = {
                "error": False,
                "message": "Details updated successfully!"
            }
        except:
            dict_response = {
                "error": True,
                "message": "Unable to update!"
            }

        return Response(dict_response)

class CompanyNameViewSet(ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = CompanySerializer

    def get_queryset(self):
        name=self.kwargs['name']
        return Company.objects.filter(name=name)

        
    



company_list = CompanyViewSet.as_view({"get":"list"})
company_create = CompanyViewSet.as_view({"post": "create"})
company_update = CompanyViewSet.as_view({"put": "update"})