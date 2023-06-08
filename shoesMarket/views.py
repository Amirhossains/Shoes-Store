from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializer import ShoesListSerializer, ShoesDetailSerializer, CommentSerializer
from .models import ShoesModel, CommentModel

class ShoesList(APIView):

    def get(self, request):
        categories = ShoesModel.objects.all()
        serializer = ShoesListSerializer(categories, many=True, context={'request':request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ShoesDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ShoesDetail(APIView):

    def found(self, pk):
        try:
            c = ShoesModel.objects.get(pk=pk)
        except ShoesModel.DoesNotExist:
            raise Http404
        return c

    def get(self, request, pk):
        category = self.found(pk)
        serializer = ShoesDetailSerializer(category, context={'request':request})
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        category = self.found(pk)
        serializer = ShoesDetailSerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        category = self.found(pk)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
