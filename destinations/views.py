from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.exceptions import NotFound, ValidationError
from .models import Destination
from .serializers import DestinationSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class DestinationAPIView(ModelViewSet):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer
    authentication_classes = []
    permission_classes = []

    def get_authenticators(self):
        if self.request.method != 'GET':
            return [TokenAuthentication()]
        return []

    def get_permissions(self):
        if self.request.method != 'GET':
            return [IsAuthenticated()]
        return []

    def list(self, request, *args, **kwargs):
        try:
            queryset = self.filter_queryset(self.get_queryset())
            if not queryset.exists():
                return Response({"message": "No destinations found", "status": status.HTTP_204_NO_CONTENT})

            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({"message": "An error occurred while fetching destinations.", "detail": str(e)},
                            status=status.HTTP_400_BAD_REQUEST)

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED,)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"message": "An error occurred while creating destinations.", "detail": str(e)},
                            status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
        except Exception:
            return Response({"detail": "Sorry!, Destination not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)

        try:
            instance = self.get_object()
        except NotFound:
            return Response({"detail": "Failed to update: Destination not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(instance, data=request.data, partial=partial)

        try:
            serializer.is_valid(raise_exception=True)
        except ValidationError as e:
            return Response({"detail": "Validation Error", "errors": e.detail},
                            status=status.HTTP_400_BAD_REQUEST)

        self.perform_update(serializer)
        return Response({"Message": "Data for this destination has been updated successfully.",
                         "Detail": serializer.data})

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
        except NotFound:
            return Response({"Message": "Unable to delete: Destination could not be found."},
                            status=status.HTTP_404_NOT_FOUND)

        self.perform_destroy(instance)
        return Response({"Message": "Data for this destination has been deleted successfully."},
                        status=status.HTTP_204_NO_CONTENT)
