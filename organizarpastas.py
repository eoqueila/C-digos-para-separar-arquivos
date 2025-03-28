import shutil
import os
from datetime import datetime
import tkinter as tk
from tkinter import filedialog, messagebox

def organizar_pastas(origem, destino):
    if not origem or not destino:
        messagebox.showerror("Erro", "Selecione os diretórios primeiro!")
        return
    
    os.makedirs(destino, exist_ok=True)
    
    for pasta in os.listdir(origem):
        caminho_pasta = os.path.join(origem, pasta)
        
        if os.path.isdir(caminho_pasta):
            data_criacao = datetime.fromtimestamp(os.path.getctime(caminho_pasta))
            nome_pasta_data = data_criacao.strftime("%Y-%m-%d")
            caminho_pasta_destino = os.path.join(destino, nome_pasta_data)
            os.makedirs(caminho_pasta_destino, exist_ok=True)
            shutil.move(caminho_pasta, os.path.join(caminho_pasta_destino, pasta))
    
    messagebox.showinfo("Concluído", "Organização finalizada com sucesso!")

def selecionar_origem():
    pasta = filedialog.askdirectory()
    entry_origem.delete(0, tk.END)
    entry_origem.insert(0, pasta)

def selecionar_destino():
    pasta = filedialog.askdirectory()
    entry_destino.delete(0, tk.END)
    entry_destino.insert(0, pasta)


root = tk.Tk()
root.title("Organizador de Pastas por Data")

frame = tk.Frame(root, padx=10, pady=10)
frame.pack(pady=20)


tk.Label(frame, text="Pasta de Origem:").grid(row=0, column=0, sticky="w")
entry_origem = tk.Entry(frame, width=50)
entry_origem.grid(row=0, column=1)
tk.Button(frame, text="Selecionar", command=selecionar_origem).grid(row=0, column=2)


tk.Label(frame, text="Pasta de Destino:").grid(row=1, column=0, sticky="w")
entry_destino = tk.Entry(frame, width=50)
entry_destino.grid(row=1, column=1)
tk.Button(frame, text="Selecionar", command=selecionar_destino).grid(row=1, column=2)


tk.Button(frame, text="Organizar", command=lambda: organizar_pastas(entry_origem.get(), entry_destino.get())).grid(row=2, column=1, pady=10)

root.mainloop()
