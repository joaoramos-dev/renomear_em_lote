import sys
import os
import tkinter as tk
from tkinter import filedialog
import shutil

# Configuração do caminho do ícone
def obter_caminho_icone():
    if getattr(sys, "frozen", False):  # Quando rodando como .exe
        # Acessa diretamente o arquivo no _MEIPASS
        return os.path.join(sys._MEIPASS, "icons8-editar-arquivo-64.ico")
    else:  # Quando rodando como .py
        return "icons8-editar-arquivo-64.ico"

# Função para selecionar a pasta
def selecionar_pasta():
    global pasta
    pasta = filedialog.askdirectory(title="Selecione uma pasta")
    if pasta:
        label_caminho["text"] = f"Pasta selecionada: {pasta}"

# Função para renomear os arquivos
def renomear_arquivos():
    try:
        if not pasta:
            label_caminho["text"] = "Por favor, selecione uma pasta primeiro."
            return

        numero_inicial = int(entry_numero_inicial.get())
        tipo_arquivo = entry_tipo_arquivo.get().strip()

        if not tipo_arquivo:
            label_status["text"] = "Por favor, insira o tipo de arquivo (ex: .S-1010)."
            return

        contador = numero_inicial
        total_renomeados = 0
        for arquivo in os.listdir(pasta):
            if tipo_arquivo in arquivo:
                parte_antes, parte_depois = arquivo.split(tipo_arquivo, 1)
                novo_nome = f"{parte_antes[:-3]}{contador}{tipo_arquivo}{parte_depois}"

                caminho_antigo = os.path.join(pasta, arquivo)
                caminho_novo = os.path.join(pasta, novo_nome)

                os.rename(caminho_antigo, caminho_novo)
                contador += 1
                total_renomeados += 1

        label_status["text"] = f"Renomeação concluída! Total de arquivos renomeados: {total_renomeados}"
    except Exception as e:
        label_status["text"] = f"Erro: {e}"
        
        
        #Frontend em python

# Configuração da janela principal
janela = tk.Tk()
janela.title("Renomeador de Arquivos eSocial")
janela.geometry("500x300")

# Define o ícone da janela
janela.iconbitmap(obter_caminho_icone())

# Botão para selecionar a pasta
botao_selecionar = tk.Button(janela, text="Selecionar Pasta", command=selecionar_pasta)
botao_selecionar.pack(pady=10)

label_caminho = tk.Label(janela, text="Nenhuma pasta selecionada", wraplength=450)
label_caminho.pack(pady=10)

# Número inicial para a sequência
frame_numero_inicial = tk.Frame(janela)
frame_numero_inicial.pack(pady=10)
tk.Label(frame_numero_inicial, text="Número inicial:").pack(side="left", padx=10)
entry_numero_inicial = tk.Entry(frame_numero_inicial)
entry_numero_inicial.pack(side="left", padx=10)
entry_numero_inicial.insert(0, "101")

# Entrada do tipo de arquivo em comum que será alterado
frame_tipo_arquivo = tk.Frame(janela)
frame_tipo_arquivo.pack(pady=10)
tk.Label(frame_tipo_arquivo, text="Tipo de arquivo:").pack(side="left", padx=10)
entry_tipo_arquivo = tk.Entry(frame_tipo_arquivo)
entry_tipo_arquivo.pack(side="left", padx=10)
entry_tipo_arquivo.insert(0, ".S-1010")

# Botão para renomear os arquivos
botao_renomear = tk.Button(janela, text="Renomear Arquivos", command=renomear_arquivos)
botao_renomear.pack(pady=10)

label_status = tk.Label(janela, text="")
label_status.pack(pady=10)

janela.mainloop()
