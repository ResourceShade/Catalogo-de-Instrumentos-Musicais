# Harmonia Musical — Loja de Instrumentos Musicais

**1ª Avaliação · Disciplina: Frameworks Back-End**  
Professor: Rafael Rodrigues · Grupo 14

---

## Integrantes

| Nome                            | RA       |
| ------------------------------- | -------- |
| Arthur Felix Oliveira Torres    | 01848455 |
| Felipe Gabriel Barbosa Dionizio | 01848719 |
| Tiago Renato Vinícius Silva     | 01808230 |

---

## Sobre o projeto

A **Harmonia Musical** é uma aplicação web desenvolvida com Django que simula o catálogo online de uma loja de instrumentos musicais. O sistema exibe os produtos disponíveis em grade de cards, permite visualizar o detalhe de cada instrumento e conta com um carrinho de compras funcional.

O banco de dados inclui 8 instrumentos cadastrados pelo painel administrativo do Django, distribuídos entre as categorias Corda, Sopro, Percussão e Teclas.

---

## Tecnologias

- Python 3.12
- Django 6.1.1
- SQLite
- HTML5, CSS3 e JavaScript

---

## Como executar

**1. Ativar o ambiente virtual**
```bash
source .venv/bin/activate
```

**2. Aplicar as migrações**
```bash
python manage.py migrate
```

**3. Iniciar o servidor**
```bash
python manage.py runserver
```

Acesse em: `http://127.0.0.1:8000`

O painel administrativo fica em `http://127.0.0.1:8000/admin`.

**Testando com DEBUG=False**
```bash
python manage.py collectstatic
# Alterar DEBUG = False em harmonia_musical/settings.py
python manage.py runserver
```

---

## Requisitos atendidos

Conforme a especificação do Grupo 14:

- [x] Model `Instrumento` com os campos `nome`, `preco`, `estoque` e `categoria`
- [x] Migrações criadas e aplicadas (`makemigrations` / `migrate`)
- [x] Model registrado no Admin com 8 registros de exemplo cadastrados
- [x] Página de listagem (`index`) exibindo todos os instrumentos em grade HTML
- [x] Rota dinâmica de detalhe — `/instrumentos/<id>/` — com view e template próprios
- [x] Nome de cada instrumento na listagem funciona como link para a página de detalhe
- [x] Arquivo de estilos estático (`static/css/estilos.css`) aplicado em todas as páginas
- [x] Imagem exibida via `{% static %}` nos templates
- [x] Arquivo `static/js/script.js` com função JavaScript acionada por botão
- [x] Projeto testado com `DEBUG = True` e `DEBUG = False`

---

## Extras

Além dos requisitos obrigatórios, o grupo expandiu o projeto com funcionalidades adicionais:

**Interface e navegação**
- Grade de cards no catálogo, com imagem, categoria e indicador de estoque por produto
- Imagem individual para cada instrumento (campo `imagem` adicionado ao model)
- Barra de busca para filtrar produtos por nome
- Filtros por categoria na barra de navegação (Corda, Sopro, Percussão, Teclas, Outros)
- Breadcrumb de navegação na página de detalhe
- Design responsivo — funciona em desktop, tablet e celular
- Rodapé sempre fixo na borda inferior da tela

**Carrinho de compras**
- Carrinho funcional usando sessions do Django
- Controles de quantidade (+/−) diretamente na página do carrinho
- Validação de estoque: o sistema não permite adicionar mais unidades do que há disponível
- Diálogo de confirmação ao remover um item (`confirm()` nativo do JavaScript)
- Resumo do pedido com subtotal por item, frete e total geral

**JavaScript com uso real**
- O botão "Finalizar Pedido" dispara um `alert()` informando que o pagamento está temporariamente em manutenção — cumprindo o requisito de função JS com uma aplicação contextual dentro do fluxo do site

---

## Estrutura de arquivos

```
loja-instrumentos-musicais/
├── harmonia_musical/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── instrumentos/
│   ├── migrations/
│   ├── static/
│   │   ├── css/
│   │   │   └── estilos.css
│   │   ├── js/
│   │   │   └── script.js
│   │   └── images/
│   ├── templates/
│   │   ├── index.html
│   │   ├── detalhe.html
│   │   └── carrinho.html
│   ├── admin.py
│   ├── models.py
│   ├── views.py
│   └── urls.py
├── manage.py
└── requirements.txt
```
