from modeltranslation.translator import translator, TranslationOptions
from company.models import Company
from company.contrib.staff.models import Employee


class EmployeeTrans(TranslationOptions):
    fields = ('title', 'bio')
translator.register(Employee, EmployeeTrans)
