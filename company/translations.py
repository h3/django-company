from modeltranslation.translator import translator, TranslationOptions
from company.models import Company


class CompanyTrans(TranslationOptions):
    fields = ('name', 'slogan')
translator.register(Company, CompanyTrans)
