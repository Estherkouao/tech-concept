from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


# ======================================================
# USER MANAGER
# ======================================================

class UserManager(BaseUserManager):

    def create_user(self, username, password=None, **extra_fields):

        if not username:
            raise ValueError("Le nom d'utilisateur est obligatoire")

        user = self.model(
            username=username,
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)

        return user


    def create_superuser(self, username, password=None, **extra_fields):

        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("role", "admin")


        if extra_fields.get("is_staff") is not True:
            raise ValueError(
                "Le super utilisateur doit avoir is_staff=True"
            )


        if extra_fields.get("is_superuser") is not True:
            raise ValueError(
                "Le super utilisateur doit avoir is_superuser=True"
            )


        return self.create_user(
            username,
            password,
            **extra_fields
        )



# ======================================================
# USER MODEL
# ======================================================

class User(AbstractBaseUser, PermissionsMixin):

    ROLE_CHOICES = [
        ("admin", "Admin"),
        ("client", "Client"),
    ]


    username = models.CharField(
        max_length=150,
        unique=True,
        verbose_name="Nom utilisateur"
    )


    email = models.EmailField(
        max_length=254,
        unique=True,
        blank=True,
        null=True,
        verbose_name="Email"
    )


    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default="client",
        verbose_name="Rôle"
    )


    is_active = models.BooleanField(
        default=True,
        verbose_name="Actif"
    )


    is_staff = models.BooleanField(
        default=False,
        verbose_name="Staff"
    )


    objects = UserManager()


    USERNAME_FIELD = "username"

    REQUIRED_FIELDS = ["email"]



    class Meta:
        verbose_name = "Utilisateur"
        verbose_name_plural = "Utilisateurs"



    def __str__(self):

        return f"{self.username} ({self.role})"




# ======================================================
# DEMANDE DE DEVIS
# ======================================================

class DemandeDevis(models.Model):


    STATUT_CHOICES = [

        ("en_attente", "En attente"),

        ("contacte", "Contacté"),

        ("devis_envoye", "Devis envoyé"),

        ("termine", "Terminé"),

        ("annule", "Annulé"),

    ]



    SERVICES_CHOICES = [

        ("energie_solaire", "Énergie Solaire"),

        ("electricite_generale", "Électricité Générale"),

        ("reseau_informatique", "Réseau Informatique"),

        ("videosurveillance", "Vidéosurveillance"),

        ("controle_acces", "Contrôle d'Accès"),

        ("securite_incendie", "Sécurité Incendie"),

        ("cloture_electrique", "Clôture Électrique"),

        ("telephonie_ip", "Téléphonie IP"),

        ("maintenance", "Maintenance Technique"),

        ("autre", "Autre"),

    ]



    # Utilisateur connecté
    client = models.ForeignKey(

        User,

        on_delete=models.SET_NULL,

        null=True,

        blank=True,

        related_name="demandes_devis",

        verbose_name="Client"

    )



    # Référence automatique

    reference = models.CharField(

        max_length=20,

        unique=True,

        blank=True,

        verbose_name="Référence"

    )



    nom = models.CharField(

        max_length=200,

        verbose_name="Nom"

    )


    entreprise = models.CharField(

        max_length=200,

        blank=True,

        null=True,

        verbose_name="Entreprise"

    )


    telephone = models.CharField(

        max_length=20,

        verbose_name="Téléphone"

    )


    email = models.EmailField(

        max_length=254,

        verbose_name="Email"

    )


    ville = models.CharField(

        max_length=200,

        verbose_name="Ville"

    )


    service_souhaite = models.CharField(

        max_length=50,

        choices=SERVICES_CHOICES,

        verbose_name="Service souhaité"

    )


    description = models.TextField(

        blank=True,

        null=True,

        verbose_name="Description du projet"

    )


    budget = models.CharField(

        max_length=100,

        blank=True,

        null=True,

        verbose_name="Budget estimé"

    )


    date_souhaitee = models.DateField(

        blank=True,

        null=True,

        verbose_name="Date souhaitée"

    )


    piece_jointe = models.FileField(

        upload_to="devis_pieces/",

        blank=True,

        null=True,

        verbose_name="Pièce jointe"

    )


    statut = models.CharField(

        max_length=20,

        choices=STATUT_CHOICES,

        default="en_attente",

        verbose_name="Statut"

    )


    date_creation = models.DateTimeField(

        auto_now_add=True,

        verbose_name="Date création"

    )


    date_mise_a_jour = models.DateTimeField(

        auto_now=True,

        verbose_name="Dernière modification"

    )



    class Meta:

        verbose_name = "Demande de devis"

        verbose_name_plural = "Demandes de devis"

        ordering = ["-date_creation"]



    def save(self, *args, **kwargs):

        if not self.reference:

            nombre = DemandeDevis.objects.count() + 1

            self.reference = f"DEV-{nombre:05d}"


        super().save(*args, **kwargs)




    def __str__(self):

        return (
            f"{self.reference} - "
            f"{self.nom} - "
            f"{self.get_service_souhaite_display()}"
        )