from django import forms
from .models import DemandeDevis


class DemandeDevisForm(forms.ModelForm):
    class Meta:
        model = DemandeDevis
        fields = [
            'nom', 'entreprise', 'telephone', 'email', 'ville',
            'service_souhaite', 'description', 'budget',
            'date_souhaitee', 'piece_jointe'
        ]
        widgets = {
            'nom': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Votre nom complet *',
                'required': True
            }),
            'entreprise': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nom de votre entreprise'
            }),
            'telephone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Votre numéro de téléphone *',
                'type': 'tel',
                'required': True
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Votre adresse email *',
                'required': True
            }),
            'ville': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Votre ville *',
                'required': True
            }),
            'service_souhaite': forms.Select(attrs={
                'class': 'form-control',
                'required': True
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Décrivez votre projet en détail...',
                'rows': 5
            }),
            'budget': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Budget estimé (ex: 500 000 - 1 000 000 FCFA)'
            }),
            'date_souhaitee': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'piece_jointe': forms.FileInput(attrs={
                'class': 'form-control',
                'accept': '.pdf,.doc,.docx,.jpg,.jpeg,.png,.zip'
            }),
        }
        labels = {
            'nom': 'Nom *',
            'entreprise': 'Entreprise',
            'telephone': 'Téléphone *',
            'email': 'Email *',
            'ville': 'Ville *',
            'service_souhaite': 'Service souhaité *',
            'description': 'Description du projet',
            'budget': 'Budget estimé',
            'date_souhaitee': 'Date souhaitée',
            'piece_jointe': 'Pièce jointe (devis, plans, photos...)',
        }

    def clean_telephone(self):
        telephone = self.cleaned_data.get('telephone')
        # Remove spaces, dots, dashes
        cleaned = telephone.replace(' ', '').replace('.', '').replace('-', '').replace('(', '').replace(')', '')
        if not cleaned.isdigit() and not cleaned.startswith('+'):
            raise forms.ValidationError("Veuillez entrer un numéro de téléphone valide.")
        return telephone

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email:
            return email.lower().strip()
        return email

