from rest_framework import serializers, viewsets
from .models import Member


class MemberSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Member
        fields = ('first_name', 'last_name', 'email',
                  'mobile_number', 'bio', 'photo', 'website')


class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
