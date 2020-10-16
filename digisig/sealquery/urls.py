from django.urls import path, re_path

from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('index', views.index, name='index'),
	path('search', views.search, name='search'),
	path('sealdescription_search', views.sealdescription_search, name='sealdescription_search'),
	path('advanced_search', views.advanced_search, name='advanced_search'),
	path('search/<int:qrepository>/<int:qseries>/<int:qphotograph>/<int:qnature>/<int:qlocation>/', views.search),
	re_path(r'entity/(?P<digisig_entity_number>[0-9]{8})', views.entity, name='entity'),
	path('entity/<str:entity_phrase>', views.entity_fail, name='entity_fail'),
	]