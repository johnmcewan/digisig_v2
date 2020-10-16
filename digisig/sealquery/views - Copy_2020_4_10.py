from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.urls import reverse
from datetime import datetime


from .forms import ManifestationForm
from .models import Item, Digisigitemview, Repository, Digisigseriesview, CountiesUk, Nature, RepresentationType, DigisigManifestationview, TimegroupA, Shape

# Create your views here.

# test
def test(request):
	return HttpResponse("Hello World")


# index and blank 
def index(request):
	template = loader.get_template('sealquery/index.html')
	context = {
			}
	return HttpResponse(template.render(context, request))

# search
def search(request):
	repository_object = Repository.objects.order_by('repository_fulltitle')
	series_object = Digisigseriesview.objects.order_by('fk_repository', 'series_name') 
	county_object = CountiesUk.objects.order_by('location_county')
	nature_object = Nature.objects.order_by('nature_name')
	representation_object = RepresentationType.objects.order_by('representation_type')
	timegroup_object = TimegroupA.objects.order_by('pk_timegroup_a')
	shape_object = Shape.objects.order_by('shape')

	manifestation_object = DigisigManifestationview.objects.all()


	if request.method == 'POST':
		print(request.POST)
		qrepository = request.POST.get('repository_options')
		qseries = request.POST.get('series_options')
		qrepresentation_type = request.POST.get('photograph_type')
		qnature = request.POST.get('nature')
		qcounties_uk = request.POST.get('location')
		qtimegroup = request.POST.get('timegroup')
		qshape = request.POST.get('shape_options')
		qshelfmark = request.POST.get('shelfmark')
		default_options = request.POST

		if qrepository is not None:
			if int(qrepository) > 0:
				manifestation_object = manifestation_object.filter(
					fk_repository=qrepository)

		if qseries is not None:
			if int(qseries) > 0:
				manifestation_object = manifestation_object.filter(
					fk_series=qseries)

		if qrepresentation_type is not None:
			if int(qrepresentation_type) > 0:
				manifestation_object = manifestation_object.filter(
					fk_representation_type=qrepresentation_type)

		if qnature is not None:
			if int(qnature) > 0:
			 	manifestation_object = manifestation_object.filter(
			 		fk_nature=qnature)

		if qcounties_uk is not None:
			if int(qcounties_uk) > 0:
			 	manifestation_object = manifestation_object.filter(
			 		fk_counties_uk=qcounties_uk)	 	

		if qtimegroup is not None:
			if int(qtimegroup) > 0:
				temporalperiod_target = (TimegroupA.objects.get(pk_timegroup_a = qtimegroup))	
				yearstart = (temporalperiod_target.timegroup_a_startdate)
				manifestation_object = manifestation_object.filter(
					repository_startdate__lt=datetime.strptime(str(yearstart), "%Y")).filter(
					repository_enddate__gt=datetime.strptime(str(yearstart+50), "%Y"))

		if qshape is not None:
			if int(qshape) > 0:
			 	manifestation_object = manifestation_object.filter(
			 		fk_shape=qshape)

		if qshelfmark is not None:
		 	manifestation_object = manifestation_object.filter(shelfmark__contains=qshelfmark)

		totalrows = len(manifestation_object)
		manifestation_object = manifestation_object[:10]

		form = ManifestationForm()

	else:
		totalrows = len(manifestation_object)
		manifestation_object = manifestation_object[:10]
		default_options = {
			'repository_object': 0,
			'series_object': 0,
			'county_object': 0,
			'nature_object': 0,
			'representation_object': 0,
			'timegroup_object': 0,
			'shape_object': 0,
			'shelfmark': "",
			'totalrows': totalrows,
			}

		form = ManifestationForm()


	context = { 'repository_object': repository_object,
			'series_object': series_object,
			'county_object': county_object,
			'nature_object': nature_object,
			'representation_object': representation_object,
			'manifestation_object': manifestation_object,
			'timegroup_object': timegroup_object,
			'shape_object': shape_object,
			'totalrows': totalrows,
			'default_options': default_options,
			'form': form,
			}

	template = loader.get_template('sealquery/search.html')					
	return HttpResponse(template.render(context, request))

# def search2(request, qrepository, qseries, qphotograph, qnature, qlocation):
# 	template = loader.get_template('sealquery/search.html')
# 	repository_object = Repository.objects.order_by('repository_fulltitle')
# 	series_object = Series.objects.order_by('series_name')
# 	county_object = CountiesUk.objects.order_by('location_county')
# 	nature_object = Nature.objects.order_by('nature_name')
# 	representation_object = RepresentationType.objects.order_by('representation_type')
# 	manifestation_object = DigisigManifestationview.objects.filter(
# 		fk_repository=qrepository
# 		). filter(
# 		fk_series=qseries
# 		). filter(
# 		fk_representation_type=qphotograph
# 		). filter(
# 		fk_nature=qnature
# 		). filter(
# 		fk_counties_uk=qlocation
# 		)

# 	context = { 'repository_object': repository_object,
# 				'series_object': series_object,
# 				'county_object': county_object,
# 				'nature_object': nature_object,
# 				'representation_object': representation_object,
# 				'manifestation_object': manifestation_object,
# 			}
# 	return HttpResponse(template.render(context, request))

# entity
def entity(request, digisig_entity_number):

	#item = 0, seal=1, manifestation=2, sealdescription=3
	finalcharacter = digisig_entity_number[7:] 
	if finalcharacter == '0':
		item_object = get_object_or_404(Digisigitemview, id_item=digisig_entity_number)

		template = loader.get_template('sealquery/item.html')
		context = {
			'id_item': item_object.id_item,
			'item_repository': item_object.repository_fulltitle,
			'item_series': item_object.series_shortname,
			'item_shelfmark':item_object.shelfmark,
			}

	return HttpResponse(template.render(context, request))

	if finalcharacter == '1':
		return HttpResponse("you are looking at entity %s." % digisig_entity_number)

	if finalcharacter == '2':
		return HttpResponse("you are looking at entity %s." % digisig_entity_number)

	if finalcharacter == '3':
		return HttpResponse("you are looking at entity %s." % digisig_entity_number)

	else:
		return HttpResponse("another entity %s." % finalcharacter)

def entity_fail(request, entity_phrase):
	return HttpResponse("%s is not an entity I know about." % entity_phrase)