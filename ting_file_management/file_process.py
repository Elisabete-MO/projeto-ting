from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    # Verifica se o arquivo já foi processado anteriormente
    for index in range(len(instance)):
        if path_file == instance.queue[index]["nome_do_arquivo"]:
            return None

    lines = txt_importer(path_file)

    processed_data = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(lines),
        "linhas_do_arquivo": lines
    }

    # Adiciona o dicionário à fila
    instance.enqueue(processed_data)

    print(processed_data, file=sys.stdout)


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
