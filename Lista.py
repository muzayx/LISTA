import tkinter as tk

def adicionar_tarefa():
    tarefa = entry_tarefa.get()
    if tarefa:
        lista_tarefas.insert(tk.END, tarefa)
        entry_tarefa.delete(0, tk.END)

def remover_tarefa():
    try:
        selecao = lista_tarefas.curselection()[0]
        lista_tarefas.delete(selecao)
    except IndexError:
        pass

janela = tk.Tk()
janela.title("Lista de Tarefas")

# Ajusta o tamanho da janela
largura = 400
altura = 300
largura_tela = janela.winfo_screenwidth()
altura_tela = janela.winfo_screenheight()
posicao_x = (largura_tela - largura) // 2
posicao_y = (altura_tela - altura) // 2
janela.geometry(f"{largura}x{altura}+{posicao_x}+{posicao_y}")

entry_tarefa = tk.Entry(janela)
botao_adicionar = tk.Button(janela, text="Adicionar tarefa", command=adicionar_tarefa)
botao_remover = tk.Button(janela, text="Remover tarefa selecionada", command=remover_tarefa)
lista_tarefas = tk.Listbox(janela)

# Ajusta a aparência
entry_tarefa.pack(pady=10)
botao_adicionar.pack(pady=5)
botao_remover.pack(pady=5)
lista_tarefas.pack(expand=True, fill=tk.BOTH)

janela.mainloop()
