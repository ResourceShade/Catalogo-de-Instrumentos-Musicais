# Harmonia Musical - Loja de Instrumentos Musicais

Projeto Django desenvolvido para a 1ª Avaliação da disciplina Frameworks Back-End.

## Descrição

Sistema de catálogo de instrumentos musicais com listagem geral e página de detalhe por item.

## Tecnologias

- Python 3.12
- Django 6.1.1

## Estrutura do Projeto

- **harmonia_musical/** - Projeto Django principal
- **instrumentos/** - Aplicação para gerenciamento de instrumentos

## Instalação e Execução

### 1. Ativar o ambiente virtual

```bash
source .venv/bin/activate
```

### 2. Aplicar as migrações

```bash
python manage.py makemigrations
python manage.py migrate
```

### 3. Criar superusuário (opcional)

```bash
python manage.py createsuperuser
```

### 4. Iniciar o servidor

```bash
python manage.py runserver
```

Acesse: http://127.0.0.1:8000/

### 5. Testar com DEBUG=False (opcional)

```bash
python manage.py collectstatic
# Altere DEBUG para False em harmonia_musical/settings.py
python manage.py runserver
```

## Funcionalidades

- [x] Model Instrumento com campos: nome, preco, estoque, categoria
- [x] Listagem de todos os instrumentos em tabela HTML
- [x] Página de detalhe dinâmica (/instrumentos/<id>/)
- [x] Links na listagem para páginas de detalhe
- [x] Arquivos estáticos (CSS, imagem e JavaScript)
- [x] Admin configurado com 8 registros de exemplo

## Autor

Desenvolvido pelo Grupo 14
