import tkinter as tk
from tkinter import messagebox, ttk

from app.models.cliente import Cliente


class Cliente_View:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.configurar_janela()
        self.criar_componentes()
        self.configurar_treeview()
        self.configurar_eventos()

    def configurar_janela(self):
        self.root.title("CRUD de Clientes")
        self.root.geometry("850x650")
        self.root.resizable(False, False)

    def criar_componentes(self):
        self.lbl_titulo = tk.Label(
            self.root,
            text="Cadastro de Clientes",
            font=("Arial", 16, "bold"),
        )
        self.lbl_titulo.grid(
            row=0,
            column=0,
            columnspan=2,
            padx=5,
            pady=5
        )
        self.frm_dados = tk.LabelFrame(
            self.root,
            text="Dados do cliente"
        )
        self.frm_dados.grid(
            row=1,
            column=0,
            columnspan=2,
            padx=10,
            pady=5,
            sticky="ew"
        )
        self.frm_dados.grid_columnconfigure(0, weight=0)
        self.frm_dados.grid_columnconfigure(1, weight=1)

        # ID
        self.lbl_id = tk.Label(
            self.frm_dados,
            text="ID:"
        )
        self.lbl_id.grid(
            row=0,
            column=0,
            padx=5,
            pady=5,
            sticky="w"
        )
        self.txt_id = tk.Entry(
            self.frm_dados,
            width=10,
            state="readonly"
        )
        self.txt_id.grid(
            row=0,
            column=1,
            padx=5,
            pady=5,
            sticky="w"
        )

        # Nome
        self.lbl_nome = tk.Label(
            self.frm_dados,
            text="Nome:"
        )
        self.lbl_nome.grid(
            row=1,
            column=0,
            padx=5,
            pady=5,
            sticky="w"
        )
        self.txt_nome = tk.Entry(
            self.frm_dados,
            width=35
        )
        self.txt_nome.grid(
            row=1,
            column=1,
            padx=5,
            pady=5,
            sticky="w"
        )

        # Data de Nascimento
        self.lbl_data_nascimento = tk.Label(
            self.frm_dados,
            text="Data Nascimento:"
        )
        self.lbl_data_nascimento.grid(
            row=2,
            column=0,
            padx=5,
            pady=5,
            sticky="w"
        )
        self.txt_data_nascimento = tk.Entry(
            self.frm_dados,
            width=15
        )
        self.txt_data_nascimento.grid(
            row=2,
            column=1,
            padx=5,
            pady=5,
            sticky="w"
        )

        # Limite de Crédito
        self.lbl_limite_credito = tk.Label(
            self.frm_dados,
            text="Limite Crédito:"
        )
        self.lbl_limite_credito.grid(
            row=3,
            column=0,
            padx=5,
            pady=5,
            sticky="w"
        )
        self.txt_limite_credito = tk.Entry(
            self.frm_dados,
            width=15
        )
        self.txt_limite_credito.grid(
            row=3,
            column=1,
            padx=5,
            pady=5,
            sticky="w"
        )

        # Cidade (Combobox para seleção da FK)
        self.lbl_cidade = tk.Label(
            self.frm_dados,
            text="Cidade:"
        )
        self.lbl_cidade.grid(
            row=4,
            column=0,
            padx=5,
            pady=5,
            sticky="w"
        )
        self.cb_cidade = ttk.Combobox(
            self.frm_dados,
            width=32,
            state="readonly"
        )
        self.cb_cidade.grid(
            row=4,
            column=1,
            padx=5,
            pady=5,
            sticky="w"
        )

        # Botões
        self.frm_botoes = tk.Frame(
            self.frm_dados,
            border=2,
            relief="groove"
        )
        self.frm_botoes.grid(
            row=5,
            column=0,
            padx=10,
            pady=5,
            columnspan=2,
        )
        self.btn_novo = tk.Button(
            self.frm_botoes,
            text="Novo",
            width=15
        )
        self.btn_novo.grid(
            row=0,
            column=0,
            padx=5,
            pady=5
        )
        self.btn_salvar = tk.Button(
            self.frm_botoes,
            text="Salvar",
            width=15
        )
        self.btn_salvar.grid(
            row=0,
            column=1,
            padx=5,
            pady=5
        )
        self.btn_alterar = tk.Button(
            self.frm_botoes,
            text="Alterar",
            width=15
        )
        self.btn_alterar.grid(
            row=0,
            column=2,
            padx=5,
            pady=5
        )
        self.btn_excluir = tk.Button(
            self.frm_botoes,
            text="Excluir",
            width=15
        )
        self.btn_excluir.grid(
            row=0,
            column=3,
            padx=5,
            pady=5
        )
        self.btn_fechar = tk.Button(
            self.frm_botoes,
            text="Fechar",
            width=15
        )
        self.btn_fechar.grid(
            row=0,
            column=4,
            padx=5,
            pady=5
        )

        # Tabela (Treeview)
        self.tbl_clientes = ttk.Treeview(
            self.root,
            height=10
        )
        self.tbl_clientes.grid(
            row=2,
            column=0,
            columnspan=2,
            padx=10,
            pady=10,
            sticky="nsew"
        )

    def configurar_treeview(self):
        self.tbl_clientes["columns"] = (
            "id",
            "nome",
            "data_nascimento",
            "limite_credito",
            "cidade"
        )
        self.tbl_clientes.column(
            "#0",
            width=0,
            stretch=False
        )
        self.tbl_clientes.column(
            "id",
            width=10,
            anchor="center"
        )
        self.tbl_clientes.column(
            "nome",
            width=40
        )
        self.tbl_clientes.column(
            "data_nascimento",
            width=25,
            anchor="center"
        )
        self.tbl_clientes.column(
            "limite_credito",
            width=25,
            anchor="e"
        )
        self.tbl_clientes.column(
            "cidade",
            width=30
        )

        self.tbl_clientes.heading(
            "id",
            text="ID"
        )
        self.tbl_clientes.heading(
            "nome",
            text="Nome"
        )
        self.tbl_clientes.heading(
            "data_nascimento",
            text="Data Nasc."
        )
        self.tbl_clientes.heading(
            "limite_credito",
            text="Limite Crédito"
        )
        self.tbl_clientes.heading(
            "cidade",
            text="Cidade"
        )

    def configurar_eventos(self):
        self.btn_novo.config(
            command=self.controller.new
        )
        self.btn_salvar.config(
            command=self.controller.save
        )
        self.btn_alterar.config(
            command=self.controller.update
        )
        self.btn_excluir.config(
            command=self.controller.delete
        )
        self.btn_fechar.config(
            command=self.fechar
        )
        self.tbl_clientes.bind(
            "<<TreeviewSelect>>",
            self.controller.selecionar_cliente
        )

    def preencher_campos(self, cliente):
        self.limpar_campos()
        self.txt_id.config(state="normal")
        self.txt_id.insert(
            0,
            str(cliente.id)
        )
        self.txt_id.config(state="readonly")

        nome_formatado = cliente.nome.title() if hasattr(cliente, 'nome') and cliente.nome else ""
        self.txt_nome.insert(
            0,
            nome_formatado
        )

        data_nasc = str(getattr(cliente, 'data_nascimento', ''))
        self.txt_data_nascimento.insert(
            0,
            data_nasc
        )

        limite = str(getattr(cliente, 'limite_credito', ''))
        self.txt_limite_credito.insert(
            0,
            limite
        )

        if hasattr(cliente, 'cidade') and cliente.cidade:
            cidade_str = getattr(cliente.cidade, 'nome', str(cliente.cidade))
            self.cb_cidade.set(cidade_str.title())

    def limpar_campos(self):
        self.txt_id.config(state="normal")
        self.txt_id.delete(0, tk.END)
        self.txt_id.config(state="readonly")
        self.txt_nome.delete(0, tk.END)
        self.txt_data_nascimento.delete(0, tk.END)
        self.txt_limite_credito.delete(0, tk.END)
        self.cb_cidade.set("")
        self.txt_nome.focus()

    def limpar_treeview(self):
        for item in self.tbl_clientes.get_children():
            self.tbl_clientes.delete(item)

    def get_id_selecionado(self):
        item = self.tbl_clientes.selection()[0]
        return self.tbl_clientes.item(item)["values"][0]

    def confirmar_exclusao(self):
        return messagebox.askyesno(
            "Confirmação",
            "Deseja realmente excluir este cliente?"
        )

    def ler_dados_cliente(self):
        nome = self.txt_nome.get()
        data_nascimento = self.txt_data_nascimento.get()
        limite_credito = self.txt_limite_credito.get()
        cidade = self.cb_cidade.get()
        return nome, data_nascimento, limite_credito, cidade

    def preencher_combobox_cidades(self, cidades):
        lista_cidades = [f"{c.id} - {c.nome.title()}" if hasattr(c, 'nome') else str(c) for c in cidades]
        self.cb_cidade['values'] = lista_cidades

    def exibir_mensagem(self, mensagem, sucesso=True):
        if sucesso:
            messagebox.showinfo(
                "Mini ERP",
                mensagem
            )
        else:
            messagebox.showerror(
                "Mini ERP",
                mensagem
            )

    def exibir_clientes(self, clientes):
        self.limpar_treeview()
        for cliente in clientes:
            nome_cidade = cliente.cidade.nome.title() if hasattr(cliente, 'cidade') and hasattr(cliente.cidade, 'nome') else str(getattr(cliente, 'cidade_id', ''))
            nome_formatado = cliente.nome.title() if hasattr(cliente, 'nome') and cliente.nome else ""
            data_nasc = getattr(cliente, 'data_nascimento', '')
            limite = getattr(cliente, 'limite_credito', '')

            self.tbl_clientes.insert(
                "",
                tk.END,
                values=(
                    cliente.id,
                    nome_formatado,
                    data_nasc,
                    limite,
                    nome_cidade
                )
            )

    def fechar(self):
        self.root.destroy()

    def iniciar(self):
        self.controller.get_all()
        self.root.mainloop()