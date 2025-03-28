import os
import shutil
from datetime import datetime
import tkinter as tk
from tkinter import filedialog, messagebox
import platform
from PIL import Image
from PIL.ExifTags import TAGS

def get_exif_creation_date(caminho_arquivo):
    try:
        image = Image.open(caminho_arquivo)
        exif_data = image._getexif()
        if exif_data:
            for tag, value in exif_data.items():
                tag_name = TAGS.get(tag, tag)
                if tag_name == "DateTimeOriginal":
                    return datetime.strptime(value, "%Y:%m:%d %H:%M:%S")
    except Exception as e:
        pass
    return None

def get_creation_time(caminho_arquivo):
    exif_date = get_exif_creation_date(caminho_arquivo)
    if exif_date:
        return exif_date
    
    if platform.system() == "Windows":
        return datetime.fromtimestamp(os.stat(caminho_arquivo).st_ctime)
    else:
        return datetime.fromtimestamp(os.path.getctime(caminho_arquivo))

def organizar_fotos(origem, destino):
    if not origem or not destino:
        messagebox.showerror("Erro", "Selecione os diretórios primeiro!")
        return
    
    os.makedirs(destino, exist_ok=True)
    
    for arquivo in os.listdir(origem):
        caminho_arquivo = os.path.join(origem, arquivo)
        
        if os.path.isfile(caminho_arquivo):  
            data_criacao = get_creation_time(caminho_arquivo)
            nome_pasta_data = data_criacao.strftime("%Y-%m-%d")
            caminho_pasta_destino = os.path.join(destino, nome_pasta_data)
            os.makedirs(caminho_pasta_destino, exist_ok=True)
            shutil.move(caminho_arquivo, os.path.join(caminho_pasta_destino, arquivo))
    
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
root.title("Organizador de Fotos por Data")

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


tk.Button(frame, text="Organizar", command=lambda: organizar_fotos(entry_origem.get(), entry_destino.get())).grid(row=2, column=1, pady=10)

root.mainloop()
