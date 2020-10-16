from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.urls import reverse
from datetime import datetime
from django.core.paginator import Paginator


from .forms import ManifestationForm, SealdescriptionForm
from .models import Item, Digisigitemview, Repository, Digisigseriesview, CountiesUk, Nature, RepresentationType, DigisigManifestationview, TimegroupA, Shape, Digisigsealdescriptionview, Seal

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
	manifestation_object = DigisigManifestationview.objects.all()

	if request.method == 'POST':
		print(request.POST)

		form = ManifestationForm(request.POST)
		if form.is_valid():

			qrepository = form.cleaned_data['repository']	
			qseries = form.cleaned_data['series']
			qrepresentation_type = form.cleaned_data['representation']
			qnature = form.cleaned_data['nature']
			qcounties_uk = form.cleaned_data['location']
			qtimegroup = form.cleaned_data['timegroup']
			qshape = form.cleaned_data['shape']
			qshelfmark = form.cleaned_data['name']
			qpagination = form.cleaned_data['pagination']

			rows = len(manifestation_object)
			print(rows)

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

			if len(qshelfmark) > 0:
			 	manifestation_object = manifestation_object.filter(shelfmark__contains=qshelfmark)

			form = ManifestationForm(request.POST)

	else:
		form = ManifestationForm()
		qpagination = 1

# preparing the data for the manifestation object
	qpaginationend = int(qpagination) * 10
	qpaginationstart = int(qpaginationend) -9 
	totalrows = len(manifestation_object)

	# if the dataset is less than the page limit
	if qpaginationend > totalrows:
		qpaginationend = totalrows

	manifestation_object = manifestation_object[qpaginationstart:qpaginationend]
	totaldisplay = str(qpaginationstart) + " - " + str(qpaginationend)

	pagecountercurrent = qpagination
	pagecounternext = int(qpagination)+1
	pagecounternextnext = int(qpagination)+2

# this code prepares the list of links to associated seal descriptions for each seal manifestation
	sealdescriptions = []
	for e in manifestation_object:
		testvalue = e.fk_seal
		manifestation = e.id_manifestation
		testsealdescriptionset = Digisigsealdescriptionview.objects.filter(
			fk_seal=testvalue)
		for f in testsealdescriptionset:
			sealdescriptions.append((manifestation, f.id_sealdescription))

	context = { 
			'manifestation_object': manifestation_object,
			'sealdescriptions': sealdescriptions,
			'totalrows': totalrows,
			'totaldisplay': totaldisplay,
			'form': form,
			'pagecountercurrent': pagecountercurrent,
			'pagecounternext': pagecounternext,
			'pagecounternextnext': pagecounternextnext,
			}

	template = loader.get_template('sealquery/search.html')					
	return HttpResponse(template.render(context, request))



def sealdescription_search(request):
	sealdescription_object = Digisigsealdescriptionview.objects.all()


	if request.method == 'POST':
		print(request.POST)

		form = SealdescriptionForm(request.POST)
		if form.is_valid():
			rows = len(sealdescription_object)
			print(rows)
	else:
		form = SealdescriptionForm()

	sealdescription_object = sealdescription_object[:10]
#	totaldisplay = str(qpaginationstart) + " - " + str(qpaginationend)

	context = {
		'sealdescription_object': sealdescription_object,
		'form': form,
		}

	template = loader.get_template('sealquery/sealdescription_search.html')
	return HttpResponse(template.render(context, request))


def advanced_search(request):

	context = {
	}

	template = loader.get_template('sealquery/advanced_search.html')					
	return HttpResponse(template.render(context, request))

# entity
def entity(request, digisig_entity_number):

	#item = 0, seal=1, manifestation=2, sealdescription=3
	finalcharacter = digisig_entity_number[7:] 

	if finalcharacter == '0':
		item_object = get_object_or_404(Digisigitemview, id_item=digisig_entity_number)
		manifestation_object = DigisigManifestationview.objects.filter(fk_item=digisig_entity_number).order_by('number', 'faceterm')
		totalrows = len(manifestation_object)
		item_info = manifestation_object[:1]
		manifestation_object = manifestation_object[:10]
		totaldisplay = len(manifestation_object)


		template = loader.get_template('sealquery/item.html')
		context = {
			'item_object': item_object,
			'manifestation_object': manifestation_object,
			'item_info': item_info,
			'totalrows': totalrows,
			'totaldisplay': totaldisplay,
			}
		return HttpResponse(template.render(context, request))

	if finalcharacter == '1':
		seal_object = get_object_or_404(Seal, id_seal=digisig_entity_number)
		manifestation_object = DigisigManifestationview.objects.filter(fk_seal=digisig_entity_number)
		totalrows = len(manifestation_object)

		sealdescriptions = []
		for e in manifestation_object:
			print ('hello')
			testvalue = e.fk_seal
			manifestation = e.id_manifestation
			testsealdescriptionset = Digisigsealdescriptionview.objects.filter(
				fk_seal=testvalue)
			for f in testsealdescriptionset:
				sealdescriptions.append((manifestation, f.id_sealdescription))

		template = loader.get_template('sealquery/seal.html')
		context = {
			'seal_object': seal_object,
			'manifestation_object': manifestation_object,
			'sealdescriptions': sealdescriptions,
			'totalrows': totalrows,
			}

		print (manifestation_object[:1])
		return HttpResponse(template.render(context, request))

	if finalcharacter == '2':
		return HttpResponse("you are looking at entity %s." % digisig_entity_number)

	if finalcharacter == '3':
		sealdescription_object = get_object_or_404(Digisigsealdescriptionview, id_sealdescription=digisig_entity_number)

		template = loader.get_template('sealquery/sealdescription.html')
		context = {
			'sealdescription_object': sealdescription_object,
			}

		return HttpResponse(template.render(context, request))

	else:
		return HttpResponse("another entity %s." % finalcharacter)

def entity_fail(request, entity_phrase):
	return HttpResponse("%s is not an entity I know about." % entity_phrase)