from django.views.generic import FormView
from osgeo import ogr

from geo_test.forms.load_wfs import LoadWFSForm, WFSFeatureFormSet


class LoadWFSView(FormView):
    form_class = LoadWFSForm
    template_name = 'load_wfs.html'

    def form_valid(self, form):
        driver = ogr.GetDriverByName('WFS')
        wfs = driver.Open('WFS:' + form.data['url'])
        initial_data = []
        for layer_id in range(wfs.GetLayerCount()):
            layer = wfs.GetLayerByIndex(layer_id)
            initial_data.append(
                {
                    'id': layer_id,
                    'name': layer.GetName(),
                    'feature_count': layer.GetFeatureCount(),
                }
            )

        form = WFSFeatureFormSet(initial=initial_data)

        return self.render_to_response(
            self.get_context_data(wfs_forms=form)
        )
