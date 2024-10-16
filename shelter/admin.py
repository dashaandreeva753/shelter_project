from django.contrib import admin

from shelter.models import Pet, Shelter


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ('animal', 'name', 'age', 'description', 'health')
    list_filter = ("name", "age",)
    search_fields = ("name", "description",)


@admin.register(Shelter)
class ShelterAdmin(admin.ModelAdmin):
    list_display = ('title', 'address', 'phone', 'country', 'places')
    list_filter = ("title", "address",)
    search_fields = ("title", "phone",)
