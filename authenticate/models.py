from django.db import models
from django.contrib import admin

class LandInformations(models.Model):
    land_id = models.AutoField(primary_key=True, unique=True, default=0)
    owner_name = models.CharField(max_length=100, default='')
    plot_number = models.CharField(max_length=50, default='')
    street_name = models.CharField(max_length=100, default='')
    ward_number = models.CharField(max_length=50, default='')
    block_number = models.CharField(max_length=50, default='')
    sub_division = models.CharField(max_length=100, default='')
    survey_number = models.CharField(max_length=50, default='')
    district = models.CharField(max_length=100, default='')
    taluk = models.CharField(max_length=100, default='')
    state = models.CharField(max_length=100, default='')

    URBAN_RURAL_CHOICES = [
        ('Urban', 'Urban'),
        ('Rural', 'Rural'),
    ]
    urban_or_rural = models.CharField(max_length=10, choices=URBAN_RURAL_CHOICES, default='Urban')

    LAND_TYPE_CHOICES = [
        ('Agricultural', 'Agricultural'),
        ('Private', 'Private'),
        ('Government', 'Government'),
    ]
    land_type = models.CharField(max_length=15, choices=LAND_TYPE_CHOICES, default='Agricultural')

    PATTA_CHITTA_CHOICES = [
        ('Patta', 'Patta'),
        ('Chitta', 'Chitta'),
    ]
    patta_or_chitta_status = models.CharField(max_length=10, choices=PATTA_CHITTA_CHOICES, default='Patta')

    approval_status = models.CharField(max_length=100, default='')
    land_coordinates = models.CharField(max_length=10000, default='')

    # Add the last_tax_paid field
    last_tax_paid = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return str(self.land_id)

class LandInfoAdmin(admin.ModelAdmin):
    list_display = ('owner_name', 'plot_number', 'street_name', 'ward_number', 'block_number', 'sub_division', 'survey_number', 'district', 'taluk', 'state', 'urban_or_rural', 'land_type', 'patta_or_chitta_status', 'approval_status', 'last_tax_paid', 'land_coordinates')

