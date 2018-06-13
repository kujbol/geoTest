from django.contrib import admin

# Register your models here.
from geo_test.models import Question, Quiz, QuizResult, WFSFeature


class QuestionAdmin(admin.ModelAdmin):
    pass


class WFSAdmin(admin.ModelAdmin):

    class Media:
        js = ("js/ol.js", "js/wfs_loader.js", )


admin.site.register(Question, admin_class=QuestionAdmin)
admin.site.register(Quiz)
admin.site.register(WFSFeature, admin_class=WFSAdmin)
admin.site.register(QuizResult)
