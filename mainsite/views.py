from multiprocessing import context
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.mail import EmailMessage
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import FileResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, ListView, FormView, DetailView

from .forms import DoacaoAlimentoForm, IntercambioForm
from .models import *


class IndexView(TemplateView):
    template_name = 'mainsite/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['bannermain'] = Post.objects.filter(place="bannermain").order_by('created_at').first()
        context['infosuperior'] = Post.objects.filter(place="infosuperior").first()
        context['animals'] = Animal.objects.all()
        context['aboutproject'] = Post.objects.filter(place="aboutproject").first()
        context['testimonials'] = Post.objects.filter(place="testimonials")
        context['livezoo'] = Post.objects.filter(place="livezoo").first()
        context['zooarea'] = Post.objects.filter(place="zooarea").first()
        context['zoospecies'] = Post.objects.filter(place="zoospecies").first()
        return context


class InstitutionalPage(DetailView):
    template_name = 'mainsite/components/institutional_page.html'
    model = Post
    context_object_name = "institutional_page"
    slug_field = 'slug'


class DonationsView(TemplateView):
    template_name = "mainsite/donations/donations.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['donations'] = Post.objects.filter(place="donations").order_by('created_at').last()
        context['food_donation'] = Post.objects.filter(place="food_donation").order_by('created_at').last()
        context['adoption'] = Post.objects.filter(place="adopt").order_by('created_at').last()
        return context  


class DonationView(TemplateView):
    template_name = "mainsite/donations/donation.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['donations'] = Post.objects.filter(place="donations").order_by('created_at').last()
        return context

 
class FoodDonationView(FormView):
    template_name = "mainsite/donations/food_donation.html"
    form_class = DoacaoAlimentoForm
    success_url = reverse_lazy('mainsite:food_donation')
    
    def form_valid(self, form):
        
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        phone = form.cleaned_data['phone']
                
        email_to_zoo = EmailMessage(
            "Solicitação de Contato para Doação de Alimento",
            f"{name} está solicitando contato para acertar uma doação de alimentos!\n\nInformações de contato:\nE-mail: {email}\nTelefone:{phone}\n\nEntre em contato para acertar os detalhes!",
            settings.EMAIL_HOST_USER,
            ['zoounama.adm@gmail.com']
        )
        
        email_to_zoo.send()
        
        messages.success(self.request, 'Sua solicitação de contato foi recebida! Aguarde o retorno.')
        
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, 'Ocorreu um erro ao enviar sua solicitação, tente novamente!.')
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['food_donation'] = Post.objects.filter(place="food_donation").order_by('created_at').last()
        return context
                        

class AdoptView(ListView):
    template_name = "mainsite/donations/adopt.html"
    model = Animal
    context_object_name = 'animals'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['adoption'] = Post.objects.filter(place="adopt").order_by('created_at').last()
        return context    


class AdminDocs(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    template_name = 'mainsite/admin_docs.html'

    def test_func(self):
        return self.request.user.is_staff


class ExchangeView(ListView):
    template_name = "mainsite/exchange.html"
    model = Notice
    context_object_name = 'notices'
    ordering = ['-year', '-semester']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['exchange'] = Post.objects.filter(place="exchange").order_by('created_at').last()
        return context    

class DownloadFileView(View):
    def get(self, request, pk):
        notice = get_object_or_404(Notice, pk=pk)
        file_path = notice.file.path
        response = FileResponse(open(file_path, 'rb'), content_type='application/octet-stream')
        response['Content-Disposition'] = f'attachment; filename="{notice.file.name}"'
        return response


class ExchangeRegistrationView(FormView):
    template_name = "mainsite/exchange_registration.html"
    form_class = IntercambioForm
    success_url = reverse_lazy('mainsite:exchange_registration')
    
    def form_valid(self, form):
        
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        phone = form.cleaned_data['phone']
                
        email_to_zoo = EmailMessage(
            "Inscrição para Intercâmbio",
            f"{name} está se inscrevendo para o intercâmbio\n\nInformações de contato:\nE-mail: {email}\nTelefone:{phone}",
            settings.EMAIL_HOST_USER,
            ['zoounama.adm@gmail.com']
        )
        
        email_to_zoo.send()
        
        messages.success(self.request, 'Sua inscrição foi recebida! Aguarde o retorno.')
        
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, 'Ocorreu um erro ao enviar sua inscrição, tente novamente!')
        return super().form_invalid(form)    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        notice= Notice.objects.last() 
        context['notice'] = notice
        context['exchange_registration'] = Post.objects.filter(place="exchange_reg").order_by('created_at').last()
        return context


class RelatedWorkView(ListView):
    template_name = "mainsite/related_work.html"
    context_object_name = 'related_works'

    def get_queryset(self):
        return Post.objects.filter(place="related_work").order_by('-created_at')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        related_work_list = context[self.context_object_name]
        paginator = Paginator(related_work_list, 5)

        page = self.request.GET.get('page')
        try:
            related_work = paginator.page(page)
        except PageNotAnInteger:
            related_work = paginator.page(1)
        except EmptyPage:
            related_work = paginator.page(paginator.num_pages)

        context[self.context_object_name] = related_work
        return context
    
class AnimalDetailView(DetailView):
    template_name = "mainsite/animal_detail.html"
    model = Animal
    context_object_name = "animal"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context