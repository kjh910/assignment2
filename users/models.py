from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    """ Custom User Model """

    PREFERENCE_BOOKS = "books"
    PREFERENCE_MOVIES = "movies"

    PREFERENCE = (
        (PREFERENCE_BOOKS, "Books"),
        (PREFERENCE_MOVIES, "Movies"),
    )

    LANGUAGE_ENGLISH = "en"
    LANGUAGE_KOREAN = "kr"

    LANGUAGE_CHOICES = (
      (LANGUAGE_ENGLISH, "English"), 
      (LANGUAGE_KOREAN, "Korean")
    )

    BOOK_GENRE_FOOD = "food"
    BOOK_GENRE_HISTORY = "history"
    BOOK_GENRE_MEMOIR = "memoir"
    BOOK_GENRE_POLITICS = "politics"
    BOOK_GENRE_SCIENCE_FICTION = "science Fiction"

    FAVOURITE_BOOK_GENRES = (
      (BOOK_GENRE_FOOD, "Food"), 
      (BOOK_GENRE_HISTORY, "History"),
      (BOOK_GENRE_MEMOIR, "Memoir"),
      (BOOK_GENRE_POLITICS, "Politics"),
      (BOOK_GENRE_SCIENCE_FICTION, "Science Fiction")
    )
    
    MOVIE_GENRE_ACTION = "action"
    MOVIE_GENRE_ROMANCE = "romance"
    MOVIE_GENRE_MISTERY = "mistery"
    MOVIE_GENRE_HORROR = "horror"
    MOVIE_GENRE_COMEDY = "comedy"

    FAVOURITE_MOVIE_GENRES = (
      (MOVIE_GENRE_ACTION, "Action"), 
      (MOVIE_GENRE_ROMANCE, "Romance"),
      (MOVIE_GENRE_MISTERY, "Mistery"),
      (MOVIE_GENRE_HORROR, "Horror"),
      (MOVIE_GENRE_COMEDY, "Comedy")
    )

    bio = models.TextField(default="", blank=True)
    preference = models.CharField(
      choices=PREFERENCE, max_length=20, null=True, blank=True
    )
    language = models.CharField(
        choices=LANGUAGE_CHOICES, max_length=2, null=True, blank=True
    )
    favourite_book_genres = models.CharField(
        choices=FAVOURITE_BOOK_GENRES, max_length=20, null=True, blank=True
    )
    favourite_movie_genres = models.CharField(
        choices=FAVOURITE_MOVIE_GENRES, max_length=20, null=True, blank=True
    )
    superhost = models.BooleanField(default=False)