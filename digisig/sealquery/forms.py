from django import forms

from .models import Digisigseriesview, Digisigrepositoriesview, Digisigsealdescriptionview, CountiesUk, Nature, RepresentationType, TimegroupA, Shape


#Form for querying seal impressions
repositories_options = [('0', 'blank')]
series_options = [('0', 'blank')]
location_options = [('0', 'blank')]
nature_options = [('0', 'blank')]
representation_options = [('0', 'blank')]
timegroup_options = [('0', 'blank')]
shape_options = [('0', 'blank')]

for e in Digisigrepositoriesview.objects.order_by('repository_fulltitle'):
	repositories_options.append((e.fk_repository, e.repository_fulltitle))

for e in Digisigseriesview.objects.order_by('fk_repository', 'series_name'):
	series_options.append((e.pk_series, e.series_name))

for e in CountiesUk.objects.order_by('location_county'):
	location_options.append((e.pk_counties_uk, e.location_county))

for e in Nature.objects.order_by('nature_name'):
	nature_options.append((e.pk_nature, e.nature_name))

for e in RepresentationType.objects.order_by('representation_type'):
	representation_options.append((e.pk_representation_type, e.representation_type))
	
for e in TimegroupA.objects.order_by('pk_timegroup_a'):
	timegroup_options.append((e.timegroup_a, e.timegroup_a_range))

for e in Shape.objects.order_by('shape'):
	shape_options.append((e.pk_shape, e.shape))

class ManifestationForm(forms.Form):
	repository = forms.ChoiceField(choices=repositories_options, required=False)
	series = forms.ChoiceField(choices=series_options, required=False)	
	location = forms.ChoiceField(choices=location_options, required=False)
	nature = forms.ChoiceField(choices=nature_options, required=False)
	representation = forms.ChoiceField(choices=representation_options, required=False)
	timegroup = forms.ChoiceField(choices=timegroup_options, required=False)
	shape = forms.ChoiceField(choices=shape_options, required=False)
	name = forms.CharField(label='Repository Identifier', max_length=100, required=False)
	pagination = forms.IntegerField(initial=1, widget=forms.HiddenInput)







#Form for quering seal descriptions

collections_options = [('0', 'blank')]

for e in Digisigsealdescriptionview.objects.order_by('collection_shorttitle').distinct('collection_shorttitle'):
	collections_options.append((e.fk_collection, e.collection_shorttitle))

print (collections_options)	

class SealdescriptionForm(forms.Form):
	pagination = forms.IntegerField(initial=1, widget=forms.HiddenInput)
	collection = forms.ChoiceField(choices=collections_options, required=False)
	cataloguecode = forms.CharField(label='Catalogue Identifier', max_length=100, required=False)