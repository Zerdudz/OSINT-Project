from flask import Flask, render_template, request
import requests
from time import sleep
import scrappers.Scrapper_Strava, scrappers.Scrapper_Paruvendu,scrappers.Scrapper_Finishers
from geopy.geocoders import Nominatim
import googlemaps

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/search_strava', methods=['POST'])
def search_strava():
    query = request.form['query']
    api_lbc = scrappers.Scrapper_Strava.Scrapper_Strava()
    data = api_lbc.get_athletes(query)

    # Convertir les lieux en coordonnées géographiques.
    new_data = []
    # geolocator = Nominatim(user_agent="myGeocoder")

    gmaps = googlemaps.Client(key='AIzaSyDeJ6BWvDqbxY757fY0nNQH9ESE4HCuKgE')


    for item in data['items']:
        address = item['location']
        # location = geolocator.geocode(address)
        geocode_result = gmaps.geocode(address)

        lat = geocode_result[0]['geometry']['location']['lat']
        lng = geocode_result[0]['geometry']['location']['lng']

        if lat and lng:
            item['coordinates'] = {'lat': float(lat), 'lng': float(lng)}
            new_data.append(item)  # Ajoutez l'élément à la nouvelle liste seulement s'il a des coordonnées
        else:
            print(f"No geocoding results for address: {address}")

    data['items'] = new_data


    return data


@app.route('/search_paruvendu', methods=['POST'])
def search_paruvendu():
    query = request.form['query']
    api_paru = scrappers.Scrapper_Paruvendu.Scrapper_Paruvendu()
    data = api_paru.get_annonces(query)

    # Convertir les lieux en coordonnées géographiques.
    new_data = []
    # geolocator = Nominatim(user_agent="myGeocoder")

    gmaps = googlemaps.Client(key='AIzaSyDeJ6BWvDqbxY757fY0nNQH9ESE4HCuKgE')


    for item in data['items']:
        address = item['location']
        # location = geolocator.geocode(address)
        geocode_result = gmaps.geocode(address)

        lat = geocode_result[0]['geometry']['location']['lat']
        lng = geocode_result[0]['geometry']['location']['lng']

        if lat and lng:
            item['coordinates'] = {'lat': float(lat), 'lng': float(lng)}
            new_data.append(item)  # Ajoutez l'élément à la nouvelle liste seulement s'il a des coordonnées
        else:
            print(f"No geocoding results for address: {address}")

    data['items'] = new_data


    return data


@app.route('/search_finishers', methods=['POST'])
def search_finishers():
    query = request.form['query']
    api_finishers = scrappers.Scrapper_Finishers.Scrapper_Finishers()
    data = api_finishers.get_courses(query)

    # Convertir les lieux en coordonnées géographiques.
    new_data = []
    # geolocator = Nominatim(user_agent="myGeocoder")

    gmaps = googlemaps.Client(key='AIzaSyDeJ6BWvXXXXXXXXXnNQH9ESE4HCuKgE')


    for item in data['items']:
        address = item['location']
        # location = geolocator.geocode(address)
        geocode_result = gmaps.geocode(address)

        try:
            lat = geocode_result[0]['geometry']['location']['lat']
            lng = geocode_result[0]['geometry']['location']['lng']
        except:
            pass

        if lat and lng:
            item['coordinates'] = {'lat': float(lat), 'lng': float(lng)}
            new_data.append(item)  # Ajoutez l'élément à la nouvelle liste seulement s'il a des coordonnées
        else:
            print(f"No geocoding results for address: {address}")

    data['items'] = new_data


    return data


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0")
