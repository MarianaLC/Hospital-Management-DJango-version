from django.contrib.auth.models import User, UserManager, AbstractUser
from django.db import models


class Utilizador(User):
    nome = models.CharField(max_length=200)
    bi = models.CharField(max_length=200, unique=True)
    NIF = models.CharField(max_length=200, unique=True)
    morada = models.CharField(max_length=200)
    codigo_postal = models.CharField(max_length=200)

    objects = UserManager()

class Funcionario(Utilizador):
    class Meta:
        ordering = ('nome',)

    def __str__(self):
        return f"Nome : {self.nome}, bi : {self.bi}"

class Medico(Utilizador):
    especialidade = models.CharField(max_length=200)
    cedula = models.CharField(max_length=200)

    class Meta:
        ordering = ('nome',)

    def __str__(self):
        return f"Nome : {self.nome}, bi : {self.bi}"


class Enfermeiro(Utilizador):
    especialidade = models.CharField(max_length=200)

    class Meta:
        ordering = ('nome',)

    def __str__(self):
        return f"Nome : {self.nome}, bi : {self.bi}"


class Farmaceutico(Utilizador):
    class Meta:
        ordering = ('nome',)

    def __str__(self):
        return f"Nome : {self.nome}, bi : {self.bi}"


class Utente(Utilizador):
    class Meta:
        ordering = ('nome',)

    def __str__(self):
        return f"Nome : {self.nome}, bi : {self.bi}"


class Medicamento(models.Model):
    dci = models.CharField(max_length=200)
    nome_medicamento = models.CharField(max_length=200)
    forma_farmaceutica = models.CharField(max_length=100)
    dosagem = models.CharField(max_length=200)
    estado_autorizacao = models.BooleanField()
    generico = models.BooleanField()
    titular_AIM = models.CharField(max_length=200)

    class Meta:
        ordering = ('dci',)

    def __str__(self):
        return self.dci + ', ' + self.nome_medicamento + ', ' + self.forma_farmaceutica + ', ' + self.dosagem + ', ' \
               + str(self.generico) + \
               ', ' + self.titular_AIM


class Outro_Artigo(models.Model):
    nome_artigo = models.CharField(max_length=200)
    fornecedor = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.nome_artigo} - {self.fornecedor}"


class Stock_med(models.Model):
    farmaco = models.ForeignKey(Medicamento, unique=True, on_delete=models.CASCADE)
    quant = models.PositiveIntegerField()



class Stock_art(models.Model):
    artigo = models.ForeignKey(Outro_Artigo, unique=True, on_delete=models.CASCADE)
    quant = models.PositiveIntegerField()


class Ato_Medico(models.Model):
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    utente = models.ForeignKey(Utente, on_delete=models.CASCADE)
    hora = models.DateTimeField()
    quant_med = models.PositiveIntegerField(default=0)
    medicamento = models.ForeignKey(Medicamento, on_delete=models.SET_NULL, null=True)
    quant_art = models.PositiveIntegerField(default=0)
    outro_artigo = models.ForeignKey(Outro_Artigo, on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ('hora',)

    def __str__(self):
        return f"Médico : {self.medico}, Utente : {self.utente}, Hora : {self.hora}" \
               f", Medicamento : {self.quant_med, self.medicamento}, Outros Artigos : {self.quant_art, self.outro_artigo}"


class Ato_Enfermagem(models.Model):
    enfermeiro = models.ForeignKey(Enfermeiro, on_delete=models.CASCADE)
    utente = models.ForeignKey(Utente, on_delete=models.CASCADE)
    hora = models.DateTimeField()
    quant_art = models.PositiveIntegerField(default=0)
    outro_artigo = models.ForeignKey(Outro_Artigo, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"Enfermeiro : {self.enfermeiro.nome}, Utente : {self.utente.nome}, Hora : {self.hora}" \
               f", Outros Artigos : {self.quant_art, self.outro_artigo}"


class Ato_Farmaceutico(models.Model):
    farmaceutico = models.ForeignKey(Farmaceutico, on_delete=models.CASCADE)
    hora = models.DateTimeField()
    quant_med = models.PositiveIntegerField(default=0)
    medicamento = models.ForeignKey(Medicamento, on_delete=models.SET_NULL, null=True)
    quant_art = models.PositiveIntegerField(default=0)
    outro_artigo = models.ForeignKey(Outro_Artigo, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"Farmaceutico : {self.farmaceutico.nome}, Hora : {self.hora}, Medicamento : {self.quant_med, self.medicamento}" \
               f", Outros Artigos : {self.quant_art, self.outro_artigo}"
