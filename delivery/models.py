from django.db import models

PAYMENT = (('chèque', 'chèque'),
('espéce', 'espéce'),
('compte', 'compte'),
('autre', 'autre'),)


STATUS = (('livré', 'livré'),
('en cours', 'en cours'),
('retourné', 'retourné'),
)


class OneClient(models.Model):
    nom = models.CharField(max_length=128, verbose_name="Nom du client")
    contact = models.CharField(max_length=128, verbose_name="Contact du client")
    adresse = models.CharField(max_length=128, verbose_name="Adresse du client")
    tel = models.CharField(max_length=128, verbose_name="Téléphone")

class OneDelivery(models.Model):
    num_facture = models.CharField(max_length=128, verbose_name="Numéro de Facture")
    destinataire = models.ForeignKey(OneClient, on_delete=models.CASCADE)
    bon_de_livraison = models.CharField(max_length=128, verbose_name="Bon de Livraison")
    nombre_de_colis = models.CharField(max_length=128, verbose_name="Nombre de Colis")
    type_de_paiment = models.CharField(max_length=128, verbose_name="Type de Paiment", choices=PAYMENT, null=True)
    status = models.CharField(max_length=128, verbose_name="status de la livraisons", choices=STATUS, default='en cours', null=True)
    creer_le = models.DateTimeField(auto_now_add=True, verbose_name="Livraison créer le :")
