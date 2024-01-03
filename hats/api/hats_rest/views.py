from django.shortcuts import render
from common.json import ModelEncoder
from .models import Hat, LocationVO
from django.views.decorators.http import require_http_methods
import json

class LocationVOEncoder(ModelEncoder):
    model = LocationVO
    properties = [
        'closet_name',
        'section_number',
        'shelf_number',
        'import_href',
    ]

class HatEncoder(ModelEncoder):
    model = Hat
    properties = [
        'style_name',
        'fabric',
        'color',
        'picture_url',
        'id',
    ]
    encoders = {
        'location': LocationVOEncoder()
    }
