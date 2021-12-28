from django.contrib import admin
from django.utils.html import format_html
from .models import Place, Image
import traceback


class ImageInline(admin.TabularInline):
    model = Image
    readonly_fields = ["image_preview",]
    fields = ['image', 'image_preview', 'position']

    def image_preview(self, obj):
        try:
            html = format_html('<img src="{url}" height=200px />',
                url = obj.image.url
            )
            return html
        except Exception as err:
            print(err)
            traceback.print_exc()
  

@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]
