from django import forms

from .models import patron, couturier, MaisonCouture, Comment

class SearchForm(forms.Form):
    query = forms.CharField(label='Entrer le nom complet pour rechercher ', max_length=100)


class PatronForm(forms.ModelForm):
    class Meta:
        model = patron
        fields = [ 'title', 'nomode', 'image', 'explain', 'topic', 'is_published', 'pub_date', ]

class couturierForm(forms.ModelForm):
    class Meta:
        model = couturier
        fields = [ 'nom_complet', 'nom_populaire', 'contact', 'email', 'nom_atelier', 'adresse_atelier', 'photo', ]

class MaisonCoutureForm(forms.ModelForm):
    class Meta:
        model = MaisonCouture
        fields = ['nom' ,'adresse', 'photo_atel', 'telephone','specialisation','email','site_web','description','date_creation']

class CommentAddForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [ 'Ajouter_commentaire' ]
