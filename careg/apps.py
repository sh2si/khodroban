from tabnanny import verbose
from django.apps import AppConfig


class CaregConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "careg"
    verbose_name = "ثبت خودرو"
