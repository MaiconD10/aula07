from django.http import JsonResponse

from .models import Transacao


def listar_transacoes(request):
    transacoes = Transacao.objects.all().values(
        'id', 'descricao', 'valor', 'data', 'tipo', 'status', 'usuario', 'categoria'
    )
    return JsonResponse(list(transacoes), safe=False)
