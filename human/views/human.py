from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from human.models import Human
from human.serializers import HumanSerializer


class HumanViewSet(GenericViewSet,
                   mixins.ListModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.CreateModelMixin,
                   mixins.DestroyModelMixin):
    serializer_class = HumanSerializer
    queryset = Human.objects.all()

