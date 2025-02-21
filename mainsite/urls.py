from django.urls import path
from .views import *

app_name = 'mainsite'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('institucional/<slug:slug>/', InstitutionalPage.as_view(), name='institutional'),
    path('intercambio/', ExchangeView.as_view(), name='exchange'),
    path('intercambio/inscricao', ExchangeRegistrationView.as_view(), name='exchange_registration'),
    path('download/<int:pk>/', DownloadFileView.as_view(), name='download_file'),
    path('trabalhos/', RelatedWorkView.as_view(), name='related_work'),
    path('doacoes/', DonationsView.as_view(), name='donations'),
    path('doacoes/doacao', DonationView.as_view(), name='donation'),
    path('doacoes/doar-alimento',FoodDonationView.as_view(), name='food_donation'),
    path('doacoes/adote', AdoptView.as_view(), name='adopt'),
    path("admin/docs/", AdminDocs.as_view(), name="admin-docs"),
    path('animal/<int:pk>/', AnimalDetailView.as_view(), name='animal_detail'),
]