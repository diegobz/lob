from django.db.models import Q
from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Address
from .serializers import AddressSerializer


@api_view(['GET', 'POST'])
def addresses_list(request):
    if request.method == 'GET':

        if 'search' in request.query_params:
            keyword = request.query_params['search']
            query = Address.objects.filter(
                Q(line1__contains=keyword) |
                Q(line2__contains=keyword) |
                Q(city__contains=keyword) |
                Q(state__contains=keyword) |
                Q(zipcode__contains=keyword)
            )
        else:
            query = Address.objects.all()
        serializer = AddressSerializer(query, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        address = AddressSerializer(data=request.data)
        if address.is_valid():
            address.save()
            return Response(address.data, status=status.HTTP_201_CREATED)
        return Response(address.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def addresses_detail(request, pk):
    try:
        address = Address.objects.get(pk=pk)
    except Address.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AddressSerializer(address)
        return Response(serializer.data)

    elif request.method in ('PUT', 'PATCH'):
        if request.method == 'PATCH':
            partial = True
        else:
            partial = False

        serializer = AddressSerializer(address, data=request.data, partial=partial)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        address.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
