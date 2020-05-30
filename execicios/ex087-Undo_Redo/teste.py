"""
Faca uma lista de tarefa com as seguintes opções:
- adicionar tarefa
- listar tarefa
- opção de desfazer ( a cada vez que chamamos, desfaz a última ação )
- opção de refazeer ( a cada vez que chamamos, refaz a ultima ação. )

ex.:
['tarefa 1'], ['tarefa 2]
['tarefa 1'] <- Desfazer
['tarefa 1'], ['Tarefa 2'] <- Refazer

input <- Nova tarefa
"""
def show_op(todo_list):
    print()
    print('Tarefas: ')
    print(todo_list)
    print()

def  do_add(todo, todo_list):
    todo_list.append(todo)

def do_undo(todo_list,redo_list):

    if not todo_list:
        print('Nada a desfazer.')
        return

    last_todo = todo_list.pop()
    redo_list.append(last_todo)

def do_redo(todo_list,redo_list):
    if not redo_list:
        print('Nada a refazer.')
        return

    last_redo = redo_list.pop()
    todo_list.append(last_redo)

if __name__ == "__main__":
    todo_list = []
    redo_list = list()

    while True:
        todo = input('Digite uma tarefa ou undo, redo lst: ')

        if todo == 'ls':
            show_op(todo_list)
            continue
        elif todo == 'undo':
            do_undo(todo_list, redo_list)
            continue
        elif todo == 'redo':
            do_redo(todo_list, redo_list)
            continue

        
        do_add(todo, todo_list)


