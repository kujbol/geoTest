from django import forms


class LoadWFSDetailsForm(forms.Form):
    def __init__(self, question_fields, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['question_source'] = forms.ChoiceField(
            choices=[(question, question) for question in question_fields]
        )

    geometry_source = forms.CharField()
