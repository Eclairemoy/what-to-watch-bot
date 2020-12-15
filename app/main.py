import json
import os
import pandas as pd
import requests
from flask import Flask, request, send_file

app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get('FLASK_SECRET_KEY')
MOVIE_DB_API_KEY = os.environ.get('MOVIE_DB_API_KEY')


@app.route('/show-greeting', methods=['POST'])
def show_greeting():
    return


@app.route('/title-description', methods=['POST'])
def title_description():
    return


@app.route('/collect',  methods=['POST'])
def collect():
    return


@app.route('/collect-desc',  methods=['POST'])
def collect_desc():
    return


@app.route('/get-movie-recs', methods=['GET'])
def get_movie_recs():
    return 


@app.route('/get-tv-recs', methods=['GET'])
def get_tv_recs():
    return


@app.route('/get-description', methods=['GET'])
def get_description():
    return


def get_movie_genre_int(genre):
    movie_genres = {    "action": 28,
                        "adventure": 12,
                        "animation": 16,
                        "comedy": 35,
                        "crime": 80,
                        "documentary": 99,
                        "drama": 18,
                        "family": 10751,
                        "fantasy": 14,
                        "history": 36,
                        "horror": 27,
                        "music": 10402,
                        "mystery": 9648,
                        "romance": 10749,
                        "sci-fi": 878,
                        "tv-movie": 10770,
                        "thriller": 53,
                        "war": 10752,
                        "western": 37
                    }
    
    genre_int = movie_genres.get(genre, None)

    return genre_int


def get_tv_genre_int(genre):
    tv_genres = {   "action": 10759,
                    "animation": 16,
                    "comedy": 35,
                    "crime": 80,
                    "documentary": 99,
                    "drama": 18,
                    "family": 10751,
                    "kids": 10762,
                    "mystery": 9648,
                    "news": 10763,
                    "reality": 10764,
                    "sci-fi": 10765,
                    "soap": 10766,
                    "talk": 10767,
                    "war": 10768,
                    "western": 37
                }
    
    genre_int = tv_genres.get(genre, None)

    return genre_int


def is_unseen(media_title):
    
    return
