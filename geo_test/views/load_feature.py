from django.contrib.gis.geos import GEOSGeometry
from django.views.generic import FormView
from osgeo import ogr, gdal

from geo_test.forms.load_feature import LoadWFSDetailsForm
from geo_test.models import Quiz, WFSFeature, Question

gdal.SetConfigOption('OGR_WFS_LOAD_MULTIPLE_LAYER_DEFN', 'NO')
gdal.SetConfigOption('OGR_WFS_PAGING_ALLOWED', 'YES')
gdal.SetConfigOption('OGR_WFS_PAGE_SIZE', '10000')


class LoadFeatureWFS(FormView):
    template_name = 'load_feature.html'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.driver = ogr.GetDriverByName('WFS')

    def get_form(self, form_class=None):
        params = self.request.GET

        wfs = self.driver.Open('WFS:' + params['url'] + '')
        layer = wfs.GetLayerByIndex(int(params['layer_id']))

        form_kwargs = self.get_form_kwargs()
        form_kwargs['initial']['geometry_source'] = layer.GetGeometryColumn()

        column_names = [
            layer.GetLayerDefn().GetFieldDefn(field_count).GetNameRef()
            for field_count in range(layer.GetLayerDefn().GetFieldCount())
        ]

        form = LoadWFSDetailsForm(column_names, **form_kwargs)
        return form

    def form_valid(self, form):
        params = self.request.GET

        wfs = self.driver.Open('WFS:' + params['url'])
        layer = wfs.GetLayerByIndex(int(params['layer_id']))

        wfs_feature = WFSFeature.objects.create(
            url=params['url'],
            name_source=form.data['question_source'],
            geo_source=form.data['geometry_source']
        )
        quiz = Quiz.objects.create(
            name=layer.GetName(),
            description='empty_description',
            data_source=wfs_feature
        )

        for feature in layer:
            wkt_geom = feature.GetGeometryRef().ExportToWkt()
            spatial = feature.GetGeometryRef().GetSpatialReference()
            wkt_geom = wkt_geom.replace('MULTISURFACE', 'MULTIPOLYGON')
            Question.objects.create(
                name=feature.GetFieldAsString(wfs_feature.name_source),
                geo=GEOSGeometry(wkt_geom, srid=2180),
                description='test',
                quiz=quiz,
            )

        return self.render_to_response(
            self.get_context_data(
                form=form
            )
        )
