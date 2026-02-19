from django.contrib import admin
from unfold.admin import ModelAdmin
from unfold.decorators import action

from .models import DemoModel


@admin.register(DemoModel)
class DemoModelAdminClass(ModelAdmin):
    actions_detail = ["example_action"]

    @action(
        description="Example Action",
        permissions=["app.add_demomodel"],
        url_path="example"
    )
    def example_action(self, request, object_id):
        raise NotImplementedError
