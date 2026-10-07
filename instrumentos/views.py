from django.shortcuts import render, get_object_or_404, redirect
from .models import Instrumento


def _cart_count(request):
    return sum(request.session.get('carrinho', {}).values())


def index(request):
    busca = request.GET.get('q', '').strip()
    categoria = request.GET.get('categoria', '').strip()

    instrumentos = Instrumento.objects.all()
    if busca:
        instrumentos = instrumentos.filter(nome__icontains=busca)
    if categoria:
        instrumentos = instrumentos.filter(categoria=categoria)

    return render(request, 'index.html', {
        'instrumentos': instrumentos,
        'busca': busca,
        'categoria_filtro': categoria,
        'total_carrinho': _cart_count(request),
        'categorias': Instrumento.CATEGORIA_CHOICES,
    })


def detalhe(request, id):
    instrumento = get_object_or_404(Instrumento, id=id)
    return render(request, 'detalhe.html', {
        'instrumento': instrumento,
        'total_carrinho': _cart_count(request),
    })


def carrinho(request):
    sessao = request.session.get('carrinho', {})
    itens, total = [], 0
    for str_id, qtd in sessao.items():
        inst = get_object_or_404(Instrumento, id=int(str_id))
        subtotal = inst.preco * qtd
        total += subtotal
        itens.append({'instrumento': inst, 'quantidade': qtd, 'subtotal': subtotal})
    return render(request, 'carrinho.html', {
        'itens': itens,
        'total': total,
        'total_carrinho': len(itens),
    })


def adicionar_ao_carrinho(request, id):
    if request.method == 'POST':
        inst = get_object_or_404(Instrumento, id=id)
        sessao = request.session.get('carrinho', {})
        str_id = str(id)
        qty_atual = sessao.get(str_id, 0)
        if qty_atual < inst.estoque:
            sessao[str_id] = qty_atual + 1
            request.session['carrinho'] = sessao
            request.session.modified = True
    referrer = request.META.get('HTTP_REFERER', '/')
    return redirect(referrer)


def diminuir_do_carrinho(request, id):
    if request.method == 'POST':
        sessao = request.session.get('carrinho', {})
        str_id = str(id)
        if str_id in sessao:
            if sessao[str_id] <= 1:
                del sessao[str_id]
            else:
                sessao[str_id] -= 1
            request.session['carrinho'] = sessao
            request.session.modified = True
    return redirect('instrumentos:carrinho')


def remover_do_carrinho(request, id):
    if request.method == 'POST':
        sessao = request.session.get('carrinho', {})
        sessao.pop(str(id), None)
        request.session['carrinho'] = sessao
        request.session.modified = True
    return redirect('instrumentos:carrinho')
