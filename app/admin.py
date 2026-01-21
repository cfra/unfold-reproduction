from django.contrib import admin
from unfold.admin import ModelAdmin

from .models import DemoModel


@admin.register(DemoModel)
class DemoModelAdminClass(ModelAdmin):
    fieldsets = [
        (
            None,
            {
                "fields": [
                    "field_a",
                    "field_b",
                    "field_c",
                    "field_d",
                    "field_e",
                ]
            }
        ),
        (
            "Fieldset 1",
            {
                "classes": ["collapse"],
                "fields": [
                    "field_f",
                    "field_g",
                    "field_h",
                    "field_i",
                    "field_j",
                ]
            }
        ),
        (
            "Fieldset 2",
            {
                "classes": ["collapse"],
                "fields": [
                    "field_k",
                    "field_l",
                    "field_m",
                    "field_n",
                ]
            }
        ),
    ]
