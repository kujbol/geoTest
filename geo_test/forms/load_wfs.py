from django import forms
from django.forms import formset_factory


class LoadWFSForm(forms.Form):
    url = forms.URLField()


class WFSFeatureForm(forms.Form):
    id = forms.IntegerField()
    name = forms.CharField(help_text='Title')
    feature_count = forms.IntegerField(help_text='Id of layer')


WFSFeatureFormSet = formset_factory(WFSFeatureForm)
