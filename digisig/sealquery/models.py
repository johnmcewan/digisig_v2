# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

from django.db import models
from django.forms import ModelForm


class Access(models.Model):
    pk_access = models.IntegerField(primary_key=True)
    access_level = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'access'


class Approximation(models.Model):
    pk_approximation = models.AutoField(primary_key=True)
    approximation_temporal = models.TextField(blank=True, null=True)
    approximation_physical = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'approximation'


class Approximation2(models.Model):
    pk_approximation2 = models.AutoField(primary_key=True)
    approximation2_temporal = models.TextField(blank=True, null=True)
    approximation2_physical = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'approximation_2'


class Armament(models.Model):
    pk_armament = models.AutoField(primary_key=True)
    armament = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'armament'


class Attachment(models.Model):
    pk_attachment = models.AutoField(primary_key=True)
    attachment = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'attachment'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Catalogue(models.Model):
    pk_catalogue = models.AutoField(primary_key=True)
    title = models.TextField(blank=True, null=True)
    fk_access = models.IntegerField(blank=True, null=True)
    publicationdate_start = models.IntegerField(blank=True, null=True)
    publicationdate_end = models.IntegerField(blank=True, null=True)
    uri_catalogue = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catalogue'


class Certainty(models.Model):
    pk_certainty = models.AutoField(primary_key=True)
    certainty = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'certainty'


class Class(models.Model):
    class_number = models.IntegerField()
    class_name = models.TextField(blank=True, null=True)
    classnotation = models.TextField(blank=True, null=True)
    classdefinition = models.TextField(blank=True, null=True)
    classtitle = models.TextField(blank=True, null=True)
    level = models.IntegerField(blank=True, null=True)
    level1 = models.IntegerField(blank=True, null=True)
    level2 = models.IntegerField(blank=True, null=True)
    level3 = models.IntegerField(blank=True, null=True)
    level4 = models.IntegerField(blank=True, null=True)
    level5 = models.IntegerField(blank=True, null=True)
    level6 = models.IntegerField(blank=True, null=True)
    level7 = models.IntegerField(blank=True, null=True)
    level8 = models.IntegerField(blank=True, null=True)
    level9 = models.IntegerField(blank=True, null=True)
    level10 = models.IntegerField(blank=True, null=True)
    fk_seal_example = models.IntegerField(blank=True, null=True)
    printphrase_class = models.TextField(blank=True, null=True)
    printindex = models.TextField(blank=True, null=True)
    class_sortorder = models.IntegerField(blank=True, null=True)
    datasetwales = models.BooleanField(blank=True, null=True)
    datasetlondon = models.BooleanField(blank=True, null=True)
    stub = models.TextField(blank=True, null=True)
    fk_face_example = models.IntegerField(blank=True, null=True)
    fk_representation_example = models.IntegerField(blank=True, null=True)
    cases = models.IntegerField(blank=True, null=True)
    id_class = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'class'


class Collection(models.Model):
    pk_collection = models.AutoField(primary_key=True)
    collection_shorttitle = models.TextField(blank=True, null=True)
    collection_fulltitle = models.TextField(blank=True, null=True)
    collection_pagereference = models.TextField(blank=True, null=True)
    fk_unit = models.IntegerField(blank=True, null=True)
    fk_catalogue = models.IntegerField(blank=True, null=True)
    collection_volume = models.TextField(blank=True, null=True)
    fk_contributor = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'collection'


class Colour(models.Model):
    pk_colour = models.AutoField(primary_key=True)
    colour = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'colour'


class Connection(models.Model):
    pk_connection = models.AutoField(primary_key=True)
    connection = models.TextField(blank=True, null=True)
    fk_repository = models.IntegerField(blank=True, null=True)
    thumb = models.TextField(blank=True, null=True)
    medium = models.TextField(blank=True, null=True)
    connection_description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'connection'


class ConnectionImages(models.Model):
    pk_connection_images = models.AutoField(primary_key=True)
    medium = models.TextField(blank=True, null=True)
    thumb = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'connection_images'


