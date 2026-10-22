"""Mostra um resumo da situação das tarefas cadastradas."""

from novo import tarefas


def mostrar_resumo():
    total = len(tarefas)
    concluidas = sum(tarefa["concluida"] for tarefa in tarefas)
    print(f"Total de tarefas: {total}")
    print(f"Concluídas: {concluidas}")
    print(f"Pendentes: {total - concluidas}")


if __name__ == "__main__":
    mostrar_resumo()
