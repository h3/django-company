from modeltranslation.translator import translator, TranslationOptions
from company.contrib.testimonials.models import Testimonial


class TestimonialTrans(TranslationOptions):
    fields = ('title', 'text')
translator.register(Testimonial, TestimonialTrans)
