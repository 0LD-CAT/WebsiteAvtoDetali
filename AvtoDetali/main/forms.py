from django import forms

class MyForm(forms.Form):
    my_choices = (
        ('value1', 'Lada'),
        ('value2', 'BMW'),
        ('value3', 'Mazda'),
        ('value4', 'Mercedes'),
        ('value5', 'Volvo'),
        ('value6', 'Honda')
    )
    my_field = forms.ChoiceField(label='Выберите марку машины:', choices=my_choices, widget=forms.Select())