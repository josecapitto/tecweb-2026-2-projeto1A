from utils import *
from urllib.parse import unquote_plus
from database import *

def index(request):
    # A string de request sempre começa com o tipo da requisição (ex: GET, POST)
    if request.startswith('POST'):

        print("entrou aqui")
        request = request.replace('\r', '')  # Remove caracteres indesejados
        # Cabeçalho e corpo estão sempre separados por duas quebras de linha
        partes = request.split('\n\n')
        corpo = partes[1]
        params = {}
        for chave_valor in corpo.split('&'):
            chave, valor = chave_valor.split('=')
            params[unquote_plus(chave)] = unquote_plus(valor)

        save_note(params['titulo'], params['detalhes'])

        return build_response(code=303, reason='See Other', headers='Location: /')

    note_template = load_template('components/note.html')

    db = Database('banco')

    note_template = load_template('components/note.html')
    notes_li = []
    for dados in db.get_all():
        notes_li.append(note_template.format(title=dados.title, details=dados.content, id=dados.id))



    notes = '\n'.join(notes_li) 

    return build_response(body=load_template('index.html').format(notes=notes))

def editar(request, ide):
    
    if request.startswith('POST'):
        
        db = Database('banco')

        print("entrou aqui")
        request = request.replace('\r', '')  # Remove caracteres indesejados
        # Cabeçalho e corpo estão sempre separados por duas quebras de linha
        partes = request.split('\n\n')
        corpo = partes[1]
        params = {}
        for chave_valor in corpo.split('&'):
            chave, valor = chave_valor.split('=')
            params[unquote_plus(chave)] = unquote_plus(valor)
        
        antigo_titulo = params['titulo']
        antigo_detail = params['detalhes']

        update_note(ide, params['titulo'], params['detalhes'])

        return build_response(code=303, reason='See Other', headers='Location: /')



    note_template = load_template('components/note.html')
    db = Database('banco')
    notes_li = []
    for dados in db.get_all():
        if dados.id == ide: 
            return build_response(body=load_template('editar.html').format(notes=dados, titulo=dados.title, descricao=dados.content))