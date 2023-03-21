from rest_framework import mixins, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from back.serializers import TransportMarkSerializer
from rest_framework.viewsets import GenericViewSet
from back.models import TransportMark
from django.shortcuts import get_object_or_404


class ViewTransportMark(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    GenericViewSet
):
    serializer_class = TransportMarkSerializer

    def get_permissions(self):
        permission_classes = []
        if self.action == 'list' or self.action == 'retrieve':
            permission_classes = []
        if self.action == 'delete' or self.action == 'update' or self.action == 'create':
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def get_queryset(self):
        return TransportMark.objects.all()

    def list(self, *args, **kwargs):
        self.get_permissions()
        serializer = self.serializer_class(self.get_queryset(), many=True)
        print(self.request.user.is_authenticated)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        self.get_permissions()

        if TransportMark.objects.filter(name=request.data['name']).exists():
            return Response('The mark is exist!', status=status.HTTP_204_NO_CONTENT)
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        self.get_permissions()
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, *args, **kwargs):
        instance = get_object_or_404(TransportMark, pk=self.kwargs['pk'])
        serializer = self.serializer_class(data=instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, *args, **kwargs):
        instance = get_object_or_404(TransportMark, pk=self.kwargs['pk'])
        instance.delete()
        return Response('The instance was deleted successfully!', status=status.HTTP_204_NO_CONTENT)




