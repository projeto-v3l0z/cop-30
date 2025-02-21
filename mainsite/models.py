import datetime
import os

from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.dispatch import receiver
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

class Animal(models.Model):

    TIPOS_ANIMAL = (
        (_('Anfíbio'), _('Anfíbio')),
        (_('Ave'), _('Ave')),
        (_('Mamífero'), _('Mamífero')),
        (_('Peixe'), _('Peixe')),
        (_('Réptil'), _('Réptil'))
    )

    DIETA = (
        (_('Carnívoro'), _('Carnívoro')),
        (_('Carnívoro'), _('Carnívoro')),
        (_('Detritívoro'), _('Detritívoro')),
        (_('Frugívoro'), _('Frugívoro')),
        (_('Herbívoro'), _('Herbívoro')),
        (_('Insetívoro'), _('Insetívoro')),
        (_('Invertívoro'), _('Invertívoro')),
        (_('Onívoro'), _('Onívoro')),
        (_('Perifitívoro'), _('Perifitívoro')),
        (_('Frugívoro'), _('Frugívoro')),
        (_('Herbívoro'), _('Herbívoro')),
        (_('Insetívoro'), _('Insetívoro')),
        (_('Invertívoro'), _('Invertívoro')),
        (_('Onívoro'), _('Onívoro')),
        (_('Perifitívoro'), _('Perifitívoro')),
    )

    STATUS = (
        (_('Sem riscos'), _('Sem riscos')),
        (_('Vulnerável'), _('Vulnerável')),
        (_('Pouco preocupante'), _('Pouco preocupante')),
    )

    MEDIDAPESO = (
        ('kg', 'kg'),
        ('g', 'g'),
    )

    name = models.CharField(_('Nome'), max_length=60)
    scientific_name = models.CharField(_('Nome científico'), max_length=70)
    type = models.CharField(
        _('Tipo'),
        max_length=20,
        choices=TIPOS_ANIMAL,
        default='mamífero',
    )
    lifetime = models.PositiveSmallIntegerField(_('Tempo de vida'), default=0)
    diet = models.CharField(
        _('Dieta'),
        max_length=20,
        choices=DIETA,
        default='herbivoro'
    )
    weight = models.FloatField(_('Peso'), default=0)
    weight_measure = models.CharField(
        _('Unidade de Medida do Peso'),
        max_length=2,
        choices=MEDIDAPESO,
        default='kg',
    )
    status = models.CharField(
        _('Status de Risco'),
        max_length=20,
        choices=STATUS,
        default='semriscos',
    )
    description = models.TextField(_('Descrição'), max_length=3000, null=True, blank=True)
    adoption_link = models.URLField(_('Link para apoio'), default='http://pag.ae/7ZyUJfPM3')
    main_image = models.ImageField(_('Imagem Principal'), upload_to='animais')
    secondary_image = models.ImageField(_('Imagem Secundária'), upload_to='animais')
    video = models.CharField(_('Vídeo'), max_length=200, default='videos/zoo-unama.mp4')
    # Logs
    created_by = models.ForeignKey('auth.User', verbose_name=_('Criado por'), on_delete=models.CASCADE, related_name='animal_created_by', null=True, editable=False)
    created_at = models.DateTimeField(_('Criado em'), auto_now_add=True, null=True, editable=False)
    updated_by = models.ForeignKey('auth.User', verbose_name=_('Atualizado por'), on_delete=models.CASCADE, related_name='animal_updated_by', null=True, editable=False)
    updated_at = models.DateTimeField(_('Atualizado em'), auto_now=True, null=True, editable=False)

    class Meta:
        verbose_name = _("Animal")
        verbose_name_plural = _("Animais")

    def __str__(self):
        return self.name


@receiver(models.signals.pre_delete, sender=Animal)
def auto_delete_Animais_on_delete(sender, instance, **kwargs):
    if instance.main_image:
        if os.path.isfile(instance.main_image.path):
            os.remove(instance.main_image.path)
    if instance.secondary_image:
        if os.path.isfile(instance.secondary_image.path):
            os.remove(instance.secondary_image.path)


