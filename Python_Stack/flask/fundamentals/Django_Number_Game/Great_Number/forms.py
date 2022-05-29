from django import forms


class PlayerNameForm(forms.Form):
    player_name = forms.CharField(max_length=100)
