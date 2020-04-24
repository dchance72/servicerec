from django.forms import ModelForm
from tracksvc.models import CheckEvent

class CheckForm(ModelForm):
    class Meta:
        model = CheckEvent
        fields = ['when', 'user', 'state', 'notes']
