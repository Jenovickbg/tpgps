from django.shortcuts import render
from django.conf import settings
import os

def home(request):
    # Coordinates for Rond-Point Victoire (example)
    context = {
        'google_maps_api_key': os.getenv('GOOGLE_MAPS_API_KEY', ''),
        'center_lat': -4.4419,
        'center_lng': 15.2663,
        'stops': [
            {'name': 'Rond-Point Victoire', 'lat': -4.4419, 'lng': 15.2663, 'photo': ''},
            {'name': 'Gare Centrale', 'lat': -4.3276, 'lng': 15.2663, 'photo': ''},
        ],
    }
    return render(request, 'map.html', context)