class Contributor(models.Model):
    pk_contributor = models.AutoField(primary_key=True)
    name_first = models.TextField(blank=True, null=True)
    name_last = models.TextField(blank=True, null=True)
    name_middle = models.TextField(blank=True, null=True)
    email = models.TextField(blank=True, null=True)
    uri_contributor = models.TextField(db_column='URI_contributor', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'contributor'


class CountiesUk(models.Model):
    location_county = models.TextField(blank=True, null=True)
    fk_locationtype = models.IntegerField(blank=True, null=True)
    fk_gazeteer = models.IntegerField(blank=True, null=True)
    pk_counties_uk = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'counties_uk'


class Descriptor(models.Model):
    pk_descriptor = models.AutoField(primary_key=True)
    descriptor_modern = models.TextField(blank=True, null=True)
    descriptor_original = models.TextField(blank=True, null=True)
    descriptor_comment = models.TextField(blank=True, null=True)
    fk_gender = models.IntegerField(blank=True, null=True)
    fk_descriptortype = models.IntegerField(blank=True, null=True)
    fk_language = models.IntegerField(blank=True, null=True)
    indexphrase = models.TextField(blank=True, null=True)
    indexentry = models.TextField(blank=True, null=True)
    exclude = models.BooleanField(blank=True, null=True)
    includeoriginal = models.BooleanField(blank=True, null=True)
    fk_descriptor = models.IntegerField(blank=True, null=True)
    crossreferencephrase = models.TextField(blank=True, null=True)
    indexentry_format = models.TextField(blank=True, null=True)
    missingmainentry = models.BooleanField(blank=True, null=True)
    article = models.BooleanField(blank=True, null=True)
    comma = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'descriptor'


class Descriptortype(models.Model):
    pk_descriptortype = models.IntegerField(blank=True, null=True)
    descriptortype = models.CharField(max_length=255, blank=True, null=True)
    descriptortype_definition = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'descriptortype'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class DurhamSeal(models.Model):
    fk_individual_realizer = models.IntegerField(blank=True, null=True)
    fk_certainty_realizer = models.IntegerField(blank=True, null=True)
    motif_obverse = models.TextField(blank=True, null=True)
    motif_reverse = models.TextField(blank=True, null=True)
    legend_obverse = models.CharField(max_length=255, blank=True, null=True)
    legend_reverse = models.CharField(max_length=255, blank=True, null=True)
    biface_seal = models.CharField(max_length=255, blank=True, null=True)
    temp_pk_durhamsealid = models.IntegerField(blank=True, null=True)
    temp_durham_number = models.IntegerField(blank=True, null=True)
    temp_id_durhamtemp = models.IntegerField(blank=True, null=True)
    temp_image_file = models.CharField(max_length=255, blank=True, null=True)
    temp_fk_shape = models.IntegerField(blank=True, null=True)
    temp_phrase_full = models.TextField(blank=True, null=True)
    temp_size_horizontal = models.IntegerField(blank=True, null=True)
    temp_size_vertical = models.IntegerField(blank=True, null=True)
    temp_date_durham = models.CharField(max_length=255, blank=True, null=True)
    temp_person = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'durham_seal'


class Engraving(models.Model):
    pk_engraving = models.IntegerField(blank=True, null=True)
    engraving = models.TextField(blank=True, null=True)
    fk_period = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'engraving'


class Entity(models.Model):
    pk_entity = models.AutoField(primary_key=True)
    entity_view = models.TextField(blank=True, null=True)
    entity_returnedvariables = models.TextField(blank=True, null=True)
    entity_column = models.TextField(blank=True, null=True)
    entity_code = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'entity'


class Event(models.Model):
    part_description = models.TextField(blank=True, null=True)
    part_transcription = models.TextField(blank=True, null=True)
    fk_dateapprox_part_start = models.SmallIntegerField(blank=True, null=True)
    part_daystart = models.SmallIntegerField(blank=True, null=True)
    fk_month_part_start = models.SmallIntegerField(blank=True, null=True)
    part_year_start = models.SmallIntegerField(blank=True, null=True)
    part_comment_start = models.TextField(blank=True, null=True)
    fk_dateapprox_part_end = models.SmallIntegerField(blank=True, null=True)
    part_dayend = models.SmallIntegerField(blank=True, null=True)
    fk_month_part_end = models.SmallIntegerField(blank=True, null=True)
    part_yearend = models.SmallIntegerField(blank=True, null=True)
    part_comment_end = models.TextField(blank=True, null=True)
    fk_period_part = models.SmallIntegerField(blank=True, null=True)
    part_comment = models.TextField(blank=True, null=True)
    fk_locationname = models.IntegerField(blank=True, null=True)
    part_comment_location = models.TextField(blank=True, null=True)
    repository_startdate = models.DateField(blank=True, null=True)
    repository_enddate = models.DateField(blank=True, null=True)
    repository_location = models.TextField(blank=True, null=True)
    repository_description = models.TextField(blank=True, null=True)
    startdate = models.DateField(blank=True, null=True)
    enddate = models.DateField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    pk_event = models.IntegerField(primary_key=True)
    pas_id = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'event'


class EventLocation(models.Model):
    pk_event_location = models.AutoField(primary_key=True)
    event_location = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'event_location'


class EventOld(models.Model):
    pk_event = models.AutoField(primary_key=True)
    fk_item = models.IntegerField(blank=True, null=True)
    event_description = models.TextField(blank=True, null=True)
    event_daystart = models.IntegerField(blank=True, null=True)
    fk_month_event_start = models.IntegerField(blank=True, null=True)
    event_year_start = models.IntegerField(blank=True, null=True)
    fk_dateapprox_event_start = models.IntegerField(blank=True, null=True)
    event_comment_start = models.TextField(blank=True, null=True)
    fk_dateapprox_event_end = models.IntegerField(blank=True, null=True)
    event_dayend = models.IntegerField(blank=True, null=True)
    fk_month_event_end = models.IntegerField(blank=True, null=True)
    event_yearend = models.IntegerField(blank=True, null=True)
    event_comment_end = models.TextField(blank=True, null=True)
    fk_period_event = models.IntegerField(blank=True, null=True)
    event_comment = models.TextField(blank=True, null=True)
    fk_locationname = models.IntegerField(blank=True, null=True)
    event_comment_location = models.TextField(blank=True, null=True)
    repository_startdate = models.DateField(blank=True, null=True)
    repository_enddate = models.DateField(blank=True, null=True)
    repository_location = models.TextField(blank=True, null=True)
    repository_description = models.TextField(blank=True, null=True)
    startdate = models.TextField(blank=True, null=True)
    enddate = models.TextField(blank=True, null=True)
    fk_part = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'event_old'


class Face(models.Model):
    pk_face = models.IntegerField()
    fk_seal = models.ForeignKey('Seal', models.DO_NOTHING, db_column='fk_seal', blank=True, null=True)
    fk_faceterm = models.ForeignKey('Faceterm', models.DO_NOTHING, db_column='fk_faceterm', blank=True, null=True)
    fk_shape = models.ForeignKey('Shape', models.DO_NOTHING, db_column='fk_shape', blank=True, null=True)
    fk_approx_vertical = models.IntegerField(blank=True, null=True)
    face_vertical = models.IntegerField(blank=True, null=True)
    fk_approx_horizontal = models.IntegerField(blank=True, null=True)
    face_horizontal = models.IntegerField(blank=True, null=True)
    legend = models.TextField(blank=True, null=True)
    design = models.TextField(blank=True, null=True)
    face_comment = models.TextField(blank=True, null=True)
    fk_legend_specific = models.IntegerField(blank=True, null=True)
    print_sealmanifestation = models.TextField(blank=True, null=True)
    print_sealsizeandshape = models.TextField(blank=True, null=True)
    fk_class = models.IntegerField(blank=True, null=True)
    datasetparticipation = models.IntegerField(blank=True, null=True)
    dataset_durham = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_face = models.AutoField(primary_key=True)
    temp_bm = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'face'


class Faceterm(models.Model):
    pk_faceterm = models.AutoField(primary_key=True)
    faceterm = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'faceterm'


class Field(models.Model):
    pk_field = models.AutoField(primary_key=True)
    field_title = models.TextField(blank=True, null=True)
    field_order = models.IntegerField(blank=True, null=True)
    field_column = models.TextField(blank=True, null=True)
    field_returnedvariables = models.TextField(blank=True, null=True)
    field_url = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'field'


class Fraction(models.Model):
    pk_fraction = models.AutoField(primary_key=True)
    fraction = models.TextField(blank=True, null=True)
    order = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fraction'


class Gazetteer1999(models.Model):
    join_count = models.FloatField(db_column='Join_Count', blank=True, null=True)  # Field name made lowercase.
    target_fid = models.FloatField(db_column='TARGET_FID', blank=True, null=True)  # Field name made lowercase.
    pk_osgazetteer_1999 = models.FloatField(primary_key=True)
    kmref = models.CharField(max_length=255, blank=True, null=True)
    defname = models.CharField(max_length=255, blank=True, null=True)
    tileref = models.CharField(max_length=255, blank=True, null=True)
    latdeg = models.FloatField(blank=True, null=True)
    latmin = models.FloatField(blank=True, null=True)
    longdeg = models.FloatField(blank=True, null=True)
    longmin = models.FloatField(blank=True, null=True)
    northing = models.FloatField(blank=True, null=True)
    easting = models.FloatField(blank=True, null=True)
    gmt = models.CharField(max_length=255, blank=True, null=True)
    countycode = models.CharField(max_length=255, blank=True, null=True)
    county = models.CharField(max_length=255, blank=True, null=True)
    feat_code = models.CharField(max_length=255, blank=True, null=True)
    ditdate = models.DateTimeField(blank=True, null=True)
    updateco = models.CharField(max_length=255, blank=True, null=True)
    sheet1 = models.FloatField(blank=True, null=True)
    sheet2 = models.FloatField(blank=True, null=True)
    sheet3 = models.FloatField(blank=True, null=True)
    objectid = models.FloatField(db_column='OBJECTID', blank=True, null=True)  # Field name made lowercase.
    fid_ukde_1 = models.FloatField(db_column='FID_UKDe_1', blank=True, null=True)  # Field name made lowercase.
    name_1 = models.CharField(db_column='NAME_1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    county_12 = models.CharField(db_column='COUNTY_12', max_length=255, blank=True, null=True)  # Field name made lowercase.
    abbr_1 = models.CharField(db_column='ABBR_1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    hcs_numb_1 = models.FloatField(db_column='HCS_NUMB_1', blank=True, null=True)  # Field name made lowercase.
    hcs_code_1 = models.CharField(db_column='HCS_CODE_1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    shape_leng = models.FloatField(db_column='Shape_Leng', blank=True, null=True)  # Field name made lowercase.
    shape_area = models.FloatField(db_column='Shape_Area', blank=True, null=True)  # Field name made lowercase.
    fk_counties_uk = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gazetteer_1999'


class Gazetteer1999Vanilla(models.Model):
    primarykey_osdata = models.IntegerField(blank=True, null=True)
    kmref = models.CharField(max_length=255, blank=True, null=True)
    defname = models.CharField(max_length=255, blank=True, null=True)
    tileref = models.CharField(max_length=255, blank=True, null=True)
    latdeg = models.IntegerField(blank=True, null=True)
    latmin = models.FloatField(blank=True, null=True)
    longdeg = models.IntegerField(blank=True, null=True)
    longmin = models.FloatField(blank=True, null=True)
    northing = models.IntegerField(blank=True, null=True)
    easting = models.IntegerField(blank=True, null=True)
    gmt = models.CharField(max_length=255, blank=True, null=True)
    countycode = models.CharField(max_length=255, blank=True, null=True)
    county = models.CharField(max_length=255, blank=True, null=True)
    feat_code = models.CharField(max_length=255, blank=True, null=True)
    ditdate = models.DateTimeField(blank=True, null=True)
    updateco = models.CharField(max_length=255, blank=True, null=True)
    sheet1 = models.IntegerField(blank=True, null=True)
    sheet2 = models.IntegerField(blank=True, null=True)
    sheet3 = models.IntegerField(blank=True, null=True)
    pk_gazetteer = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'gazetteer_1999_vanilla'


class Gender(models.Model):
    pk_gender = models.AutoField(primary_key=True)
    gender = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gender'


class ImageState(models.Model):
    pk_image_state = models.AutoField(primary_key=True)
    image_state = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'image_state'


class Individual(models.Model):
    pk_individual = models.AutoField(primary_key=True)
    corporateentity = models.BooleanField(blank=True, null=True)
    fk_descriptor_title = models.IntegerField(blank=True, null=True)
    fk_descriptor_name = models.IntegerField(blank=True, null=True)
    fk_descriptor_prefix1 = models.IntegerField(blank=True, null=True)
    fk_descriptor_decriptor1 = models.IntegerField(blank=True, null=True)
    fk_punctuationmark = models.IntegerField(blank=True, null=True)
    fk_descriptor_prefix2 = models.IntegerField(blank=True, null=True)
    fk_descriptor_descriptor2 = models.IntegerField(blank=True, null=True)
    fk_descriptor_prefix3 = models.IntegerField(blank=True, null=True)
    fk_descriptor_descriptor3 = models.IntegerField(blank=True, null=True)
    fullname_original = models.TextField(blank=True, null=True)
    fullname_modern = models.TextField(blank=True, null=True)
    alias = models.TextField(blank=True, null=True)
    datestart = models.TextField(blank=True, null=True)
    fk_event_start = models.IntegerField(blank=True, null=True)
    comment_individual_start = models.TextField(blank=True, null=True)
    datestop = models.TextField(blank=True, null=True)
    fk_event_stop = models.TextField(blank=True, null=True)
    comment_individual_stop = models.TextField(blank=True, null=True)
    seal = models.BooleanField(blank=True, null=True)
    civicoffice = models.BooleanField(blank=True, null=True)
    mayor = models.BooleanField(blank=True, null=True)
    comment_mayor = models.TextField(blank=True, null=True)
    sheriff = models.BooleanField(blank=True, null=True)
    comment_sheriff = models.TextField(blank=True, null=True)
    alderman = models.BooleanField(blank=True, null=True)
    fk_event_startalderman = models.IntegerField(blank=True, null=True)
    aldermanstart = models.IntegerField(blank=True, null=True)
    fk_event_endalderman = models.IntegerField(blank=True, null=True)
    aldermanend = models.IntegerField(blank=True, null=True)
    comment_alderman = models.TextField(blank=True, null=True)
    office = models.BooleanField(blank=True, null=True)
    comment_office = models.TextField(blank=True, null=True)
    sussexdataset = models.BooleanField(blank=True, null=True)
    walesid = models.IntegerField(blank=True, null=True)
    dl25id = models.IntegerField(blank=True, null=True)
    fk_occupation = models.IntegerField(blank=True, null=True)
    fk_mld_id = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'individual'


class Item(models.Model):
    pk_item = models.IntegerField()
    fk_repository = models.IntegerField()
    fk_series = models.ForeignKey('Series', models.DO_NOTHING, db_column='fk_series')
    classmark_alpha1 = models.TextField(blank=True, null=True)
    classmark_number1 = models.IntegerField(blank=True, null=True)
    classmark_alpha2 = models.TextField(blank=True, null=True)
    classmark_number2 = models.IntegerField(blank=True, null=True)
    classmark_alpha3 = models.TextField(blank=True, null=True)
    classmark_number3 = models.IntegerField(blank=True, null=True)
    catalogue = models.TextField(blank=True, null=True)
    fk_dateapprox_start = models.IntegerField(blank=True, null=True)
    year_start = models.SmallIntegerField(blank=True, null=True)
    fk_month_start = models.IntegerField(blank=True, null=True)
    day_start = models.SmallIntegerField(blank=True, null=True)
    fk_dateapprox_end = models.IntegerField(blank=True, null=True)
    year_end = models.SmallIntegerField(blank=True, null=True)
    fk_month_end = models.IntegerField(blank=True, null=True)
    day_end = models.SmallIntegerField(blank=True, null=True)
    comment_datestart = models.TextField(blank=True, null=True)
    comment_dateend = models.TextField(blank=True, null=True)
    fk_period = models.IntegerField(blank=True, null=True)
    feature_seal = models.BooleanField(blank=True, null=True)
    feature_support = models.SmallIntegerField(blank=True, null=True)
    photograph = models.BooleanField(blank=True, null=True)
    feature_chirograph = models.BooleanField(blank=True, null=True)
    feature_sealed = models.BooleanField(blank=True, null=True)
    feature_indented = models.BooleanField(blank=True, null=True)
    comment_item = models.TextField(blank=True, null=True)
    item_timestamp = models.DateTimeField(blank=True, null=True)
    id_repository = models.TextField(blank=True, null=True)
    shelfmark = models.TextField(blank=True, null=True)
    id_item = models.BigAutoField(primary_key=True)
    ui_item_repository = models.TextField(blank=True, null=True)
    prefix_alpha1 = models.TextField(blank=True, null=True)
    prefix_number1 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    prefix_alpha2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    prefix_number2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    prefix_alpha3 = models.TextField(blank=True, null=True)
    temp_durham = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    prefix_number3 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'item'


class Language(models.Model):
    pk_language = models.IntegerField(blank=True, null=True)
    language = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'language'


class Legendspecific(models.Model):
    pk_legendspecific = models.AutoField(primary_key=True)
    fk_legendtype = models.ForeignKey('Legendtype', models.DO_NOTHING, db_column='fk_legendtype', blank=True, null=True)
    legendspecific = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'legendspecific'


class Legendtype(models.Model):
    pk_legendtype = models.AutoField(primary_key=True)
    legendtype = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'legendtype'


class Location(models.Model):
    pk_location = models.AutoField(primary_key=True)
    location = models.TextField(blank=True, null=True)
    xcoordinate = models.IntegerField(blank=True, null=True)
    ycoordinate = models.IntegerField(blank=True, null=True)
    fk_locationtype = models.IntegerField(blank=True, null=True)
    fk_gazeteer = models.IntegerField(blank=True, null=True)
    fk_englandwales_parish = models.IntegerField(blank=True, null=True)
    mld_locationname = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'location'


class LocationReference(models.Model):
    fk_part = models.IntegerField(blank=True, null=True)
    fk_locationname = models.IntegerField(blank=True, null=True)
    pk_location_reference = models.AutoField(primary_key=True)
    location_reference = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'location_reference'


class Locationname(models.Model):
    pk_locationname = models.AutoField(primary_key=True)
    locationname = models.TextField(blank=True, null=True)
    fk_location = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'locationname'


class Locationtype(models.Model):
    pk_locationtype = models.IntegerField(primary_key=True)
    locationtype = models.CharField(max_length=255, blank=True, null=True)
    locationcomment = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'locationtype'


class Manifestation(models.Model):
    pk_manifestation = models.IntegerField()
    fk_support = models.ForeignKey('Support', models.DO_NOTHING, db_column='fk_support', blank=True, null=True)
    fk_position = models.IntegerField(blank=True, null=True)
    fk_face = models.ForeignKey(Face, models.DO_NOTHING, db_column='fk_face', blank=True, null=True)
    fk_individual_producer = models.IntegerField(blank=True, null=True)
    fk_certainty_producer = models.IntegerField(blank=True, null=True)
    fragment = models.BooleanField(blank=True, null=True)
    size_vertical = models.IntegerField(blank=True, null=True)
    size_horizontal = models.IntegerField(blank=True, null=True)
    manifestation_legend = models.TextField(blank=True, null=True)
    manifestation_motif = models.TextField(blank=True, null=True)
    my_volume = models.IntegerField(blank=True, null=True)
    my_page = models.IntegerField(blank=True, null=True)
    manifestation_comment = models.TextField(blank=True, null=True)
    fullreference = models.TextField(blank=True, null=True)
    file_photograph = models.TextField(blank=True, null=True)
    briefreference = models.TextField(blank=True, null=True)
    id_repository = models.TextField(blank=True, null=True)
    datasetsussex = models.BooleanField(blank=True, null=True)
    datasetlondon = models.BooleanField(blank=True, null=True)
    datasetlondon_editionnumber = models.IntegerField(blank=True, null=True)
    datasetwales_sealnumber = models.IntegerField(blank=True, null=True)
    datasetwales_manifestationnumber = models.IntegerField(blank=True, null=True)
    datasetdl25 = models.BooleanField(blank=True, null=True)
    datasetdl25_manifestationnumber = models.IntegerField(blank=True, null=True)
    datasetdl25_expressionnumber = models.IntegerField(blank=True, null=True)
    datasetdl25_itemnumber = models.IntegerField(blank=True, null=True)
    datasetbirch = models.IntegerField(blank=True, null=True)
    datasetwales_manifestationsort = models.IntegerField(blank=True, null=True)
    id_manifestation = models.BigAutoField(primary_key=True)
    ui_manifestation_repository = models.TextField(blank=True, null=True)
    fk_image_state = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    datasetbirch_v2 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'manifestation'


class Material(models.Model):
    pk_material = models.AutoField(primary_key=True)
    material = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'material'


class Militia(models.Model):
    pk_milita = models.AutoField(primary_key=True)
    fk_individualreference = models.IntegerField(blank=True, null=True)
    fk_armament = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'militia'


class Month(models.Model):
    pk_month = models.AutoField(primary_key=True)
    month = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'month'


class Nature(models.Model):
    pk_nature = models.AutoField(primary_key=True)
    nature_name = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nature'


class Number(models.Model):
    pk_number = models.AutoField(primary_key=True)
    number = models.TextField(blank=True, null=True)
    number_alternate = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'number'


class Office(models.Model):
    pk_office = models.AutoField(primary_key=True)
    office = models.TextField(blank=True, null=True)
    office_original = models.TextField(blank=True, null=True)
    office_order = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'office'


class ParishEnglandwales(models.Model):
    pk_parish_englandwales = models.IntegerField(primary_key=True)
    hisparishrecordnumber = models.CharField(max_length=255, blank=True, null=True)
    hisparish_serialnumber = models.CharField(max_length=255, blank=True, null=True)
    placename = models.CharField(max_length=255, blank=True, null=True)
    areaclass = models.CharField(max_length=255, blank=True, null=True)
    motherparish = models.CharField(max_length=255, blank=True, null=True)
    placename_alternate = models.CharField(max_length=255, blank=True, null=True)
    county_1844_1888 = models.CharField(db_column='county_1844-1888', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    ossurvey_code = models.CharField(max_length=255, blank=True, null=True)
    ossurveysheet = models.CharField(max_length=255, blank=True, null=True)
    parishnumber_census1851 = models.CharField(max_length=255, blank=True, null=True)
    source = models.CharField(max_length=255, blank=True, null=True)
    reference = models.CharField(max_length=255, blank=True, null=True)
    comments = models.CharField(max_length=255, blank=True, null=True)
    fk_counties_uk = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'parish_englandwales'


class Part(models.Model):
    pk_part = models.IntegerField()
    fk_item = models.IntegerField(blank=True, null=True)
    part_number1 = models.IntegerField(blank=True, null=True)
    part_number2 = models.IntegerField(blank=True, null=True)
    part_alpha1 = models.TextField(blank=True, null=True)
    part_alpha2 = models.TextField(blank=True, null=True)
    part_description = models.TextField(blank=True, null=True)
    part_transcription = models.TextField(blank=True, null=True)
    fk_dateapprox_part_start = models.SmallIntegerField(blank=True, null=True)
    part_daystart = models.SmallIntegerField(blank=True, null=True)
    fk_month_part_start = models.SmallIntegerField(blank=True, null=True)
    part_year_start = models.SmallIntegerField(blank=True, null=True)
    part_comment_start = models.TextField(blank=True, null=True)
    fk_dateapprox_part_end = models.SmallIntegerField(blank=True, null=True)
    part_dayend = models.SmallIntegerField(blank=True, null=True)
    fk_month_part_end = models.SmallIntegerField(blank=True, null=True)
    part_yearend = models.SmallIntegerField(blank=True, null=True)
    part_comment_end = models.TextField(blank=True, null=True)
    fk_period_part = models.SmallIntegerField(blank=True, null=True)
    part_comment = models.TextField(blank=True, null=True)
    fk_locationname = models.IntegerField(blank=True, null=True)
    part_comment_location = models.TextField(blank=True, null=True)
    id_repository_part = models.TextField(blank=True, null=True)
    ui_part_repository = models.TextField(blank=True, null=True)
    repository_startdate = models.DateField(blank=True, null=True)
    repository_enddate = models.DateField(blank=True, null=True)
    repository_location = models.TextField(blank=True, null=True)
    repository_description = models.TextField(blank=True, null=True)
    startdate = models.DateField(blank=True, null=True)
    enddate = models.DateField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    reference_full = models.TextField(blank=True, null=True)
    id_part = models.AutoField(primary_key=True)
    fk_event = models.IntegerField(blank=True, null=True)
    part_number3 = models.IntegerField(blank=True, null=True)
    part_number4 = models.IntegerField(blank=True, null=True)
    part_number5 = models.IntegerField(blank=True, null=True)
    published_full = models.TextField(blank=True, null=True)
    part_letter5 = models.TextField(blank=True, null=True)
    fordham_reference = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'part'


class Period(models.Model):
    pk_period = models.AutoField(primary_key=True)
    period = models.TextField(blank=True, null=True)
    fk_approx_start = models.IntegerField(blank=True, null=True)
    year_start = models.IntegerField(blank=True, null=True)
    fk_month_start = models.IntegerField(blank=True, null=True)
    day_start = models.IntegerField(blank=True, null=True)
    comment_start = models.TextField(blank=True, null=True)
    fk_approx_end = models.IntegerField(blank=True, null=True)
    year_end = models.IntegerField(blank=True, null=True)
    fk_month_end = models.IntegerField(blank=True, null=True)
    day_end = models.IntegerField(blank=True, null=True)
    comment_end = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'period'


class Position(models.Model):
    pk_position = models.AutoField(primary_key=True)
    position = models.TextField(blank=True, null=True)
    position_latin = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'position'


class Prefix(models.Model):
    pk_prefix = models.AutoField(primary_key=True)
    prefix = models.TextField(blank=True, null=True)
    prefix_english = models.TextField(blank=True, null=True)
    fk_separator = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prefix'


class Printgroup(models.Model):
    pk_printgroup = models.AutoField(primary_key=True)
    printgroup = models.TextField(blank=True, null=True)
    printgroup_order = models.IntegerField(blank=True, null=True)
    printgroup_london = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'printgroup'


class Published(models.Model):
    pk_published = models.IntegerField(primary_key=True)
    published_reference_full = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'published'


class Referenceindividual(models.Model):
    pk_referenceindividual = models.AutoField(primary_key=True)
    referenceindividual = models.TextField(blank=True, null=True)
    fk_referencerole = models.ForeignKey('Referencerole', models.DO_NOTHING, db_column='fk_referencerole', blank=True, null=True)
    fk_event = models.IntegerField(blank=True, null=True)
    fk_individualoffice = models.IntegerField(blank=True, null=True)
    fk_individual = models.IntegerField(blank=True, null=True)
    fk_individualnametype = models.IntegerField(blank=True, null=True)
    fk_individualnametitle = models.IntegerField(blank=True, null=True)
    fk_descriptor_name = models.IntegerField(blank=True, null=True)
    fk_descriptor_prefix_1 = models.IntegerField(blank=True, null=True)
    fk_descriptor_1 = models.IntegerField(blank=True, null=True)
    fk_descriptor_prefix_2 = models.IntegerField(blank=True, null=True)
    fk_descriptor_2 = models.IntegerField(blank=True, null=True)
    fk_descriptor_prefix_3 = models.IntegerField(blank=True, null=True)
    fk_descriptor_3 = models.IntegerField(blank=True, null=True)
    referencefullname = models.TextField(blank=True, null=True)
    referencecomment = models.TextField(blank=True, null=True)
    fk_relationship_node2 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'referenceindividual'


class Referencerole(models.Model):
    pk_referencerole = models.AutoField(primary_key=True)
    referencerole = models.TextField(blank=True, null=True)
    oldnumber = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    role_order = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    role_original = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'referencerole'


class RelationshipBranch(models.Model):
    fk_relationshipnode = models.ForeignKey('RelationshipNode', models.DO_NOTHING, db_column='fk_relationshipnode', blank=True, null=True)
    fk_individual = models.ForeignKey(Individual, models.DO_NOTHING, db_column='fk_individual', blank=True, null=True)
    fk_relationshiprole = models.ForeignKey('RelationshipRole', models.DO_NOTHING, db_column='fk_relationshiprole', blank=True, null=True)
    pk_branch = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'relationship_branch'


class RelationshipEvent(models.Model):
    pk_relationship_event = models.AutoField(primary_key=True)
    fk_event = models.IntegerField(blank=True, null=True)
    fk_relationship_node = models.IntegerField(blank=True, null=True)
    relationship_event = models.TextField(blank=True, null=True)
    fk_branch = models.IntegerField(blank=True, null=True)
    fk_referenceindividual = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'relationship_event'


class RelationshipNode(models.Model):
    pk_relationship_node = models.AutoField(primary_key=True)
    fk_event = models.IntegerField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    entry = models.TextField(blank=True, null=True)
    fk_event_start = models.IntegerField(blank=True, null=True)
    fk_event_stop = models.IntegerField(blank=True, null=True)
    start_day = models.IntegerField(blank=True, null=True)
    fk_start_month = models.IntegerField(blank=True, null=True)
    start_year = models.IntegerField(blank=True, null=True)
    end_day = models.IntegerField(blank=True, null=True)
    fk_end_month = models.IntegerField(blank=True, null=True)
    end_year = models.IntegerField(blank=True, null=True)
    date_start = models.DateField(blank=True, null=True)
    date_end = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'relationship_node'


class RelationshipRole(models.Model):
    relationship_role = models.CharField(max_length=50, blank=True, null=True)
    role_original = models.TextField(blank=True, null=True)
    role_order = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    old_number = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    pk_role = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'relationship_role'


class Repository(models.Model):
    pk_repository = models.AutoField(primary_key=True)
    repository = models.TextField(blank=True, null=True)
    repository_fulltitle = models.TextField(blank=True, null=True)
    id_archoncode = models.IntegerField(blank=True, null=True)
    archoncode_text = models.TextField(blank=True, null=True)
    archoncode_machine = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'repository'


class Representation(models.Model):
    id_representation = models.AutoField(primary_key=True)
    pk_representation = models.IntegerField()
    fk_digisig = models.IntegerField(blank=True, null=True)
    fk_contributor = models.IntegerField(blank=True, null=True)
    representation_date = models.DateTimeField(blank=True, null=True)
    fk_access = models.IntegerField(blank=True, null=True)
    representation_filename = models.TextField(blank=True, null=True)
    fk_collection = models.IntegerField(blank=True, null=True)
    reference = models.TextField(blank=True, null=True)
    fk_contributor_creator = models.IntegerField(blank=True, null=True)
    represenation_datecreated = models.DateField(blank=True, null=True)
    fk_connection = models.IntegerField(blank=True, null=True)
    representation_thumbnail = models.TextField(blank=True, null=True)
    primacy = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    fk_representation_type = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    representation_folder = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'representation'


class RepresentationType(models.Model):
    pk_representation_type = models.AutoField(primary_key=True)
    representation_type = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'representation_type'


class Rti(models.Model):
    pk_rti = models.AutoField(primary_key=True)
    rti_folder = models.TextField(blank=True, null=True)
    rti_file = models.TextField(blank=True, null=True)
    fk_manifestation = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'rti'


class Seal(models.Model):
    pk_seal = models.IntegerField()
    fk_individual_realizer = models.IntegerField(blank=True, null=True)
    fk_certainty_realizer = models.IntegerField(blank=True, null=True)
    fk_class = models.IntegerField(blank=True, null=True)
    datestart_seal = models.IntegerField(blank=True, null=True)
    dateend_seal = models.IntegerField(blank=True, null=True)
    biface_seal = models.BooleanField(blank=True, null=True)
    fk_timegroupa = models.IntegerField(blank=True, null=True)
    fk_timegroupb = models.IntegerField(blank=True, null=True)
    datasetlondon = models.BooleanField(blank=True, null=True)
    datasetlondon_number = models.IntegerField(blank=True, null=True)
    datasetwales = models.BooleanField(blank=True, null=True)
    datasetwales_number = models.IntegerField(blank=True, null=True)
    datasetdl25 = models.BooleanField(blank=True, null=True)
    datasetdl25_number = models.IntegerField(blank=True, null=True)
    datasetdl25_individual = models.IntegerField(blank=True, null=True)
    datasetsussex = models.BooleanField(blank=True, null=True)
    fk_printgroup = models.IntegerField(blank=True, null=True)
    fk_individual_corporategroup = models.IntegerField(blank=True, null=True)
    fk_individual_office = models.IntegerField(blank=True, null=True)
    priority = models.IntegerField(blank=True, null=True)
    printobverse_classmark = models.TextField(blank=True, null=True)
    printobverse_size = models.TextField(blank=True, null=True)
    printreverse_classmark = models.TextField(blank=True, null=True)
    printreverse_size = models.TextField(blank=True, null=True)
    legend_obverse = models.TextField(blank=True, null=True)
    legend_reverse = models.TextField(blank=True, null=True)
    motif_obverse = models.TextField(blank=True, null=True)
    motif_reverse = models.TextField(blank=True, null=True)
    printrealizer = models.TextField(blank=True, null=True)
    printclass = models.TextField(blank=True, null=True)
    comment_catalogue = models.TextField(blank=True, null=True)
    printcatalogue = models.TextField(blank=True, null=True)
    birch = models.BooleanField(blank=True, null=True)
    birchentry = models.TextField(blank=True, null=True)
    walessortnumber = models.IntegerField(blank=True, null=True)
    id_seal = models.BigAutoField(primary_key=True)
    pas_temp = models.IntegerField(blank=True, null=True)
    whittick_temp = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    dataset_ellisp = models.IntegerField(blank=True, null=True)
    fk_sealrole = models.IntegerField(blank=True, null=True)
    dataset_durham = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    bm_temp = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    gem = models.BooleanField(blank=True, null=True)
    ancientgem = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'seal'


class Sealdescription(models.Model):
    pk_sealdescription = models.IntegerField()
    fk_collection = models.ForeignKey(Collection, models.DO_NOTHING, db_column='fk_collection', blank=True, null=True)
    sealdescription = models.TextField(blank=True, null=True)
    sealdescription_identifier = models.TextField(blank=True, null=True)
    fk_seal = models.IntegerField(blank=True, null=True)
    bifaceseal = models.BooleanField(blank=True, null=True)
    motif_obverse = models.TextField(blank=True, null=True)
    motif_reverse = models.TextField(blank=True, null=True)
    legend_obverse = models.TextField(blank=True, null=True)
    legend_reverse = models.TextField(blank=True, null=True)
    fk_approx_horizontal = models.IntegerField(blank=True, null=True)
    sealsize_horizontal = models.IntegerField(blank=True, null=True)
    fk_approx_vertical = models.IntegerField(blank=True, null=True)
    sealsize_vertical = models.IntegerField(blank=True, null=True)
    shape = models.TextField(blank=True, null=True)
    catalogue_pagenumber = models.TextField(blank=True, null=True)
    catalogue_filename = models.TextField(blank=True, null=True)
    catalogue_orderingnumber = models.IntegerField(blank=True, null=True)
    realizer = models.TextField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    fk_index = models.ForeignKey('TbIndex', models.DO_NOTHING, db_column='fk_index', blank=True, null=True)
    id_sealdescription = models.BigAutoField(primary_key=True)
    sealsize_horizontal_inch = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    sealsize_vertical_inch = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    fk_faction_horizontal_inch = models.IntegerField(blank=True, null=True)
    fk_fraction_vertical_inch = models.IntegerField(blank=True, null=True)
    catalogue_volume = models.TextField(blank=True, null=True)
    fk_contributor = models.IntegerField(blank=True, null=True)
    ui_catalogue = models.TextField(blank=True, null=True)
    fk_connection = models.IntegerField(blank=True, null=True)
    sealsize_inch_horiz_frac_p1 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    sealsize_inch_horiz_frac_p2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    sealsize_inch_vert_frac_p1 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    sealsize_inch_vert_frac_p2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sealdescription'


class Sealrole(models.Model):
    pk_sealrole = models.AutoField(primary_key=True)
    sealrole = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sealrole'


class Separator(models.Model):
    pk_separator = models.AutoField(primary_key=True)
    separator = models.TextField(blank=True, null=True)
    separator_alternate = models.TextField(blank=True, null=True)
    separator_comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'separator'


class Series(models.Model):
    pk_series = models.AutoField(primary_key=True)
    fk_repository = models.IntegerField(blank=True, null=True)
    series_name = models.TextField(blank=True, null=True)
    series_alias = models.TextField(blank=True, null=True)
    series_abbreviated = models.TextField(blank=True, null=True)
    series_photocode = models.TextField(blank=True, null=True)
    series_edition = models.TextField(blank=True, null=True)
    series_uri = models.TextField(blank=True, null=True)
    series_fulltitle = models.TextField(blank=True, null=True)
    series_description = models.TextField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    series_a1 = models.TextField(blank=True, null=True)
    series_n1 = models.IntegerField(blank=True, null=True)
    series_a2 = models.TextField(blank=True, null=True)
    series_n2 = models.IntegerField(blank=True, null=True)
    series_a3 = models.TextField(blank=True, null=True)
    series_n3 = models.IntegerField(blank=True, null=True)
    series_a4 = models.TextField(blank=True, null=True)
    series_n4 = models.IntegerField(blank=True, null=True)
    series_a5 = models.TextField(blank=True, null=True)
    series_n5 = models.IntegerField(blank=True, null=True)
    fk_separator_series = models.IntegerField(blank=True, null=True)
    fk_separator_a1 = models.IntegerField(blank=True, null=True)
    fk_separator_n1 = models.IntegerField(blank=True, null=True)
    fk_separator_a2 = models.IntegerField(blank=True, null=True)
    fk_separator_n2 = models.IntegerField(blank=True, null=True)
    fk_separator_a3 = models.IntegerField(blank=True, null=True)
    fk_separator_n3 = models.IntegerField(blank=True, null=True)
    identifier_a1 = models.BooleanField(blank=True, null=True)
    identifier_n1 = models.BooleanField(blank=True, null=True)
    identifier_a2 = models.BooleanField(blank=True, null=True)
    identifier_n2 = models.BooleanField(blank=True, null=True)
    identifier_a3 = models.BooleanField(blank=True, null=True)
    identifier_n3 = models.BooleanField(blank=True, null=True)
    fk_separator_event_a1 = models.IntegerField(blank=True, null=True)
    fk_separator_event_n1 = models.IntegerField(blank=True, null=True)
    fk_separator_event_a2 = models.IntegerField(blank=True, null=True)
    fk_separator_event_n2 = models.IntegerField(blank=True, null=True)
    fk_separator_prefix_a1 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    fk_separator_prefix_n1 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    fk_separator_prefix_a2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    fk_separator_prefix_n2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    fk_connection = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    fk_separator_prefix_a3 = models.TextField(blank=True, null=True)
    fk_separator_prefix_n3 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    fk_separator_n1_variant = models.IntegerField(blank=True, null=True)
    fk_separator_series_v = models.IntegerField(blank=True, null=True)
    move = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'series'


class Setting(models.Model):
    pk_setting = models.IntegerField(blank=True, null=True)
    fk_engraving = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'setting'


class Shape(models.Model):
    pk_shape = models.AutoField(primary_key=True)
    shape = models.TextField(blank=True, null=True)
    shape_dl25 = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shape'


class Support(models.Model):
    pk_support = models.IntegerField()
    fk_item = models.ForeignKey(Item, models.DO_NOTHING, db_column='fk_item', blank=True, null=True)
    fk_part = models.ForeignKey(Part, models.DO_NOTHING, db_column='fk_part', blank=True, null=True)
    fk_colour = models.IntegerField(blank=True, null=True)
    fk_attachment = models.IntegerField(blank=True, null=True)
    fk_colourstain = models.IntegerField(blank=True, null=True)
    fk_material = models.IntegerField(blank=True, null=True)
    fk_number_originalposition = models.IntegerField(blank=True, null=True)
    fk_number_currentposition = models.IntegerField(blank=True, null=True)
    support_biface = models.BooleanField(blank=True, null=True)
    support_comment = models.TextField(blank=True, null=True)
    fk_nature = models.IntegerField(blank=True, null=True)
    temp_durham_support_pk = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_support = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'support'


class Tax(models.Model):
    pk_tax = models.AutoField(primary_key=True)
    tax = models.TextField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tax'


class Taxlist(models.Model):
    fk_referenceindividual = models.ForeignKey(Referenceindividual, models.DO_NOTHING, db_column='fk_referenceindividual', blank=True, null=True)
    amountpounds = models.IntegerField(blank=True, null=True)
    amountmark = models.DecimalField(max_digits=18, decimal_places=5, blank=True, null=True)
    amountshilling = models.IntegerField(blank=True, null=True)
    amountpence = models.IntegerField(blank=True, null=True)
    amountob = models.IntegerField(blank=True, null=True)
    amounttotal = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    positioninlist = models.IntegerField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    fk_tax = models.ForeignKey(Tax, models.DO_NOTHING, db_column='fk_tax', blank=True, null=True)
    amountq = models.IntegerField(blank=True, null=True)
    pk_taxlist = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'taxlist'


class TbIndex(models.Model):
    pk_index = models.AutoField(primary_key=True)
    a_index = models.TextField(blank=True, null=True)
    index_order = models.IntegerField(blank=True, null=True)
    fk_repository = models.IntegerField(blank=True, null=True)
    index_url = models.TextField(blank=True, null=True)
    fk_catalogue = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_index'


class TempAllsealV2(models.Model):
    pk_seal = models.IntegerField(blank=True, null=True)
    datasetlondon_number = models.IntegerField(blank=True, null=True)
    fk_faceterm = models.IntegerField(blank=True, null=True)
    pk_location = models.IntegerField(blank=True, null=True)
    fk_englandwales_parish = models.IntegerField(blank=True, null=True)
    pk_counties_uk = models.IntegerField(blank=True, null=True)
    pk_allseals = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'temp_allseal_v2'


class TempEvent(models.Model):
    pk_event = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'temp_event'


class TempEventOut(models.Model):
    pk_item = models.IntegerField(blank=True, null=True)
    ui_item_repository = models.CharField(max_length=50, blank=True, null=True)
    description1 = models.TextField(blank=True, null=True)
    start_date = models.CharField(max_length=255, blank=True, null=True)
    end_date = models.CharField(max_length=255, blank=True, null=True)
    fk_item = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'temp_event_out'


class TempLondonseal(models.Model):
    pk_seal = models.IntegerField(blank=True, null=True)
    datasetlondon_number = models.IntegerField(blank=True, null=True)
    fk_faceterm = models.IntegerField(blank=True, null=True)
    pk_location = models.IntegerField(blank=True, null=True)
    fk_englandwales_parish = models.IntegerField(blank=True, null=True)
    pk_temp_londonseal = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'temp_londonseal'


class TempTnain(models.Model):
    description1 = models.TextField(blank=True, null=True)
    id_2 = models.CharField(max_length=255, blank=True, null=True)
    fk_series = models.IntegerField(blank=True, null=True)
    number1 = models.IntegerField(blank=True, null=True)
    number2 = models.IntegerField(blank=True, null=True)
    number3 = models.IntegerField(blank=True, null=True)
    letter1 = models.CharField(max_length=255, blank=True, null=True)
    letter2 = models.CharField(max_length=255, blank=True, null=True)
    letter3 = models.CharField(max_length=255, blank=True, null=True)
    startday = models.IntegerField(blank=True, null=True)
    startmonth = models.IntegerField(blank=True, null=True)
    startyear = models.IntegerField(blank=True, null=True)
    endday = models.IntegerField(blank=True, null=True)
    endmonth = models.IntegerField(blank=True, null=True)
    endyear = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'temp_tnain'


class TimegroupA(models.Model):
    pk_timegroup_a = models.AutoField(primary_key=True)
    timegroup_a = models.IntegerField(blank=True, null=True)
    timegroup_a_range = models.TextField(blank=True, null=True)
    timegroup_a_finaldate = models.IntegerField(blank=True, null=True)
    timegroup_a_startdate = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'timegroup_a'


class TimegroupB(models.Model):
    pk_timegroup_b = models.AutoField(primary_key=True)
    timegroup_b = models.IntegerField(blank=True, null=True)
    timegroup_b_range = models.TextField(blank=True, null=True)
    timegroup_a_finaldate = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'timegroup_b'


class Tna(models.Model):
    pk_tna = models.AutoField(primary_key=True)
    citable_reference = models.TextField(blank=True, null=True)
    context_description = models.TextField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    start_date = models.TextField(blank=True, null=True)
    start_date_num = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    end_date = models.TextField(blank=True, null=True)
    end_date_num = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    covering_dates = models.TextField(blank=True, null=True)
    held_by = models.TextField(blank=True, null=True)
    catalogue_level = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    references = models.TextField(blank=True, null=True)
    opening_date = models.TextField(blank=True, null=True)
    closure_status = models.TextField(blank=True, null=True)
    closure_type = models.TextField(blank=True, null=True)
    closure_code = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    subjects = models.TextField(blank=True, null=True)
    id = models.TextField(blank=True, null=True)
    fk_number = models.IntegerField(blank=True, null=True)
    fk_series = models.IntegerField(blank=True, null=True)
    fk_item = models.IntegerField(blank=True, null=True)
    classmark_alpha1 = models.TextField(blank=True, null=True)
    classmark_number1 = models.IntegerField(blank=True, null=True)
    classmark_alpha2 = models.TextField(blank=True, null=True)
    classmark_number2 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tna'


class TnaAncientdeeds(models.Model):
    id_tna_ancientdeeds = models.IntegerField(blank=True, null=True)
    docreference = models.CharField(max_length=255, blank=True, null=True)
    catdocref = models.CharField(max_length=255, blank=True, null=True)
    contextdescription = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    startdate = models.CharField(max_length=255, blank=True, null=True)
    numstartdate = models.FloatField(blank=True, null=True)
    enddate = models.CharField(max_length=255, blank=True, null=True)
    numendate = models.FloatField(blank=True, null=True)
    coveringdates = models.CharField(max_length=255, blank=True, null=True)
    sourcelevel = models.FloatField(blank=True, null=True)
    formerrefdep = models.CharField(max_length=255, blank=True, null=True)
    openingdate = models.CharField(max_length=255, blank=True, null=True)
    closurestatus = models.CharField(max_length=255, blank=True, null=True)
    closuretype = models.CharField(max_length=255, blank=True, null=True)
    closurecode = models.FloatField(blank=True, null=True)
    taxonomy = models.CharField(max_length=255, blank=True, null=True)
    fk_series = models.SmallIntegerField(blank=True, null=True)
    number1 = models.SmallIntegerField(blank=True, null=True)
    number2 = models.SmallIntegerField(blank=True, null=True)
    tempphrase = models.CharField(max_length=255, blank=True, null=True)
    letter1 = models.CharField(max_length=255, blank=True, null=True)
    letter2 = models.CharField(max_length=255, blank=True, null=True)
    presence = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tna_ancientdeeds'


class TnaAncientdeedsRevisedcolumnnames(models.Model):
    fk_repository = models.IntegerField(blank=True, null=True)
    fk_series = models.SmallIntegerField(blank=True, null=True)
    classmark_alpha1 = models.CharField(max_length=255, blank=True, null=True)
    classmark_number1 = models.SmallIntegerField(blank=True, null=True)
    classmark_alpha2 = models.CharField(max_length=255, blank=True, null=True)
    classmark_number2 = models.SmallIntegerField(blank=True, null=True)
    catalogue = models.CharField(max_length=255, blank=True, null=True)
    tempphrase = models.CharField(max_length=255, blank=True, null=True)
    repository_id = models.CharField(max_length=255, blank=True, null=True)
    shelfmark = models.CharField(max_length=255, blank=True, null=True)
    field_id = models.IntegerField(db_column='_id', blank=True, null=True)  # Field renamed because it started with '_'.
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    startdate = models.CharField(max_length=255, blank=True, null=True)
    numstartdate = models.FloatField(blank=True, null=True)
    enddate = models.CharField(max_length=255, blank=True, null=True)
    numendate = models.FloatField(blank=True, null=True)
    coveringdates = models.CharField(max_length=255, blank=True, null=True)
    sourcelevel = models.FloatField(blank=True, null=True)
    formerrefdep = models.CharField(max_length=255, blank=True, null=True)
    openingdate = models.CharField(max_length=255, blank=True, null=True)
    closurestatus = models.CharField(max_length=255, blank=True, null=True)
    closuretype = models.CharField(max_length=255, blank=True, null=True)
    closurecode = models.FloatField(blank=True, null=True)
    taxonomy = models.CharField(max_length=255, blank=True, null=True)
    presence = models.IntegerField(blank=True, null=True)
    id2 = models.IntegerField(blank=True, null=True)
    year_start = models.IntegerField(blank=True, null=True)
    fk_month_start = models.IntegerField(blank=True, null=True)
    day_start = models.IntegerField(blank=True, null=True)
    year_end = models.IntegerField(blank=True, null=True)
    fk_month_end = models.IntegerField(blank=True, null=True)
    day_end = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tna_ancientdeeds_revisedcolumnnames'


class Uniqueidentificationnumbers(models.Model):
    pk_uinumbers = models.AutoField(primary_key=True)
    uinumbers_type = models.TextField(blank=True, null=True)
    uinumbers_number = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'uniqueidentificationnumbers'


class UserDigisig(models.Model):
    pk_user = models.AutoField(primary_key=True)
    username = models.TextField(blank=True, null=True)
    user_email = models.TextField(blank=True, null=True)
    user_affiliation = models.TextField(blank=True, null=True)
    password = models.TextField(blank=True, null=True)
    fk_access = models.IntegerField(blank=True, null=True)
    fk_repository = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_digisig'


class Digisigitemview(models.Model):
    id_item = models.AutoField(primary_key=True)
    shelfmark = models.TextField(blank=True, null=True)
    ui_item_repository = models.TextField(blank=True, null=True)
    repository_fulltitle = models.TextField(blank=True, null=True)
    series_shortname = models.TextField(blank=True, null=True)
    series_fulltitle = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'digisig_item_view'

class DigisigManifestationview(models.Model):
    id_manifestation = models.AutoField(primary_key=True)
    representation_filename = models.TextField(blank=True, null=True)
    fk_representation_type = models.IntegerField(blank=True, null=True)
    shape = models.TextField(blank=True, null=True)
    faceterm = models.TextField(blank=True, null=True)
    fk_seal = models.IntegerField(blank=True, null=True) 
    fk_class = models.IntegerField(blank=True, null=True)
    fk_shape = models.IntegerField(blank=True, null=True)
    class_name = models.TextField(blank=True, null=True)
    fk_part = models.IntegerField(blank=True, null=True)
    fk_item = models.IntegerField(blank=True, null=True)
    fk_support = models.IntegerField(blank=True, null=True)
    fk_nature = models.IntegerField(blank=True, null=True)
    attachment = models.TextField(blank=True, null=True)
    fk_number_currentposition = models.IntegerField(blank=True, null=True)
    number = models.TextField(blank=True, null=True) 
    nature_name = models.TextField(blank=True, null=True)
    shelfmark = models.TextField(blank=True, null=True)
    fk_repository = models.IntegerField(blank=True, null=True)
    fk_series = models.IntegerField(blank=True, null=True)
    repository = models.TextField(blank=True, null=True)
    series_name = models.TextField(blank=True, null=True)
    repository_startdate = models.DateField(blank=True, null=True)
    repository_enddate = models.DateField(blank=True, null=True)
    repository_location = models.TextField(blank=True, null=True)
    defname = models.CharField(max_length=255, blank=True, null=True)
    latdeg = models.IntegerField(blank=True, null=True)
    latmin = models.FloatField(blank=True, null=True)
    longdeg = models.IntegerField(blank=True, null=True)
    longmin = models.FloatField(blank=True, null=True)
    northing = models.IntegerField(blank=True, null=True)
    easting = models.IntegerField(blank=True, null=True)
    fk_counties_uk = models.IntegerField(blank=True, null=True)
    location_county = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'digisig_manifestation_view'

class Digisigseriesview(models.Model):
    pk_series = models.AutoField(primary_key=True)
    series_name = models.TextField(blank=True, null=True)
    fk_repository = models.IntegerField(blank=True, null=True)
    repository_fulltitle = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'digisig_series_view'

#View is based on digisigseriesview -- to ensure that repositories listed include only ones represented in seriesview
class Digisigrepositoriesview(models.Model):
    fk_repository = models.IntegerField(primary_key=True)
    repository_fulltitle = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'digisig_repository_view'

class Digisigsealdescriptionview(models.Model):
    id_sealdescription = models.AutoField(primary_key=True)
    fk_seal = models.IntegerField(blank=True, null=True)
    fk_collection = models.IntegerField(blank=True, null=True)
    sealdescription = models.TextField(blank=True, null=True)
    sealdescription_identifier = models.TextField(blank=True, null=True)
    catalogue_pagenumber = models.TextField(blank=True, null=True)
    catalogue_orderingnumber = models.IntegerField(blank=True, null=True)
    realizer = models.TextField(blank=True, null=True)
    fk_contributor = models.IntegerField(blank=True, null=True)
    id_representation = models.IntegerField(blank=True, null=True)
    representation_filename = models.TextField(blank=True, null=True)
    fk_access = models.IntegerField(blank=True, null=True)
    fk_connection = models.IntegerField(blank=True, null=True)
    collection_shorttitle = models.TextField(blank=True, null=True)
    collection_fulltitle = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'digisig_sealdescription_view'