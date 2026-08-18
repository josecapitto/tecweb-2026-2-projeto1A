from utils import load_data, load_template, save_note, build_response
from urllib.parse import unquote_plus


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

    notes_li = [
        note_template.format(title=dados['titulo'], details=dados['detalhes'])
        for dados in load_data('notes.json')
    ]
    notes = '\n'.join(notes_li)

    return build_response(body=load_template('index.html').format(notes=notes))