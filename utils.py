import json
import os

def extract_route(requi):
    lista = requi.split(" ")
    get = lista[1]
    nova_string = get[1:]
    return nova_string

def read_file(path):
    return open(path, "r+b").read()

def load_data(path):
    dicio = json.loads(open("data/"+path, "r", encoding='UTF-8').read())
    return dicio

def load_template(nome_arquivo):
    caminho = os.path.join("templates", nome_arquivo)
    with open(caminho, "r", encoding="utf-8") as file:
        return file.read()

def build_response(body='', code=200, reason='OK', headers=''):
    response = f"HTTP/1.1 {code} {reason}\n"
    if headers:
        response += headers + "\n"
    response += "\n"
    response += body
    return response.encode()

def save_note(titulo, detalhes):
    dados = load_data('notes.json')
    dados.append({'titulo': titulo, 'detalhes': detalhes})
    with open('data/notes.json', 'w', encoding='utf-8') as file:
        json.dump(dados, file, ensure_ascii=False, indent=4)