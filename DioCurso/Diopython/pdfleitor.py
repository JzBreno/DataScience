import PyPDF2
import tkinter as tk
from tkinter import filedialog

# Função para ler o PDF
def ler_pdf():
    # Abrir janela de seleção de arquivo
    arquivo_path = filedialog.askopenfilename(filetypes=[("Arquivos PDF", "*.pdf")])
    if not arquivo_path:
        return
    
    # Abrir o arquivo PDF
    with open(arquivo_path, 'rb') as arquivo_pdf:
        # Criar um objeto PDFReader
        leitor_pdf = PyPDF2.PdfFileReader(arquivo_pdf)

        # Obter o número de páginas do PDF
        num_paginas = leitor_pdf.numPages

        # Iterar sobre as páginas e extrair o texto
        for pagina_num in range(num_paginas):
            pagina = leitor_pdf.getPage(pagina_num)
            texto = pagina.extractText()
            print(texto)

# Criar a janela principal
root = tk.Tk()
root.title("Selecionar Arquivo PDF")

# Botão para selecionar o arquivo PDF
btn_selecionar = tk.Button(root, text="Selecionar Arquivo PDF", command=ler_pdf)
btn_selecionar.pack(pady=10)

# Executar o loop de eventos
root.mainloop()
