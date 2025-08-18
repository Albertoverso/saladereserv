from django.utils import timezone

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Sala, Reserva
from .forms import SalaForm, ReservaForm

@login_required
def dashboard(request):
    reservas = Reserva.objects.filter(funcionario=request.user)
    return render(request, 'core/dashboard.html', {'reservas': reservas})

@login_required
def salas(request):
    salas = Sala.objects.all()
    return render(request, 'core/salas.html', {'salas': salas})

@login_required
def sala_nova(request):
    form = SalaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('salas')
    return render(request, 'core/sala_form.html', {'form': form})

@login_required
def sala_editar(request, id):
    sala = get_object_or_404(Sala, pk=id)
    form = SalaForm(request.POST or None, instance=sala)
    if form.is_valid():
        form.save()
        return redirect('salas')
    return render(request, 'core/sala_form.html', {'form': form})

@login_required
def sala_excluir(request, id):
    sala = get_object_or_404(Sala, pk=id)
    hoje = timezone.localdate()
    reservas_futuras = Reserva.objects.filter(sala=sala, data__gte=hoje)

    if reservas_futuras.exists():
        return render(request, 'core/erro_exclusao.html', {
            'mensagem': 'Sala não pode ser excluída pois possui reservas futuras.'
        })

    if request.method == 'POST':
        sala.delete()
        return redirect('salas')

    return render(request, 'core/confirmar_exclusao_sala.html', {'sala': sala})


@login_required
def reservas(request):
    reservas = Reserva.objects.filter(funcionario=request.user)
    return render(request, 'core/reservas.html', {'reservas': reservas})

@login_required
def reserva_nova(request):
    form = ReservaForm(request.POST or None)
    if form.is_valid():
        nova = form.save(commit=False)
        nova.funcionario = request.user
        nova.save()
        return redirect('reservas')
    return render(request, 'core/reserva_form.html', {'form': form})

@login_required
def reserva_cancelar(request, id):
    reserva = get_object_or_404(Reserva, pk=id, funcionario=request.user)
    reserva.delete()
    return redirect('reservas')
