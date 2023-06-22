from ting_file_management.priority_queue import PriorityQueue
import pytest


def test_basic_priority_queueing():
    test_enqueue_priority()
    test_dequeue_priority()
    test_search_priority()


def test_enqueue_priority():
    queue = PriorityQueue()
    file1 = {
        "nome_do_arquivo": "arquivo1.txt",
        "qtd_linhas": 3,
        "linhas_do_arquivo": [],
    }
    file2 = {
        "nome_do_arquivo": "arquivo2.txt",
        "qtd_linhas": 6,
        "linhas_do_arquivo": [],
    }
    file3 = {
        "nome_do_arquivo": "arquivo3.txt",
        "qtd_linhas": 2,
        "linhas_do_arquivo": [],
    }

    queue.enqueue(file1)
    queue.enqueue(file2)
    queue.enqueue(file3)

    assert len(queue) == 3

    removed_file = queue.dequeue()
    assert removed_file == file1

    removed_file = queue.dequeue()
    assert removed_file == file3

    removed_file = queue.dequeue()
    assert removed_file == file2


def test_dequeue_priority():
    queue = PriorityQueue()
    file1 = {
        "nome_do_arquivo": "arquivo1.txt",
        "qtd_linhas": 3,
        "linhas_do_arquivo": [],
    }
    file2 = {
        "nome_do_arquivo": "arquivo2.txt",
        "qtd_linhas": 6,
        "linhas_do_arquivo": [],
    }
    file3 = {
        "nome_do_arquivo": "arquivo3.txt",
        "qtd_linhas": 2,
        "linhas_do_arquivo": [],
    }

    with pytest.raises(IndexError, match="A fila está vazia."):
        queue.dequeue()

    queue.enqueue(file1)
    queue.enqueue(file2)
    queue.enqueue(file3)

    removed_file = queue.dequeue()
    assert removed_file == file1
    assert len(queue) == 2

    removed_file = queue.dequeue()
    assert removed_file == file3
    assert len(queue) == 1

    removed_file = queue.dequeue()
    assert removed_file == file2
    assert len(queue) == 0


def test_search_priority():
    queue = PriorityQueue()

    with pytest.raises(IndexError, match="Índice Inválido ou Inexistente"):
        queue.search(0)

    file1 = {
        "nome_do_arquivo": "arquivo1.txt",
        "qtd_linhas": 3,
        "linhas_do_arquivo": [],
    }
    file2 = {
        "nome_do_arquivo": "arquivo2.txt",
        "qtd_linhas": 6,
        "linhas_do_arquivo": [],
    }
    file3 = {
        "nome_do_arquivo": "arquivo3.txt",
        "qtd_linhas": 2,
        "linhas_do_arquivo": [],
    }

    queue.enqueue(file1)
    queue.enqueue(file2)
    queue.enqueue(file3)

    assert queue.search(0) == file1
    assert queue.search(1) == file3
    assert queue.search(2) == file2
