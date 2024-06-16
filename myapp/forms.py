# myapp/forms.py

from django import forms

class PredictionForm(forms.Form):
    Electricity_from_renewables = forms.FloatField(label='Electricity from renewables (TWh)')
    Value_co2_emissions_kt_by_country = forms.FloatField(label='CO2 Emissions (kt by country)')
    renewables_percentage = forms.FloatField(label='Renewables (% equivalent primary energy)')
    gdp_growth = forms.FloatField(label='GDP Growth (%)')
