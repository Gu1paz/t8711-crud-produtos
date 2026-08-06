from app.models.cliente import Cliente
from app.core.data_utils import Data_Utils


class Cliente_Controller:

    def __init__(self, dao, cidade_dao, estado_dao=None, view=None):
        self.dao = dao
        self.cidade_dao = cidade_dao
        self.estado_dao = estado_dao
        self.view = view

    def get_all(self):
        """Busca todos os clientes e cidades para popular a interface."""
        clientes = self.dao.get_all()
        cidades = self.cidade_dao.get_all()

        if self.view:
            self.view.exibir_clientes(clientes)
            self.view.preencher_combobox_cidades(cidades)

    def new(self):
        """Limpa os campos da tela para um novo cadastro."""
        if self.view:
            self.view.limpar_campos()

    def save(self):
        """Salva um novo cliente gravando os dados no banco."""
        try:
            nome, data_nascimento, limite_credito, cidade_str = (
                self.view.ler_dados_cliente()
            )

            # Validações básicas
            if not nome.strip():
                self.view.exibir_mensagem("Informe o nome do cliente.", False)
                return

            if not cidade_str:
                self.view.exibir_mensagem("Selecione uma cidade.", False)
                return

            # Extrai o ID da cidade selecionada na Combobox (Ex: "1 - Porto Alegre")
            id_cidade = int(cidade_str.split(" - ")[0])
            cidade = self.cidade_dao.get_by_id(id_cidade)

            if not cidade:
                self.view.exibir_mensagem("Cidade não encontrada.", False)
                return

            # Converte limite para float
            limite_val = float(limite_credito.replace(",", ".")) if limite_credito else 0.0

            # Converte string para objeto de data
            data_nasc_obj = Data_Utils.string_para_data(data_nascimento)

            cliente = Cliente(
                id=None,
                nome=nome,
                data_nascimento=data_nasc_obj,
                limite_credito=limite_val,
                cidade=cidade
            )

            self.dao.save(cliente)
            self.view.exibir_mensagem("Cliente cadastrado com sucesso!")
            self.get_all()
            self.view.limpar_campos()

        except ValueError as e:
            self.view.exibir_mensagem(f"Erro nos dados informados: {e}", False)
        except Exception as e:
            self.view.exibir_mensagem(f"Erro ao salvar cliente: {e}", False)

    def update(self):
        """Atualiza os dados de um cliente existente."""
        try:
            id_txt = self.view.txt_id.get()
            if not id_txt:
                self.view.exibir_mensagem(
                    "Selecione um cliente na tabela para alterar.", 
                    False
                )
                return

            id_cliente = int(id_txt)
            cliente_existente = self.dao.get_by_id(id_cliente)

            if not cliente_existente:
                self.view.exibir_mensagem("Cliente não encontrado.", False)
                return

            nome, data_nascimento, limite_credito, cidade_str = (
                self.view.ler_dados_cliente()
            )

            if not cidade_str:
                self.view.exibir_mensagem("Selecione uma cidade.", False)
                return

            # Se a string contiver ' - ', extrai apenas o ID
            if " - " in cidade_str:
                id_cidade = int(cidade_str.split(" - ")[0])
            else:
                id_cidade = cliente_existente.cidade.id

            cidade = self.cidade_dao.get_by_id(id_cidade)

            limite_val = float(limite_credito.replace(",", ".")) if limite_credito else 0.0
            data_nasc_obj = Data_Utils.string_para_data(data_nascimento)

            cliente_existente.atualizar_dados(
                nome,
                data_nasc_obj,
                limite_val,
                cidade
            )

            self.dao.update(cliente_existente)
            self.view.exibir_mensagem("Cliente atualizado com sucesso!")
            self.get_all()
            self.view.limpar_campos()

        except Exception as e:
            self.view.exibir_mensagem(f"Erro ao atualizar cliente: {e}", False)

    def delete(self):
        """Exclui o cliente selecionado."""
        try:
            id_cliente = self.view.get_id_selecionado()

            if self.view.confirmar_exclusao():
                if self.dao.delete(int(id_cliente)):
                    self.view.exibir_mensagem("Cliente excluído com sucesso!")
                    self.get_all()
                    self.view.limpar_campos()
                else:
                    self.view.exibir_mensagem("Erro ao excluir cliente.", False)

        except IndexError:
            self.view.exibir_mensagem(
                "Selecione um cliente na tabela para excluir.", 
                False
            )
        except Exception as e:
            self.view.exibir_mensagem(f"Erro ao excluir: {e}", False)

    def selecionar_cliente(self, event):
        """Evento acionado ao clicar em uma linha da tabela (Treeview)."""
        try:
            id_cliente = self.view.get_id_selecionado()
            cliente = self.dao.get_by_id(int(id_cliente))
            if cliente:
                self.view.preencher_campos(cliente)
        except Exception:
            pass