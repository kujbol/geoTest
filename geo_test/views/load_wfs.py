from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.views.generic import FormView
from osgeo import ogr

from geo_test.forms.load_wfs import LoadWFSForm, WFSFeatureFormSet


@method_decorator(staff_member_required, 'get')
@method_decorator(staff_member_required, 'post')
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
