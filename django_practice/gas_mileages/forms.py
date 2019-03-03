from django import forms

from .models import GasMileage


class GasMileageForm(forms.ModelForm):

    class Meta:
        model = GasMileage
        fields = ("user", "bike", "refill_date", "trip", "amount", "price")
