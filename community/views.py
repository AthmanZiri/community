from django.http import JsonResponse
from django.core.serializers.json import DjangoJSONEncoder
from django.forms.models import model_to_dict

from .models import Member


def get_members(request):
    members = Member.objects.all()
    return JsonResponse(model_to_dict(members), DjangoJSONEncoder)
