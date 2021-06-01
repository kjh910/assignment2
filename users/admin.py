from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):

    """ Custom User Admin """
    
    list_display = (
        "username",
        "first_name",
        "last_name",
        "email",
        "is_active",
        "language",
        "superhost",
        "is_staff",
        "is_superuser",
        "bio",
        "preference",
        "language",
        "favourite_book_genres",
        "favourite_movie_genres",
    )
    
    list_filter = UserAdmin.list_filter + \
        (
            "superhost",
            "bio",
            "preference",
            "language",
            "favourite_book_genres",
            "favourite_movie_genres",
        )

    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile",
            {
                "fields": (
                    "bio",
                    "preference",
                    "language",
                    "favourite_book_genres",
                    "favourite_movie_genres",
                    "superhost",
                )
            },
        ),
    )