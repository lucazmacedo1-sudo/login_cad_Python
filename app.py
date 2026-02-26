import customtkinter as ctk
from conexao import conectar

ctk.set_appearance_mode("dark")

janela = ctk.CTk()

janela.geometry("800x600")
janela.title("Sistema de login")

def cadastrar():
    email = email_entry.get()
    senha = senha_entry.get()

    conexao = conectar()
    cursor = conexao.cursor()

    sql = f"INSERT INTO usuarios (email, senha) VALUES (%s, %s)" 
    valores = (email,senha)
    
    cursor.execute(sql, (email, senha))

    conexao.commit()
    
    resultado.configure(text="Usuario Cadrastado!")

def login():
    email = email_entry.get()
    senha = senha_entry.get()

    conexao = conectar()
    cursor = conexao.cursor()

    sql = "SELECT * FROM usuarios WHERE email =%s AND senha =%s"
    cursor.execute(sql, (email,senha))

    usuario = cursor.fetchone()

    if usuario:
        resultado.configure(text="Login realizado!")

    else:
        resultado.configure(text="Email ou senha incorretos!")



#JANELA:
email_entry =ctk.CTkEntry(janela, placeholder_text="email")
email_entry.pack(pady=5)

senha_entry =ctk.CTkEntry(janela,placeholder_text="senha", show="*" )
senha_entry.pack(pady=5)

resultado =ctk.CTkLabel(janela, text="")
resultado.pack(pady=10)

botao_cadrastar = ctk.CTkButton(
    janela,text="Cadrastar",
    command=cadastrar
)
botao_cadrastar.pack(pady=5)

botao_login = ctk.CTkButton(
    janela,text="Login",
    command=login
)
botao_login.pack(pady=5)


janela.mainloop()
