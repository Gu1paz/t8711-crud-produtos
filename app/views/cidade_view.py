import tkinter as tk
from tkinter import messagebox, ttk

from app.models.cidade import Cidade


class Cidade_View:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.configurar_janela()
        self.criar_componentes()
        self.configurar_treeview()
        self.configurar_eventos()

    def configurar_janela(self):
        self.root.title("CRUD de Cidades")
        self.root.geometry("800x600")
        self.root.resizable(False, False)

    def criar_componentes(self):
        self.lbl_titulo = tk.Label(
            self.root,
            text="Cadastro de Cidades",
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
            text="Dados da cidade"
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
            text="Cidade:"
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
            width=30
        )
        self.txt_nome.grid(
            row=1,
            column=1,
            padx=5,
            pady=5,
            sticky="w"
        )

        # Estado (Combobox para seleção da FK)
        self.lbl_estado = tk.Label(
            self.frm_dados,
            text="Estado:"
        )
        self.lbl_estado.grid(
            row=2,
            column=0,
            padx=5,
            pady=5,
            sticky="w"
        )
        self.cb_estado = ttk.Combobox(
            self.frm_dados,
            width=27,
            state="readonly"
        )
        self.cb_estado.grid(
            row=2,
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
            row=3,
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
        self.tbl_cidades = ttk.Treeview(
            self.root,
            height=12
        )
        self.tbl_cidades.grid(
            row=2,
            column=0,
            columnspan=2,
            padx=10,
            pady=10,
            sticky="nsew"
        )

    def configurar_treeview(self):
        self.tbl_cidades["columns"] = (
            "id",
            "nome",
            "estado"
        )
        self.tbl_cidades.column(
            "#0",
            width=0,
            stretch=False
        )
        self.tbl_cidades.column(
            "id",
            width=10,
            anchor="center"
        )
        self.tbl_cidades.column(
            "nome",
            width=50
        )
        self.tbl_cidades.column(
            "estado",
            width=20
        )
        self.tbl_cidades.heading(
            "id",
            text="ID"
        )
        self.tbl_cidades.heading(
            "nome",
            text="Cidade"
        )
        self.tbl_cidades.heading(
            "estado",
            text="Estado"
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
        self.tbl_cidades.bind(
            "<<TreeviewSelect>>",
            self.controller.selecionar_cidade
        )

    def preencher_campos(self, cidade):
        self.limpar_campos()
        self.txt_id.config(state="normal")
        self.txt_id.insert(
            0,
            str(cidade.id)
        )
        self.txt_id.config(state="readonly")

        self.txt_nome.insert(
            0,
            cidade.nome
        )

        if hasattr(cidade, 'estado') and cidade.estado:
            sigla = getattr(cidade.estado, 'sigla', str(cidade.estado))
            self.cb_estado.set(sigla)

    def limpar_campos(self):
        self.txt_id.config(state="normal")
        self.txt_id.delete(0, tk.END)
        self.txt_id.config(state="readonly")
        self.txt_nome.delete(0, tk.END)
        self.cb_estado.set("")
        self.txt_nome.focus()

    def limpar_treeview(self):
        for item in self.tbl_cidades.get_children():
            self.tbl_cidades.delete(item)

    def get_id_selecionado(self):
        item = self.tbl_cidades.selection()[0]
        return self.tbl_cidades.item(item)["values"][0]

    def confirmar_exclusao(self):
        return messagebox.askyesno(
            "Confirmação",
            "Deseja realmente excluir esta cidade?"
        )

    def ler_dados_cidade(self):
        nome = self.txt_nome.get()
        estado = self.cb_estado.get()
        return nome, estado

    def preencher_combobox_estados(self, estados):
        lista_estados = [f"{e.id} - {e.sigla}" if hasattr(e, 'sigla') else str(e) for e in estados]
        self.cb_estado['values'] = lista_estados

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

    def exibir_cidades(self, cidades):
        self.limpar_treeview()
        for cidade in cidades:
            sigla_estado = cidade.estado.sigla if hasattr(cidade, 'estado') and hasattr(cidade.estado, 'sigla') else getattr(cidade, 'estado_id', '')
            self.tbl_cidades.insert(
                "",
                tk.END,
                values=(
                    cidade.id,
                    cidade.nome.title(),
                    sigla_estado.upper()
                )
            )

    def fechar(self):
        self.root.destroy()

    def iniciar(self):
        self.controller.get_all()
        self.root.mainloop()