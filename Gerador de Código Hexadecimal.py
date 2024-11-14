import tkinter as tk
from tkinter import messagebox
import random

# Função para gerar um código hexadecimal aleatório
def gen_hex_code():
    hex_code = "#" + "".join(random.choice("0123456789abcdef") for _ in range(6))
    output_entry.config(state="normal")  # Habilita a edição para inserir o código
    output_entry.delete(0, tk.END)  # Limpa o campo de entrada
    output_entry.insert(0, hex_code)  # Insere o código hexadecimal
    output_entry.config(state="readonly")  # Bloqueia novamente o campo de entrada
    output_color.config(bg=hex_code)  # Atualiza a cor do display

# Função para copiar o código hexadecimal
def copy_hex_code():
    hex_code = output_entry.get()  # Pega o valor atual do campo de entrada
    if hex_code:  # Verifica se há um código a ser copiado
        root.clipboard_clear()
        root.clipboard_append(hex_code)
        messagebox.showinfo("Hexadecimal Copiado", f"Código {hex_code} copiado para a área de transferência.")

# Configurações principais da janela
root = tk.Tk()
root.title("Gerador de Código Hexadecimal")
root.geometry("400x500")
root.configure(bg="#121317")
root.resizable(False, False)

# Container para a exibição da cor gerada
output_color = tk.Frame(root, bg="#ffffff", width=200, height=200, bd=5, relief="solid")
output_color.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

# Campo de texto para exibir o código hexadecimal
output_entry = tk.Entry(root, font=("Roboto Mono", 16), justify="center", width=15, bd=2, state="readonly")
output_entry.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

# Botões de gerar e copiar
button_frame = tk.Frame(root, bg="#121317")
button_frame.place(relx=0.5, rely=0.75, anchor=tk.CENTER)

gen_btn = tk.Button(button_frame, text="Gerar", font=("Roboto Mono", 12, "bold"), bg="#18f98f", fg="#202229", padx=10, command=gen_hex_code)
gen_btn.grid(row=0, column=0, padx=10, pady=10)

copy_btn = tk.Button(button_frame, text="Copiar", font=("Roboto Mono", 12, "bold"), bg="#202229", fg="#18f98f", padx=10, command=copy_hex_code)
copy_btn.grid(row=0, column=1, padx=10, pady=10)

# Gera o primeiro código hexadecimal ao iniciar
gen_hex_code()

# Inicia o loop da interface gráfica
root.mainloop()
