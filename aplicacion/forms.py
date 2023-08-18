from django import forms

class ClienteForm(forms.Form):
    nombre = forms.CharField(label= "Nombre del cliente", max_length=50, required=True)
    apellido = forms.CharField(label= "Apellido del cliente", max_length=50, required=True)
    telefono = forms.IntegerField(label= "Telefono", required=True)
    email = forms.EmailField(label="Email", required=True)

class PantalonesForm(forms.Form):
    marca = forms.CharField(label= "Marca", max_length=50, required=True)
    talle = forms.IntegerField(label= "Talle", required=True)
    email = forms.EmailField(label="Email", required=True)
