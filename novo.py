"""Exemplo inicial de um pequeno projeto de lista de tarefas."""

tarefas = ["Estudar Git", "Criar um repositório no GitHub"]


def mostrar_tarefas():
    print("Minhas tarefas:")
    for numero, tarefa in enumerate(tarefas, start=1):
        print(f"{numero}. {tarefa}")


if __name__ == "__main__":
    mostrar_tarefas()
