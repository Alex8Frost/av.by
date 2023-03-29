from rest_framework import mixins, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.viewsets import GenericViewSet
from back import models, pagination, serializers
from django.shortcuts import get_object_or_404
from django_filters import rest_framework as filters
import back.filters as back_filter


class ViewTransportMark(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    GenericViewSet
):
    serializer_class = serializers.TransportMarkSerializer
    pagination_class = pagination.TransportAdPagination()

    def get_permissions(self):
        permission_classes = []
        if self.action == 'list' or self.action == 'retrieve':
            permission_classes = [IsAuthenticated]
        if self.action == 'delete' or self.action == 'create' or self.action == 'update':
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def get_queryset(self):
        return models.TransportMark.objects.all()

    def list(self, *args, **kwargs):
        serializer = self.serializer_class(self.get_queryset(), many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        if models.TransportMark.objects.filter(name=request.data['name']).exists():
            return Response('The mark is exist!', status=status.HTTP_204_NO_CONTENT)
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        instance = get_object_or_404(models.TransportMark, pk=self.kwargs.get('pk'))
        serializer = self.serializer_class(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        instance = get_object_or_404(models.TransportMark, pk=self.kwargs.get('pk'))
        serializer = self.serializer_class(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, *args, **kwargs):
        instance = get_object_or_404(models.TransportMark, pk=self.kwargs['pk'])
        instance.delete()
        return Response('The instance was deleted successfully!', status=status.HTTP_204_NO_CONTENT)


class ViewTransportModel(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.CreateModelMixin,
    GenericViewSet
):
    serializer_class = serializers.TransportModelSerializer

    def get_permissions(self):
        permission_classes = []
        if self.action == 'list' or self.action == 'retrieve':
            permission_classes = []
        if self.action == 'delete' or self.action == 'create' or self.action == 'update':
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]

    def get_queryset(self):
        return models.TransportModel.objects.filter(mark=self.kwargs['mark_pk'])

    def list(self, request, *args, **kwargs):
        serializer = self.serializer_class(self.get_queryset(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        serializer = self.serializer_class(get_object_or_404(self.get_queryset(), pk=self.kwargs.get('pk')))
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        instance = self.get_queryset().get(pk=self.kwargs.get('pk'))
        serializer = self.serializer_class(instance=instance, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def create(self, request, *args, **kwargs):
        serializer = serializers.TransportModelCreateSerializer(
            data=request.data, context={'mark': self.kwargs.get('mark_pk')})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, *args, **kwargs):
        instance = get_object_or_404(models.TransportModel, pk=self.kwargs.get('pk'))
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ViewTransportAd(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    GenericViewSet
):
    serializer_class = serializers.TransportAdSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = back_filter.TransportAdFilter

    def get_permissions(self):
        permission_classes = []
        if self.action == 'list' or self.action == 'retrieve':
            permission_classes = []
        if self.action == 'delete' or self.action == 'create' or self.action == 'update':
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def get_queryset(self):
        return models.TransportAd.objects.filter(status='open')

    def list(self, request, *args, **kwargs):
        serializer = self.serializer_class(self.filter_queryset(self.get_queryset()), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        instance = get_object_or_404(models.TransportAd, pk=self.kwargs.get('pk'))
        serializer = self.serializer_class(instance, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response()

    def retrieve(self, request, *args, **kwargs):
        instance = get_object_or_404(models.TransportAd, pk=self.kwargs.get('pk'))
        serializer = self.serializer_class(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        instance = get_object_or_404(models.TransportAd, pk=self.kwargs.get('pk'))
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)













