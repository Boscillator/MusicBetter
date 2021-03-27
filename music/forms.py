from django import forms

class PieceForm(forms.Form):
    piece_name = forms.CharField(label="The piece you're looking for", max_length=200)