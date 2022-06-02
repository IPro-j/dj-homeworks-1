from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from advertisements.serializers import AdvertisementSerializer
from advertisements.models import Advertisement
from advertisements.filters import AdvertisementFilter
from advertisements.permissions import IsOwner


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    filter_backends = [DjangoFilterBackend, ]
    filter_class = AdvertisementFilter

    # TODO: настройте ViewSet, укажите атрибуты для кверисета,
    #   сериализаторов и фильтров

    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ["delete", "update", "partial_update"]:
            return [IsAuthenticated(), IsOwner()]
        elif self.action in ["create"]:
            return [IsAuthenticated()]
        return []
