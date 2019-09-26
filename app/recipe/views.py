from rest_framework import viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import Tag
from recipe import serializers


class TagViewset(viewsets.GenericViewSet, mixins.ListModelMixin):
    """Manage Tags in Database"""
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Tag.objects.all()
    serializer_class = serializers.TagSerializer

    def get_queryset(self):
        """Returns objects for only currently authenticated user"""
        return self.queryset.filter(user=self.request.user).order_by('-name')