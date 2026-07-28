from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import DemandeDevisForm


def home(request):
    return render(request, 'home.html')


def service_solaire(request):
    return render(request, 'service_solaire.html')


def service_videosurveillance(request):
    return render(request, 'service_videosurveillance.html')


def service_controle_acces(request):
    return render(request, 'service_controle_acces.html')


def service_electricite(request):
    return render(request, 'service_electricite.html')


def service_reseau(request):
    return render(request, 'service_reseau.html')


def service_telephonie(request):
    return render(request, 'service_telephonie.html')


def service_incendie(request):
    return render(request, 'service_incendie.html')


def service_cloture(request):
    return render(request, 'service_cloture.html')


def service_maintenance(request):
    return render(request, 'service_maintenance.html')


def connexion(request):
    return render(request, 'connexion.html')


def demande_devis(request):
    if request.method == 'POST':
        form = DemandeDevisForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Votre demande de devis a été envoyée avec succès ! "
                "Notre équipe vous contactera dans les plus brefs délais."
            )
            return redirect('demande_devis')
        else:
            messages.error(
                request,
                "Une erreur est survenue dans le formulaire. "
                "Veuillez vérifier les champs et réessayer."
            )
    else:
        form = DemandeDevisForm()

    return render(request, 'demande_devis.html', {'form': form})


def contact(request):
    return render(request, 'contact.html')

def connexion(request):
    return render(request, "connexion.html")    

def apropos(request):
    return render(request, "apropos.html")    
    
