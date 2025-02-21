from .models import *
from modeltranslation.translator import TranslationOptions, register

@register(Animal)
class AnimalTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(Post)
class PostTranslationOptions(TranslationOptions):
    fields = ('title', 'subtitle', 'description')

@register(Notice)
class NoticeTranslationOptions(TranslationOptions):
    fields = ('title', 'description')