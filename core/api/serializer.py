from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from core.models import TuristicPoint
from atractions.api.serializers import AttractionsSerializer
from comments.api.serializers import CommentSerializer
from reviews.api.serializers import ReviewSerializer
from address.api.serializers import AddressSerializer


class TuristicPointSerializer(ModelSerializer):
    atractions = AttractionsSerializer(many=True)
    comments = CommentSerializer(many=True)
    reviews = ReviewSerializer(many=True)
    address = AddressSerializer
    complete_description = SerializerMethodField()

    class Meta:
        model = TuristicPoint
        fields = ['id',
                  'name',
                  'description',
                  'approved',
                  'picture',
                  'atractions',
                  'comments',
                  'reviews',
                  'address',
                  'complete_description',
                  'complete_description2'
                  ]

    def get_complete_description(self, obj):
        return '%s - %s' % (obj.name, obj.description)
