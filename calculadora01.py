import tkinter as tk
from tkinter import messagebox

# Função para calcular a soma e exibir o resultado
def calcular_soma():
    try:
        # Obtém os valores digitados nos campos e converte para inteiros
        num1 = int(entry1.get())
        num2 = int(entry2.get())
        num3 = int(entry3.get())

        # Calcula a soma
        soma = num1 + num2 + num3

        # Verifica a soma e determina a mensagem
        if soma >= 50:
            mensagem = f"A soma é {soma}. A soma é grande!"
        elif 20 <= soma <= 49:
            mensagem = f"A soma é {soma}. A soma é moderada!"
        else:
            mensagem = f"A soma é {soma}. A soma é pequena!"

        # Exibe a mensagem em uma caixa de diálogo
        messagebox.showinfo("Resultado", mensagem)
    except ValueError:
        # Caso o usuário digite valores inválidos
        messagebox.showerror("Erro", "Por favor, insira apenas números inteiros!")

# Criação da janela principal
janela = tk.Tk()
janela.title("Calculadora de Soma")

# Labels e campos de entrada
tk.Label(janela, text="Digite o primeiro número:").grid(row=0, column=0, padx=10, pady=5)
entry1 = tk.Entry(janela)
entry1.grid(row=0, column=1, padx=10, pady=5)

tk.Label(janela, text="Digite o segundo número:").grid(row=1, column=0, padx=10, pady=5)
entry2 = tk.Entry(janela)
entry2.grid(row=1, column=1, padx=10, pady=5)

tk.Label(janela, text="Digite o terceiro número:").grid(row=2, column=0, padx=10, pady=5)
entry3 = tk.Entry(janela)
entry3.grid(row=2, column=1, padx=10, pady=5)

# Botão para calcular
botao_calcular = tk.Button(janela, text="Calcular", command=calcular_soma)
botao_calcular.grid(row=3, column=0, columnspan=2, pady=10)

# Inicia o loop da interface gráfica
janela.mainloop()
