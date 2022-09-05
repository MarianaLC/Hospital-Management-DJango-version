from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from rest_framework import viewsets
from rest_framework import permissions, generics
from django.contrib.auth.models import Group
from rest_framework import filters
from django.core.exceptions import ValidationError
from django.contrib import messages
from rest_framework.response import Response

from .forms import *
from .serializers import *
from .models import *


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


class MedicamentoViewSet(viewsets.ModelViewSet):
    queryset = Medicamento.objects.all()
    serializer_class = MedicamentoSerializer
    permission_classes = [permissions.AllowAny]

class FuncionarioViewSet(viewsets.ModelViewSet):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer
    permission_classes = [permissions.AllowAny]

class Medicamento_ListView(generics.ListAPIView):
    queryset = Medicamento.objects.all()
    serializer_class = MedicamentoSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        print(f" Medicamento_medListView {self.request} {self.request.query_params}")

        nome = self.request.query_params.get('nome')
        if nome is not None:
            queryset = self.queryset.filter(nome_medicamento__icontains=nome)
        else:
            queryset = self.queryset.filter(id_med=-1)
        return queryset


class OutroArtigoViewSet(viewsets.ModelViewSet):
    queryset = Outro_Artigo.objects.all()
    serializer_class = OutroArtigoSerializer
    permission_classes = [permissions.AllowAny]


class OutroArtigo_ListView(generics.ListAPIView):
    queryset = Outro_Artigo.objects.all()
    serializer_class = OutroArtigoSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        print(f" OutroArtigo_artListView {self.request} {self.request.query_params}")

        nome = self.request.query_params.get('nome')
        if nome is not None:
            queryset = self.queryset.filter(nome_artigo__icontains=nome)
        else:
            queryset = self.queryset.filter(id_art=-1)
        return queryset


class UtenteViewSet(viewsets.ModelViewSet):
    queryset = Utente.objects.all()
    serializer_class = UtenteSerializer
    permission_classes = [permissions.AllowAny]


class MedicoViewSet(viewsets.ModelViewSet):
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer
    permission_classes = [permissions.AllowAny]


class FarmaceuticoViewSet(viewsets.ModelViewSet):
    queryset = Farmaceutico.objects.all()
    serializer_class = FarmaceuticoSerializer
    permission_classes = [permissions.AllowAny]


class EnfermeiroViewSet(viewsets.ModelViewSet):
    queryset = Enfermeiro.objects.all()
    serializer_class = EnfermeiroSerializer
    permission_classes = [permissions.AllowAny]


class Stock_medViewSet(viewsets.ModelViewSet):
    queryset = Stock_med.objects.all()
    serializer_class = StockmedSerializer
    permission_classes = [permissions.AllowAny]


class Stock_medListView(generics.ListAPIView):
    queryset = Stock_med.objects.all()
    serializer_class = StockmedSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        print(f" Stock_medListView {self.request} {self.request.query_params}")
        queryset = Stock_med.objects.all()
        med = self.request.query_params.get('med')
        if med is not None:
            queryset = queryset.filter(id_med=med)
        else:
            queryset.filter(id_med=-1)
        return queryset


class Stock_artViewSet(viewsets.ModelViewSet):
    queryset = Stock_art.objects.all()
    serializer_class = StockartSerializer
    permission_classes = [permissions.AllowAny]

class Stock_artListView(generics.ListAPIView):
    queryset = Stock_art.objects.all()
    serializer_class = StockartSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        print(f" Stock_artListView {self.request} {self.request.query_params}")
        queryset = Stock_art.objects.all()
        art = self.request.query_params.get('art')
        if art is not None:
            queryset = queryset.filter(id_art=art)
        else:
            queryset.filter(id_art=-1)
        return queryset

# -----------------------------------------------------------------------------------------------------------------------
def log_out(request):
    logout(request)
    form = LoginForm(request.POST or None)
    m = "Logout efetuado."
    return render(request, "login.html", {'form': form, 'logout': m})


