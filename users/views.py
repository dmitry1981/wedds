from users.serializers import RegisterSerializer, ActivateSerializer
from users.models import CustomUser as User
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
import logging


logger = logging.getLogger('api')


class UsersViewSet(
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
):
    queryset = User.objects.all()
    # serializer_class = RegisterSerializer
    # lookup_field = "invoice_id"

    def get_serializer_class(self):
        serializers = {
            'register': RegisterSerializer,
            'activate': ActivateSerializer,
            # 'login': ActivateSerializer,
            # 'logout': ActivateSerializer,
            # 'retrieve': InvoiceSerializer
        }

        if self.action in serializers.keys():
            return serializers[self.action]

    @action(detail=False, methods=['post'], url_name='register')
    def register(self, request, *args, **kwargs):
        logger.info(request.data)

        serializer = self.get_serializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        return Response(status=204)

    # @action(detail=False, methods=['get'], url_name='activate', url_path=r'activate/(?P<chapter_id>[0-9]+)')
    @action(detail=False, methods=['get'], url_name='activate')
    def activate(self, request, *args, **kwargs):
        logger.info(request.data)
        activation_code = request.query_params.get("code")
        data = {
            'activation_code': activation_code
        }

        serializer = self.get_serializer(data=data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(is_active=False, activation_code=activation_code)
            user.is_active = True
            user.save()
        except User.DoesNotExist:
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

        return Response(status=204)
