from modeltranslation.translator import translator, TranslationOptions
from company.contrib.pos.models import PointOfService


class PointOfServiceTrans(TranslationOptions):
    fields = ('name',)
translator.register(PointOfService, PointOfServiceTrans)
