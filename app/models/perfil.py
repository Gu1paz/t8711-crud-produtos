class Perfil:
    def __init__(self, id, nome, descricao):
        self.id = id
        self.nome = nome
        self.descricao = descricao

    @property
    def id(self):
        return self._id
    
    @id.setter 
    def id(self, novo_id):
        self._id = novo_id

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome

    @property
    def descricao(self):
        return self._descricao
    
    @descricao.setter
    def descricao(self, novo_descricao):
        self._descricao = novo_descricao

    def atualizar_dados(self, novo_nome, novo_descricao):
        self._nome = novo_nome
        self._descricao = novo_descricao