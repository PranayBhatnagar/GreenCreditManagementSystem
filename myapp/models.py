# myapp/models.py

from django.db import models

class PredictionInput(models.Model):
    electricity_from_renewables = models.FloatField()
    co2_emissions = models.FloatField()
    renewables_percentage = models.FloatField()
    gdp_growth = models.FloatField()
    prediction_electricity = models.FloatField(blank=True, null=True)
    prediction_co2_emissions = models.FloatField(blank=True, null=True)
    prediction_renewables_percentage = models.FloatField(blank=True, null=True)
    prediction_gdp_growth = models.FloatField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

