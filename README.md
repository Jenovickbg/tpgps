# Algomap Django Demo

This is a minimal Django project demonstration for Algomap.
It includes a single app `mapapp` that serves a page with a Google Map
centered on Rond-Point Victoire and an example marker.

**Important:** You provided a Google Maps API key to be placed in `.env`.
Consider rotating/regenerating the API key after testing, and don't publish it publicly.

## Quick start

1. Create a Python virtual environment:
   python -m venv venv
   source venv/bin/activate  # on Linux/macOS
   venv\Scripts\activate   # on Windows

2. Install requirements:
   pip install -r requirements.txt

3. Run migrations and start the server:
   python manage.py migrate
   python manage.py runserver

4. Open http://127.0.0.1:8000/ to see the map.

