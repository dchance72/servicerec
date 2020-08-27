from django.forms import ModelForm
from tracksvc.models import CheckEvent, Firearm

class CheckForm(ModelForm):
    class Meta:
        model = CheckEvent
        fields = ['when', 'user', 'state', 'notes']

class FirearmForm(ModelForm):
    class Meta:
        model = Firearm
        fields = ['make', 'model', 'serial', 'location']

