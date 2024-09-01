import customtkinter as ctk
import random
import string

class GeradorSenhasApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Gerador de Senhas Aleatórias')
        self.root.geometry('400x350')
        self.root.resizable(False, False)

        # Configuração da interface
        self.configurar_interface()

    def configurar_interface(self):
        # Título do projeto
        label_titulo = ctk.CTkLabel(self.root, text='Gerador de Senhas Aleatórias', font=('Arial', 20))
        label_titulo.pack(pady=10)

        # Entrada para o comprimento da senha
        frame_comprimento = ctk.CTkFrame(self.root)
        frame_comprimento.pack(pady=10)
        label_comprimento = ctk.CTkLabel(frame_comprimento, text='Comprimento da senha:')
        label_comprimento.pack(side=ctk.LEFT, padx=5)
        self.entry_comprimento = ctk.CTkEntry(frame_comprimento, width=50)
        self.entry_comprimento.pack(side=ctk.LEFT, padx=5)

        # Checkboxes para selecionar os componentes da senha em duas colunas
        frame_opcoes = ctk.CTkFrame(self.root)
        frame_opcoes.pack(pady=10)

        self.checkbox_maiusculas = ctk.CTkCheckBox(frame_opcoes, text='Incluir Maiúsculas')
        self.checkbox_maiusculas.grid(row=0, column=0, padx=10, pady=5, sticky='w')
        self.checkbox_minusculas = ctk.CTkCheckBox(frame_opcoes, text='Incluir Minúsculas')
        self.checkbox_minusculas.grid(row=0, column=1, padx=10, pady=5, sticky='w')
        self.checkbox_numeros = ctk.CTkCheckBox(frame_opcoes, text='Incluir Números')
        self.checkbox_numeros.grid(row=1, column=0, padx=10, pady=5, sticky='w')
        self.checkbox_simbolos = ctk.CTkCheckBox(frame_opcoes, text='Incluir Símbolos')
        self.checkbox_simbolos.grid(row=1, column=1, padx=10, pady=5, sticky='w')

        # Botão para gerar a senha
        botao_gerar = ctk.CTkButton(self.root, text='Gerar Senha', command=self.gerar_senha)
        botao_gerar.pack(pady=10)

        # Alerta caso esqueça de digitar o comprimento da senha
        self.alerta = ctk.CTkLabel(self.root, text='', font=('Arial', 15))
        self.alerta.pack(pady=2)

        # Entrada para exibir a senha gerada
        self.entry_senha = ctk.CTkEntry(self.root, width=300, font=('Arial', 14))
        self.entry_senha.pack(pady=10)

    def gerar_senha(self):
        try:
            comprimento = int(self.entry_comprimento.get())
        except ValueError:
            comprimento = 0

        caracteres = ''
        self.alerta.configure(text='')
        self.entry_senha.delete(0, ctk.END)

        # concatena com caracteres todas as letras maiúsculas
        if self.checkbox_maiusculas.get() == 1:
            caracteres += string.ascii_uppercase
        # concatena com caracteres todas as letras minúsculas
        if self.checkbox_minusculas.get() == 1:
            caracteres += string.ascii_lowercase
        # concatena com caracteres todos os números
        if self.checkbox_numeros.get() == 1:
            caracteres += string.digits
        # concatena com caracteres todos os símbolos
        if self.checkbox_simbolos.get() == 1:
            caracteres += string.punctuation

        # Gera a senha apenas se houver caracteres selecionados e comprimento definido
        if caracteres and comprimento:
            # escolhe aleatoriamente uma quantidade(comprimento)
            # de caracteres na variável caracteres e os concatena na variável senha
            senha = ''.join(random.choice(caracteres) for _ in range(comprimento))
            self.entry_senha.delete(0, ctk.END)
            self.entry_senha.insert(0, senha)
        elif not caracteres:
            self.entry_senha.delete(0, ctk.END)
            self.entry_senha.insert(0, 'Selecione pelo menos uma opção')
        elif not comprimento:
            self.alerta.configure(text='Digite o comprimento da senha', text_color='red')

def main():
    ctk.set_appearance_mode('dark')
    ctk.set_default_color_theme('dark-blue')

    root = ctk.CTk()
    app = GeradorSenhasApp(root)
    root.mainloop()

if __name__ == '__main__':
    main()
