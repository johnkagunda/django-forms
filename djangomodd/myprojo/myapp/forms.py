from django import forms

DEP = (
    ('dep1', 'Department 1'),
    ('dep2', 'Department 2'),
    ('dep3', 'Department 3'),
    ('dep4', 'Department 4'),
)

class Formy(forms.Form):
    first_name = forms.CharField(max_length=200)
    second_name = forms.CharField(max_length=200)
    time_log = forms.TimeField(widget=forms.TimeInput(format='%H:%M'))
    DPT = forms.ChoiceField(choices=DEP)
