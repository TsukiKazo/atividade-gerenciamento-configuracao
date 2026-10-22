"""Lista de tarefas atualizada com o acompanhamento de conclusão."""

tarefas = [
    {"nome": "Estudar Git", "concluida": True},
    {"nome": "Criar um repositório no GitHub", "concluida": True},
    {"nome": "Publicar as alterações do projeto", "concluida": False},
]


def mostrar_tarefas():
    print("Minhas tarefas:")
    for numero, tarefa in enumerate(tarefas, start=1):
        status = "Concluída" if tarefa["concluida"] else "Pendente"
        print(f"{numero}. {tarefa['nome']} - {status}")


if __name__ == "__main__":
    mostrar_tarefas()
