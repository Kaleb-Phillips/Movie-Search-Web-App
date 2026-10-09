# File: main.py
# Description: Python script to interface with The Movie Database (TMDB) API.
#
# Authors: Makala Roberson, Kip Roberts-Lemus, and Kaleb Phillips
# Date: August 7 2024
# Class: UTSA CS-4843-01T Cloud Computing
from flask import Flask, render_template, request, redirect, url_for
import requests
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/movie', methods=['POST'])
def movie():
    movie_title = request.form['movie_id']
    access_token = os.getenv('TMDB_ACCESS_TOKEN')

    if not access_token:
        return render_template('movie.html', description='API Access Token not found')

    url = f'https://api.themoviedb.org/3/search/movie'
    
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {access_token}"
    }
    params = {
        "query": movie_title
    }

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        if data['results']:
            movie_info = data['results'][0]  # Get the first result
            description = movie_info.get('overview', 'No description available')
            title = movie_info.get('title', 'No title available')
            release_date = movie_info.get('release_date', 'No release_date available')
            image = movie_info.get('backdrop_path')
            return render_template('movie.html', title=title, release_date="Release Date: " + release_date, description=description, image=image )
        else:
            return render_template('movie.html', description='Movie not found')
    else:
        return render_template('movie.html', description='API request failed')



@app.route('/discover', methods=['POST'])
def discover():
    access_token = os.getenv('TMDB_ACCESS_TOKEN')

    if not access_token:
        return render_template('movie.html', description='API Access Token not found')

    url = "https://api.themoviedb.org/3/movie/upcoming?language=en-US&region=US&page=1"

    headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {access_token}"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        if data['results']:

            movie_info0 = data['results'][0]  # Get the first result
            description0 = movie_info0.get('overview', 'No description available')
            title0 = movie_info0.get('title', 'No title available')
            release_date0 = movie_info0.get('release_date', 'No release_date available')
            image0 = movie_info0.get('backdrop_path')

            movie_info1 = data['results'][1]  # Get the first result
            description1 = movie_info1.get('overview', 'No description available')
            title1 = movie_info1.get('title', 'No title available')
            release_date1 = movie_info1.get('release_date', 'No release_date available')
            image1 = movie_info1.get('backdrop_path')

            movie_info2 = data['results'][2]  # Get the first result
            description2 = movie_info2.get('overview', 'No description available')
            title2 = movie_info2.get('title', 'No title available')
            release_date2 = movie_info2.get('release_date', 'No release_date available')
            image2 = movie_info2.get('backdrop_path')

            movie_info3 = data['results'][3]  # Get the first result
            description3 = movie_info3.get('overview', 'No description available')
            title3 = movie_info3.get('title', 'No title available')
            release_date3 = movie_info3.get('release_date', 'No release_date available')
            image3 = movie_info3.get('backdrop_path')

            movie_info4 = data['results'][4]  # Get the first result
            description4 = movie_info4.get('overview', 'No description available')
            title4 = movie_info4.get('title', 'No title available')
            release_date4 = movie_info4.get('release_date', 'No release_date available')
            image4 = movie_info4.get('backdrop_path')

            movie_info5 = data['results'][5]  # Get the first result
            description5 = movie_info5.get('overview', 'No description available')
            title5 = movie_info5.get('title', 'No title available')
            release_date5 = movie_info5.get('release_date', 'No release_date available')
            image5 = movie_info5.get('backdrop_path')

            movie_info6 = data['results'][6]  # Get the first result
            description6 = movie_info6.get('overview', 'No description available')
            title6 = movie_info6.get('title', 'No title available')
            release_date6 = movie_info6.get('release_date', 'No release_date available')
            image6 = movie_info6.get('backdrop_path')

            movie_info7 = data['results'][7]  # Get the first result
            description7 = movie_info7.get('overview', 'No description available')
            title7 = movie_info7.get('title', 'No title available')
            release_date7 = movie_info7.get('release_date', 'No release_date available')
            image7 = movie_info7.get('backdrop_path')

            movie_info8 = data['results'][8]  # Get the first result
            description8 = movie_info8.get('overview', 'No description available')
            title8 = movie_info8.get('title', 'No title available')
            release_date8 = movie_info8.get('release_date', 'No release_date available')
            image8 = movie_info8.get('backdrop_path')

            movie_info9 = data['results'][9]  # Get the first result
            description9 = movie_info9.get('overview', 'No description available')
            title9 = movie_info9.get('title', 'No title available')
            release_date9 = movie_info9.get('release_date', 'No release_date available')
            image9 = movie_info9.get('backdrop_path')
            

            return render_template('discover.html', title0=title0, release_date0="Release Date: " + release_date0, description0=description0, image0=image0,
                                    title1=title1, release_date1="Release Date: " + release_date1, description1=description1, image1=image1,
                                    title2=title2, release_date2="Release Date: " + release_date2, description2=description2, image2=image2,
                                    title3=title3, release_date3="Release Date: " + release_date3, description3=description3, image3=image3,
                                    title4=title4, release_date4="Release Date: " + release_date4, description4=description4, image4=image4,
                                    title5=title5, release_date5="Release Date: " + release_date5, description5=description5, image5=image5,
                                    title6=title6, release_date6="Release Date: " + release_date6, description6=description6, image6=image6,
                                    title7=title7, release_date7="Release Date: " + release_date7, description7=description7, image7=image7,
                                    title8=title8, release_date8="Release Date: " + release_date8, description8=description8, image8=image8,
                                    title9=title9, release_date9="Release Date: " + release_date9, description9=description9, image9=image9)
        else:
            return render_template('discover.html', description='Movie not found')
    else:
        return render_template('discover.html', description='API request failed')

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8080, debug=True)

