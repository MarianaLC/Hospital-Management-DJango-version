from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import *


# Form para log in
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())  # esconde a palavra passe do ecrã

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('Incorrect username or password! Please, try again.')
            if not user.check_password(password):
                raise forms.ValidationError('Incorrect username or password! Please, try again.')
        return super(LoginForm, self).clean(*args, **kwargs)


# ---------------------------------------------------ADMIN-------------------------------------------------------
# Utente admin
class UtenteCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = Utente
        fields = ('username', 'nome', 'bi', 'NIF', 'morada', 'codigo_postal', 'email',)

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super(UtenteCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()

        return user


class UtenteChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = Utente
        fields = ('username', 'nome', 'bi', 'NIF', 'morada', 'codigo_postal', 'email',)

    def clean_password(self):
        return self.initial['password']

# Funcionario admin
class FuncionarioCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = Funcionario
        fields = ('username', 'nome', 'bi', 'NIF', 'morada', 'codigo_postal', 'email',)

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super(FuncionarioCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()

        return user


class FuncionarioChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = Funcionario
        fields = ('username', 'nome', 'bi', 'NIF', 'morada', 'codigo_postal', 'email',)

    def clean_password(self):
        return self.initial['password']


class EnfermeiroCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = Enfermeiro
        fields = ('username', 'nome', 'bi', 'NIF', 'morada', 'codigo_postal', 'especialidade',)

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super(EnfermeiroCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()

        return user


class EnfermeiroChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = Enfermeiro
        fields = ('username', 'nome', 'bi', 'NIF', 'morada', 'codigo_postal', 'especialidade',)

    def clean_password(self):
        return self.initial['password']


class MedicoCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = Medico
        fields = ('username', 'nome', 'bi', 'NIF', 'morada', 'codigo_postal', 'especialidade', 'cedula',)

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super(MedicoCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()

        return user


class MedicoChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = Medico
        fields = ('username', 'nome', 'morada', 'NIF', 'bi', 'codigo_postal', 'especialidade', 'cedula')

    def clean_password(self):
        return self.initial['password']


class FarmaceuticoCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = Farmaceutico
        fields = ('username', 'nome', 'bi', 'NIF', 'morada', 'codigo_postal',)

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super(FarmaceuticoCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()

        return user


class FarmaceuticoChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = Farmaceutico
        fields = ('username', 'nome', 'bi', 'NIF', 'morada', 'codigo_postal',)

    def clean_password(self):
        return self.initial['password']


# ---------------------------------------------------------------------------------------------

class FormFuncionario(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = ['nome', 'bi', 'NIF', 'morada', 'codigo_postal', 'email']


class FormUtente(forms.ModelForm):
    class Meta:
        model = Utente
        fields = ['nome', 'bi', 'NIF', 'morada', 'codigo_postal', 'email']


class FormFarmaceutico(forms.ModelForm):
    class Meta:
        model = Farmaceutico
        fields = ['nome', 'bi', 'NIF', 'morada', 'codigo_postal', 'email']


class FormMedico(forms.ModelForm):
    class Meta:
        model = Medico
        fields = ['nome', 'bi', 'NIF', 'morada', 'codigo_postal', 'especialidade', 'cedula', 'email']


class FormEnfermeiro(forms.ModelForm):
    class Meta:
        model = Enfermeiro
        fields = ['nome', 'bi', 'NIF', 'morada', 'codigo_postal', 'especialidade', 'email']


class FormMedicamento(forms.ModelForm):
    class Meta:
        model = Medicamento
        fields = ['dci','nome_medicamento', 'forma_farmaceutica', 'dosagem', 'estado_autorizacao', 'generico', 'titular_AIM']


class FormOutroArtigo(forms.ModelForm):
    class Meta:
        model = Outro_Artigo
        fields = ['nome_artigo', 'fornecedor']


class FormAtoMedico(forms.ModelForm):
    class Meta:
        model = Ato_Medico
        fields = ['medico', 'utente', 'hora', 'quant_med', 'medicamento', 'quant_art', 'outro_artigo']


class FormAtoEnfermagem(forms.ModelForm):
    class Meta:
        model = Ato_Enfermagem
        fields = ['enfermeiro', 'utente', 'hora', 'quant_art', 'outro_artigo']


class FormAtoFarmaceutico(forms.ModelForm):
    class Meta:
        model = Ato_Farmaceutico
        fields = ['farmaceutico','hora', 'quant_med', 'medicamento', 'quant_art', 'outro_artigo']


# -----------------------------------------------------------------------------------------------------------------------