class Post(models.Model):
    LOCAL_POST = [
        ('bannermain', _('Banner Principal')),
        ('infosuperior', _('Informações da Indigenazinha')),
        ('aboutproject', _('Sobre o Projeto')),
        ('zooarea', _('Área do Zoológico')),
        ('zoospecies', _('Espécies do Zoológico')),
        ('livezoo', _('Live Zoo')),
        ('testimonials', _('Depoimentos')),
        ('related_work', _('Trabalhos Relacionados')),
        ('donations', _('Doações')),
        ('food_donation', _('Doação de Alimentos')),
        ('adopt', _('Adote')),
        ('exchange', _('Intercâmbio')),
        ('exchange_reg', _('Inscrição de Intercâmbio')),
        ('institutional_pages', _('Páginas Institucionais'))
    ]
    
    title = models.CharField(_('Título'), max_length=100)
    description = models.TextField(_('Descrição'), max_length=2000)
    place = models.CharField(
        _('Onde isso vai aparecer?'),
        max_length=20,
        choices=LOCAL_POST,
        default='testimonials'
    )
    link = models.URLField(_('Link'), blank=True, null=True)
    # Video
    video = models.FileField(_('Vídeo'), upload_to='postagem', blank=True, null=True)
    # Sub-Info
    title = models.CharField(_('Título'), max_length=100)
    subtitle = models.CharField(_('Subtítulo'), max_length=100, blank=True)
    # Logs
    created_by = models.ForeignKey(User, verbose_name=_('Criado por'), on_delete=models.CASCADE, related_name='post_created_by', null=True, editable=False)
    created_at = models.DateTimeField(_('Criado em'), auto_now_add=True, null=True, editable=False)
    updated_by = models.ForeignKey(User, verbose_name=_('Atualizado por'), on_delete=models.CASCADE, related_name='post_updated_by', null=True, editable=False)
    updated_at = models.DateTimeField(_('Atualizado em'), auto_now=True, null=True, editable=False)
    # Slug
    slug = models.SlugField(_('Slug'), max_length=100, blank=True, null=True, editable=False)

    def save(self, *args, **kwargs):
        if self.subtitle:
            slug = slugify(self.subtitle)
            if Post.objects.filter(slug=slug).exists():
                slug += f"-{Post.objects.count() + 1}"
            self.slug = slug
        super(Post, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _("Postagem")
        verbose_name_plural = _("Postagens")

    def __str__(self):
        return self.title


class PostImage(models.Model):
    post = models.ForeignKey(Post, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(_('Imagem'), upload_to='postagem')
    
    class Meta:
        verbose_name = _("Imagem do Post")
        verbose_name_plural = _("Imagens do Post")

    def __str__(self):
        return self.post.title + " - " + _("Imagem")

    def save(self, *args, **kwargs):
        if self.post.place == 'testimonials' and self.post.images.exists():
            raise ValidationError(_('Postagens do tipo "Depoimento" só podem ter uma imagem.'))
        super().save(*args, **kwargs)


@receiver(models.signals.pre_delete, sender=PostImage)
def auto_delete_PostImage_on_delete(sender, instance, **kwargs):
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)


def validate_svg_file(value):
    if not value.name.endswith('.svg'):
        raise ValidationError(
            _('O arquivo deve ser ".svg". Ache bons ícones em <https://icons.getbootstrap.com>.'))


class Notice(models.Model):
    semesters = (
        ('1', '1°'),
        ('2', '2°'),
    )
    title = models.CharField(_('Título'), max_length=100)
    description = models.TextField(_('Descrição'), max_length=500, blank=True, null=True)
    year = models.PositiveSmallIntegerField(_('Ano'), default=datetime.date.today().year, validators=[MinValueValidator(2024), MaxValueValidator(2099)])    
    semester = models.CharField(
            _('Semestre'),
            max_length=1,
            choices=semesters,
            default='1',
        )
    file = models.FileField(_('Arquivo'), upload_to='editais')
    # Logs
    created_by = models.ForeignKey('auth.User', verbose_name=_('Criado por'), on_delete=models.CASCADE, related_name='notice_created_by', null=True, editable=False)
    created_at = models.DateTimeField(_('Criado em'), auto_now_add=True, null=True, editable=False)
    updated_by = models.ForeignKey('auth.User', verbose_name=_('Atualizado por'), on_delete=models.CASCADE, related_name='notice_updated_by', null=True, editable=False)
    updated_at = models.DateTimeField(_('Atualizado em'), auto_now=True, null=True, editable=False)

    class Meta:
        verbose_name = _("Edital")
        verbose_name_plural = _("Editais")

    def __str__(self):
        return self.title