def log_in(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        password = form.cleaned_data.get('password')
        username = form.cleaned_data.get('username')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user in User.objects.filter(groups__name="Farmacêuticos"):
                login(request, user)
                return HttpResponseRedirect('menufarmaceutico')
            elif user in User.objects.filter(groups__name="Funcionário"):
                login(request, user)
                return HttpResponseRedirect('menufuncionario')
            elif user in User.objects.filter(groups__name="Utentes"):
                login(request, user)
                return HttpResponseRedirect('menuutente')
            elif user in User.objects.filter(groups__name="Médicos"):
                login(request, user)
                return HttpResponseRedirect('menumedico')
            elif user in User.objects.filter(groups__name="Enfermeiros"):
                login(request, user)
                return HttpResponseRedirect('menuenfermeiro')
            elif user.is_superuser:
                login(request, user)
                return HttpResponseRedirect('/admin')
            else:
                raise ValidationError('Invalid user')

    return render(request, "login.html", {'form': form})


# -----------------------------------------------------------------------------------------------------------------------
def AddGroup(request,id,gid):
    myuser = User.objects.get(id=id)
    my_group = Group.objects.get(id=gid)
    my_group.user_set.add(myuser)

# -----------------MENUS-----------------------------------------------------------------------------------------------------

@login_required(login_url='/hospital')
def menu_utente(request):
    return render(request, "menuutente.html", {})

@login_required(login_url='/hospital')
def menu_medico(request):
    return render(request, "menumedico.html", {})

@login_required(login_url='/hospital')
def menu_enfermeiro(request):
    return render(request, "menuenfermeiro.html", {})

@login_required(login_url='/hospital')
def menu_farmaceutico(request):
    return render(request, "menufarmaceutico.html", {})

@login_required(login_url='/hospital')
def menu_funcionario(request):
    return render(request, "menufuncionario.html", {})

#------------------------UTENTE------------------------------------------

@login_required(login_url='/hospital')
def ver_ficha_utente(request):
    if request.method == "GET":
            utente = Utente.objects.get(id=request.user.id)
            query_set = utente.ato_medico_set.all()
            query_atos = utente.ato_enfermagem_set.all()
            atosmedicos = []
            atosenfermagem = []
            utente_info = []
            for ato in query_set:
                atosmedicos.append({'Médico': ato.medico.nome,'Utente': ato.utente.nome, 'Hora': ato.hora, 'Medicamento': ato.medicamento.nome_medicamento, 'Outros Artigos': ato.outro_artigo.nome_artigo})

            for ato in query_atos:
                atosenfermagem.append({'Enfermeiro': ato.enfermeiro.nome,'Utente': ato.utente.nome, 'Hora': ato.hora, 'Outros Artigos': ato.outro_artigo.nome_artigo})

            print(atosmedicos)
            print(atosenfermagem)
            utente_info.append({'Nome': utente.nome,'bi': utente.bi, 'NIF': utente.NIF, 'Morada': utente.morada, 'Código Postal': utente.codigo_postal})
            context = {'atosmedicos': atosmedicos, 'atosenfermagem': atosenfermagem, 'utente_info': utente_info}
            return render(request, "fichautente.html", context)


#---------------------------------STOCK----------------------------------------------------------------------------
def auxiliar_retirar_stock_med(codigo_medicamento,quantidade):
    stock_med = Stock_med.objects.get(farmaco=codigo_medicamento)

    stock_med.quant = stock_med.quant-quantidade
    stock_med.save()


def retirar_stock_med(request,pk,quantidade ): # este pk tem que ser o do medicamento introduzido no ato medico
    auxiliar_retirar_stock_med(pk,quantidade)


def auxiliar_retirar_stock_art(codigo_artigo,quantidade):
    stock_art = Stock_art.objects.get(artigo=codigo_artigo)
    stock_art.quant = stock_art.quant - quantidade
    stock_art.save()


def retirar_stock_art(request,pk,quantidade):
    auxiliar_retirar_stock_art(pk,quantidade)

def auxiliar_adicionar_stock_med(codigo_medicamento,quantidade):
    stock_med = Stock_med.objects.get(farmaco=codigo_medicamento)

    stock_med.quant = stock_med.quant + quantidade
    stock_med.save()

def adicionar_stock_med(request,pk,quantidade ): # este pk tem que ser o do medicamento introduzido no ato medico
    auxiliar_adicionar_stock_med(pk,quantidade)

def auxiliar_adicionar_stock_art(codigo_artigo,quantidade):
    stock_art = Stock_art.objects.get(artigo=codigo_artigo)
    stock_art.quant = stock_art.quant + quantidade
    stock_art.save()

def adicionar_stock_art(request,pk,quantidade):
    auxiliar_adicionar_stock_art(pk,quantidade)


#------------------------------------------------FUNCIONARIO------------------------------------------------------

@login_required(login_url='/hospital')
def medico_estatisticas(request):
    if request.method == "GET":

        totalatmed = len(Ato_Medico.objects.all())
        totalmed = len(Medico.objects.all())

        mediaM = totalatmed / totalmed

        qntmax2 = 0
        for med in Medico.objects.all():
            if len(Ato_Medico.objects.filter(medico=med)) > qntmax2:
                qntmax2 = len(Ato_Medico.objects.filter(medico=med))
                medmax = med

        context = {"mediaM": mediaM,"medmax": medmax}

        return render(request, "medicoestatisticas.html", context)

@login_required(login_url='/hospital')
def enfermeiro_estatisticas(request):
    if request.method == "GET":

        totalatenf = len(Ato_Enfermagem.objects.all())
        totalenf = len(Enfermeiro.objects.all())

        mediaE = totalatenf / totalenf

        qntmax2 = 0
        for enf in Enfermeiro.objects.all():
            if len(Ato_Enfermagem.objects.filter(enfermeiro=enf)) > qntmax2:
                qntmax2 = len(Ato_Enfermagem.objects.filter(enfermeiro=enf))
                enfmax = enf


        context = {"mediaE": mediaE,"enfmax": enfmax}

        return render(request, "enfermeiroestatisticas.html", context)


@login_required(login_url='/hospital')
def farmaceutico_estatisticas(request):
    if request.method == "GET":

        totalatof = len(Ato_Farmaceutico.objects.all())
        totalfar = len(Farmaceutico.objects.all())

        mediaF = totalatof / totalfar

        qntmax2 = 0
        for far in Farmaceutico.objects.all():
            if len(Ato_Farmaceutico.objects.filter(farmaceutico=far)) > qntmax2:
                qntmax2 = len(Ato_Farmaceutico.objects.filter(farmaceutico=far))
                farmax = far

        query_set = Stock_med.objects.all()
        meds_mais_stock = []
        c = 0
        for stock_med in query_set:
            if c <= 2:
                meds_mais_stock.append(
                    {'Medicamento': stock_med.farmaco.nome_medicamento, 'Quantidade': stock_med.quant})
            c = c + 1

        query_sety = Stock_art.objects.all()
        arts_mais_stock = []
        d = 0
        for stock_art in query_sety:
            if d <= 2:
                arts_mais_stock.append(
                    {'Artigo': stock_art.artigo.nome_artigo, 'Quantidade': stock_art.quant})
            d = d + 1

        context = {'meds_mais_stock': meds_mais_stock, 'arts_mais_stock': arts_mais_stock, "mediaF": mediaF,
                   "farmax": farmax}

        return render(request, "farmaceuticoestatisticas.html", context)

@login_required(login_url='/hospital')
def utente_estatisticas(request):
    if request.method == "GET":

        totalatmed = len(Ato_Medico.objects.all())
        totalut = len(Utente.objects.all())

        mediaU = totalatmed / totalut

        qntmax2 = 0
        for ut in Utente.objects.all():
            if len(Ato_Medico.objects.filter(utente=ut)) > qntmax2:
                qntmax2 = len(Ato_Medico.objects.filter(utente=ut))
                utmax = ut

        totalatenf = len(Ato_Enfermagem.objects.all())

        mediaUE = totalatenf / totalut

        qntmax2 = 0
        for ut in Utente.objects.all():
            if len(Ato_Enfermagem.objects.filter(utente=ut)) > qntmax2:
                qntmax2 = len(Ato_Enfermagem.objects.filter(utente=ut))
                utmaxe = ut

        context = {"mediaU": mediaU,"utmax": utmax,"mediaUE":mediaUE, "utmaxe":utmaxe}

        return render(request, "utenteestatisticas.html", context)

#------------------------------------------------MÉDICO------------------------------------------------------
@login_required(login_url='/hospital')
def atomedico_create(request):
    form = FormAtoMedico(request.POST or None)
    #print(form.is_valid())
    if form.is_valid():
        if len(Ato_Medico.objects.filter(hora=form.cleaned_data['hora'])) == 0:  # se não há um ato na esta hora
            form.save()
            id_medicamento=form.cleaned_data['medicamento'].id
            quant_medicamento=form.cleaned_data['quant_med']
            retirar_stock_med('POST',id_medicamento,quant_medicamento)
            id_artigo = form.cleaned_data['outro_artigo'].id
            quant_artigo = form.cleaned_data['quant_art']
            retirar_stock_art('POST', id_artigo, quant_artigo)
            return render(request, "sucesso.html", {})

        else:
            if (len(Ato_Medico.objects.filter(medico=form.cleaned_data['medico'])) == 0 or len( # se existir a esta hora confirma-se
                    Ato_Medico.objects.filter(utente=form.cleaned_data['utente'])) == 0):
                form.save()
                id_medicamento = form.cleaned_data['medicamento'].id
                quant_medicamento = form.cleaned_data['quant_med']
                retirar_stock_med('POST', id_medicamento, quant_medicamento)
                id_artigo = form.cleaned_data['outro_artigo'].id
                quant_artigo = form.cleaned_data['quant_art']
                retirar_stock_art('POST', id_artigo, quant_artigo)
                return render(request, "sucesso.html", {})

            else:
                return render(request, "erro.html", {})

    return render(request, "atomedico_create.html", {'form': form})


@login_required(login_url='/hospital')
def info_medico(request):
    if request.method == "GET":
            medico = Medico.objects.get(id=request.user.id)
            medico_info = []
            medico_info.append({'Nome': medico.nome,'bi': medico.bi, 'NIF': medico.NIF, 'Morada': medico.morada, 'Código Postal': medico.codigo_postal, 'Especialidade': medico.especialidade, 'Cedula': medico.cedula})
            context = {'medico_info':medico_info}
            return render(request, "infomedico.html", context)

@login_required(login_url='/hospital')
def medico_atos(request):
    if request.method == "GET":
            medico = Medico.objects.get(id=request.user.id)
            query_set = medico.ato_medico_set.all()
            atosmedicos = []
            for ato in query_set:
                atosmedicos.append({'Médico': ato.medico.nome,'Utente': ato.utente.nome, 'Hora': ato.hora, 'Medicamento': ato.medicamento.nome_medicamento, 'Quantidade medicamento': ato.quant_med, 'Outros Artigos': ato.outro_artigo.nome_artigo, 'Quantidade artigo': ato.quant_art})
            print(atosmedicos)
            context = {'atosmedicos': atosmedicos}
            return render(request, "medicoatos.html", context)


#------------------------------------------------ENFERMEIRO------------------------------------------------------
@login_required(login_url='/hospital')
def atoenfermagem_create(request):
    form = FormAtoEnfermagem(request.POST or None)
    print(form.is_valid())
    if form.is_valid():
        if len(Ato_Enfermagem.objects.filter(hora=form.cleaned_data['hora'])) == 0:  # se não há um ato na esta hora
            form.save()
            id_artigo = form.cleaned_data['outro_artigo'].id
            quant_artigo = form.cleaned_data['quant_art']
            retirar_stock_art('POST', id_artigo, quant_artigo)
            return render(request, "sucesso.html", {})

        else:
            if (len(Ato_Enfermagem.objects.filter(enfermeiro=form.cleaned_data['enfermeiro'])) == 0 or len( # se existir a esta hora confirma-se
                    Ato_Enfermagem.objects.filter(utente=form.cleaned_data['utente'])) == 0):
                form.save()
                id_artigo = form.cleaned_data['outro_artigo'].id
                quant_artigo = form.cleaned_data['quant_art']
                retirar_stock_art('POST', id_artigo, quant_artigo)
                return render(request, "sucesso.html", {})

            else:
                return render(request, "erro.html", {})

    return render(request, "atoenfermagem_create.html", {'form': form})



@login_required(login_url='/hospital')
def info_enfermeiro(request):
    if request.method == "GET":
            enfermeiro = Enfermeiro.objects.get(id=request.user.id)
            enfermeiro_info = []
            enfermeiro_info.append({'Nome': enfermeiro.nome,'bi': enfermeiro.bi, 'NIF': enfermeiro.NIF, 'Morada': enfermeiro.morada, 'Código Postal': enfermeiro.codigo_postal, 'Especialidade' : enfermeiro.especialidade})
            context = {'enfermeiro_info': enfermeiro_info}
            return render(request, "enfermeiro_info.html", context)


@login_required(login_url='/hospital')
def enfermeiro_atos(request):
    if request.method == "GET":
            enfermeiro = Enfermeiro.objects.get(id=request.user.id)
            query_set = enfermeiro.ato_enfermagem_set.all()
            atosenfermagem = []
            for ato in query_set:
                atosenfermagem.append({'Enfermeiro': ato.enfermeiro.nome,'Utente': ato.utente.nome, 'Hora': ato.hora, 'Outros Artigos': ato.outro_artigo.nome_artigo, 'Quantidade artigo': ato.quant_art})
            print(atosenfermagem)
            context = {'atosenfermagem': atosenfermagem}
            return render(request, "enfermeiroatos.html", context)


#-----------------------------------------------FARMACEUTICO----------------------------------------------------------------------------------

@login_required(login_url='/hospital')
def atofarmaceutico_create(request):
    form = FormAtoFarmaceutico(request.POST or None)
    print(form.is_valid())
    print(form.errors)
    if form.is_valid():
        if len(Ato_Farmaceutico.objects.filter(hora=form.cleaned_data['hora'])) == 0:  # se não há um ato na esta hora
            form.save()
            id_medicamento=form.cleaned_data['medicamento'].id
            quant_medicamento=form.cleaned_data['quant_med']
            adicionar_stock_med('POST',id_medicamento,quant_medicamento)
            id_artigo = form.cleaned_data['outro_artigo'].id
            quant_artigo = form.cleaned_data['quant_art']
            adicionar_stock_art('POST', id_artigo, quant_artigo)
            return render(request, "sucesso.html", {})

        else:
            if (len(Ato_Farmaceutico.objects.filter(farmaceutico=form.cleaned_data['farmaceutico'])) == 0):
                form.save()
                id_medicamento = form.cleaned_data['medicamento'].id
                quant_medicamento = form.cleaned_data['quant_med']
                adicionar_stock_med('POST', id_medicamento, quant_medicamento)
                id_artigo = form.cleaned_data['outro_artigo'].id
                quant_artigo = form.cleaned_data['quant_art']
                adicionar_stock_art('POST', id_artigo, quant_artigo)
                return render(request, "sucesso.html", {})

            else:
                return render(request, "erro.html", {})

    return render(request, "atofarmaceutico_create.html", {'form': form})

@login_required(login_url='/hospital')
def info_farmaceutico(request):
    if request.method == "GET":
            farmaceutico = Farmaceutico.objects.get(id=request.user.id)
            farmaceutico_info = []
            farmaceutico_info.append({'Nome': farmaceutico.nome,'bi': farmaceutico.bi, 'NIF': farmaceutico.NIF, 'Morada': farmaceutico.morada, 'Código Postal': farmaceutico.codigo_postal})
            context = {'farmaceutico_info':farmaceutico_info}
            return render(request, "info_farmaceutico.html", context)


@login_required(login_url='/hospital')
def farmaceutico_atos(request):
    if request.method == "GET":
            farmaceutico = Farmaceutico.objects.get(id=request.user.id)
            query_set = farmaceutico.ato_farmaceutico_set.all()
            atosfarmaceuticos = []
            for ato in query_set:
                atosfarmaceuticos.append({'Farmacêutico': ato.farmaceutico.nome, 'Hora': ato.hora, 'Medicamento': ato.medicamento.nome_medicamento, 'Quantidade medicamento': ato.quant_med, 'Outros Artigos': ato.outro_artigo.nome_artigo, 'Quantidade artigo': ato.quant_art})
            print(atosfarmaceuticos)
            context = {'atosfarmaceuticos': atosfarmaceuticos}
            return render(request, "farmaceuticoatos.html", context)


@login_required(login_url='/hospital')
def farmaceutico_alerta(request):
    if request.method == "GET":
        query_set = Stock_med.objects.filter(quant__lte = 250)
        em_falta_med = []
        for stock_med in query_set:
            em_falta_med.append({'Medicamento': stock_med.farmaco.nome_medicamento, 'Quantidade': stock_med.quant})
        print(em_falta_med)
        query_sety = Stock_art.objects.filter(quant__lte=250)
        em_falta_art = []
        for stock_art in query_sety:
            em_falta_art.append({'Artigo': stock_art.artigo.nome_artigo, 'Quantidade': stock_art.quant})
        print(em_falta_art)
        context = {'em_falta_med': em_falta_med, 'em_falta_art': em_falta_art }
        return render(request, "farmaceuticoalerta.html", context)


@login_required(login_url='/hospital')
def adiciona_medicamento(request):
    form = FormMedicamento(request.POST or None)
    #print(form.is_valid())
    if form.is_valid():
        medicamento = form.cleaned_data
        nome = medicamento.get('nome_medicamento')
        dci = medicamento.get('dci')
        titular_AIM = medicamento.get('titular_AIM')
        dosagem = medicamento.get('dosagem')
        generico = medicamento.get('generico')
        forma=medicamento.get('forma_farmaceutica')
        estado = medicamento.get('estado_autorizacao')
        print(Medicamento.objects.filter(nome_medicamento=nome,dci=dci,titular_AIM=titular_AIM,dosagem=dosagem,forma_farmaceutica=forma,
                                                 generico=generico,estado_autorizacao=estado))
        if(len(Medicamento.objects.filter(nome_medicamento=nome,dci=dci,titular_AIM=titular_AIM,dosagem=dosagem,generico=generico,estado_autorizacao=estado)))==0:
            form.save()
            objeto_id=Medicamento.objects.filter(nome_medicamento=nome,dci=dci,titular_AIM=titular_AIM,dosagem=dosagem,forma_farmaceutica=forma,
                                                 generico=generico,estado_autorizacao=estado).first()

            b=Stock_med(farmaco=objeto_id,quant=505)
            b.save()
            return render(request, "sucesso.html", {})
        else:
            return render(request, "erro.html", {})

    return render(request, "adiciona_medicamento.html", {'form': form})

@login_required(login_url='/hospital')
def adiciona_outro_artigo(request):
    form = FormOutroArtigo(request.POST or None)
    #print(form.is_valid())
    if form.is_valid():
        outro_artigo = form.cleaned_data
        nome = outro_artigo.get('nome_artigo')
        fornecedor = outro_artigo.get('fornecedor')
        print(Outro_Artigo.objects.filter(nome_artigo=nome,fornecedor=fornecedor))
        if(len(Outro_Artigo.objects.filter(nome_artigo=nome,fornecedor=fornecedor)))==0:
            form.save()
            objeto_id=Outro_Artigo.objects.filter(nome_artigo=nome,fornecedor=fornecedor).first()

            b=Stock_art(artigo=objeto_id,quant=505)
            b.save()
            return render(request, "sucesso.html", {})
        else:
            return render(request, "erro.html", {})

    return render(request, "adiciona_outro_artigo.html", {'form': form})


@login_required(login_url='/hospital')
def farmaceutico_stock_med(request):
    if request.method == "GET":
        query_set = Stock_med.objects.all()
        stock_med = []
        for stock in query_set:
            stock_med.append({'Medicamento': stock.farmaco.nome_medicamento, 'Quantidade': stock.quant})
        print(stock_med)

        context = {'stock_med': stock_med}
        return render(request, "farmaceuticostockmed.html", context)

@login_required(login_url='/hospital')
def farmaceutico_stock_art(request):
    if request.method == "GET":
        query_set = Stock_art.objects.all()
        stock_art = []
        for stock in query_set:
            stock_art.append({'Artigo': stock.artigo.nome_artigo, 'Quantidade': stock.quant})
        print(stock_art)

        context = {'stock_art': stock_art}
        return render(request, "farmaceuticostockart.html", context)
