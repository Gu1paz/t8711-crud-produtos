import os
from app.models.cidade import Cidade


class Cidade_Controller:
    def __init__(self, dao, estado_dao=None, view=None):
        self.dao = dao
        self.estado_dao = estado_dao
        self.view = view
        self.cidade_selecionada = None

    def carregar_estados(self):
        """Busca os estados no banco e popula a Combobox da View."""
        if self.estado_dao and self.view:
            estados = self.estado_dao.get_all()
            self.view.preencher_combobox_estados(estados)

    def _obter_estado_da_string(self, estado_str):
        """Extrai a entidade de Estado a partir do texto selecionado na Combobox."""
        if not estado_str:
            raise ValueError("Selecione um estado válido.")
        
        # Trata o formato "ID - SIGLA" da Combobox
        if " - " in estado_str:
            estado_id = int(estado_str.split(" - ")[0])
            if self.estado_dao:
                return self.estado_dao.get_by_id(estado_id)
                
        return estado_str

    def new(self):
        self.cidade_selecionada = None
        if self.view:
            self.view.limpar_campos()

    def save(self):
        try:
            nome, estado_str = self.view.ler_dados_cidade()
            
            if not nome or not estado_str:
                raise ValueError("Preencha todos os campos!")

            estado = self._obter_estado_da_string(estado_str)
            cidade = Cidade(None, nome, estado)
            
            self.dao.save(cidade)
            self.get_all()
            self.view.limpar_campos()
            self.cidade_selecionada = None
            self.view.exibir_mensagem("Cidade cadastrada com sucesso!")
            
        except ValueError as e:
            self.view.exibir_mensagem(f"Erro: {str(e)}", False)
        except Exception as e:
            self.view.exibir_mensagem(f"Erro ao salvar cidade: {str(e)}", False)

    def get_all(self):
        self.carregar_estados()
        cidades = self.dao.get_all()
        if self.view:
            self.view.exibir_cidades(cidades)

    def selecionar_cidade(self, event):
        try:
            id_cidade = self.view.get_id_selecionado()
            self.cidade_selecionada = self.dao.get_by_id(id_cidade)
            if self.cidade_selecionada and self.view:
                self.view.preencher_campos(self.cidade_selecionada)
        except (IndexError, Exception):
            pass

    def update(self):
        try:
            if self.cidade_selecionada is None:
                self.view.exibir_mensagem("Selecione uma cidade na lista.", False)
                return

            nome, estado_str = self.view.ler_dados_cidade()
            
            if not nome or not estado_str:
                raise ValueError("Preencha todos os campos!")

            estado = self._obter_estado_da_string(estado_str)

            if hasattr(self.cidade_selecionada, 'atualizar_dados'):
                self.cidade_selecionada.atualizar_dados(nome, estado)
            else:
                self.cidade_selecionada.nome = nome
                self.cidade_selecionada.estado = estado

            self.dao.update(self.cidade_selecionada)
            self.get_all()
            self.view.limpar_campos()
            self.cidade_selecionada = None
            self.view.exibir_mensagem("Cidade atualizada com sucesso!")

        except ValueError as e:
            self.view.exibir_mensagem(f"Erro: {str(e)}", False)
        except Exception as e:
            self.view.exibir_mensagem(f"Erro ao atualizar cidade: {str(e)}", False)

    def delete(self):
        if self.cidade_selecionada is None:
            self.view.exibir_mensagem("Selecione uma cidade na lista.", False)
            return

        if not self.view.confirmar_exclusao():
            return

        try:
            sucesso = self.dao.delete(self.cidade_selecionada.id)
            if sucesso:
                self.cidade_selecionada = None
                self.view.limpar_campos()
                self.get_all()
                self.view.exibir_mensagem("Cidade excluída com sucesso!")
            else:
                self.view.exibir_mensagem("Cidade não encontrada.", False)
        except Exception as e:
            self.view.exibir_mensagem(f"Problemas ao excluir cidade: {str(e)}", False)