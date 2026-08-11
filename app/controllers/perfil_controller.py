from app.models.perfil import Perfil

class Perfil_Controller:
    def __init__(self, dao, view):
        self.dao = dao
        self.view = view
        self.perfil_seleciona = None

    def new(self):
        self.view.limpar_campos()

    def save(self):
        try:
            nome, descricao = self.view.ler_dados_perfil()
            perfil = Perfil(
                None,
                nome,
                descricao
            )
            self.dao.save(perfil)
            self.get_all()
            self.view.exibir_mensagem("Perfil cadastrado com sucesso!")
        except ValueError as e:
            self.view.exibir_mensagem(f"Erro: {str(e)}", False)