from django import forms

PANEL_CHOICES = [
            ('', 'Chart type'),
            ('Pie', 'Pie chart'),
            ('Bar', 'Bar chart'),
            ('Treemap', 'Treemap chart'),
            ]

class AddGitstatsForm(forms.Form):
    user_name = forms.CharField()
    git_profile = forms.CharField()
    panel_type = forms.ChoiceField(choices=PANEL_CHOICES)
    git_profile_description = forms.CharField()

