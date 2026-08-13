from app.dao.dao import DAO
from app.models.usuario import Usuario


class Usuario_DAO(DAO):

    def __init__(self, database, cidade_dao, perfil_dao):
        super().__init__(database)
        self._cidade_dao = cidade_dao
        self._perfil_dao = perfil_dao

    def save(self, usuario):

        conexao, cursor = self.conectar()

        try:

            sql = """
                    INSERT INTO USUARIO
                    (
                        NOME,
                        EMAIL,
                        DATA_NASCIMENTO,
                        CIDADE_ID,
                        PERFIL_ID
                    )
                    VALUES
                    (
                        %s,
                        %s,
                        %s,
                        %s,
                        %s
                    )
                  """

            cursor.execute(
                sql,
                (
                    usuario.nome,
                    usuario.email,
                    usuario.data_nascimento,
                    usuario.cidade.id,
                    usuario.perfil.id
                )
            )

            conexao.commit()

            usuario.id = cursor.lastrowid

            return usuario

        except Exception:
            conexao.rollback()
            raise

        finally:
            self.desconectar(cursor, conexao)

    def get_all(self):

        conexao, cursor = self.conectar()

        try:

            sql = """
                    SELECT
                        ID,
                        NOME,
                        EMAIL,
                        DATA_NASCIMENTO,
                        CIDADE_ID,
                        PERFIL_ID
                    FROM
                        USUARIO
                    ORDER BY
                        NOME
                  """

            cursor.execute(sql)

            registros = cursor.fetchall()

            usuarios = []

            for registro in registros:

                cidade = self._cidade_dao.get_by_id(
                    registro[4]
                )

                perfil = self._perfil_dao.get_by_id(
                    registro[5]
                )

                usuarios.append(

                    Usuario(
                        registro[0],
                        registro[1],
                        registro[2],
                        registro[3],
                        cidade,
                        perfil
                    )

                )

            return usuarios

        finally:
            self.desconectar(cursor, conexao)

    def get_by_id(self, id):

        conexao, cursor = self.conectar()

        try:

            sql = """
                    SELECT
                        ID,
                        NOME,
                        EMAIL,
                        DATA_NASCIMENTO,
                        CIDADE_ID,
                        PERFIL_ID
                    FROM
                        USUARIO
                    WHERE
                        ID = %s
                  """

            cursor.execute(sql, (id,))

            registro = cursor.fetchone()

            if registro is None:
                return None

            cidade = self._cidade_dao.get_by_id(
                registro[4]
            )

            perfil = self._perfil_dao.get_by_id(
                registro[5]
            )

            return Usuario(
                registro[0],
                registro[1],
                registro[2],
                registro[3],
                cidade,
                perfil
            )

        finally:
            self.desconectar(cursor, conexao)

    def update(self, usuario):

        conexao, cursor = self.conectar()

        try:

            sql = """
                    UPDATE USUARIO
                    SET
                        NOME = %s,
                        EMAIL = %s,
                        DATA_NASCIMENTO = %s,
                        CIDADE_ID = %s,
                        PERFIL_ID = %s
                    WHERE
                        ID = %s
                  """

            cursor.execute(
                sql,
                (
                    usuario.nome,
                    usuario.email,
                    usuario.data_nascimento,
                    usuario.cidade.id,
                    usuario.perfil.id,
                    usuario.id
                )
            )

            conexao.commit()

            return cursor.rowcount > 0

        except Exception:
            conexao.rollback()
            raise

        finally:
            self.desconectar(cursor, conexao)

    def delete(self, id):

        conexao, cursor = self.conectar()

        try:

            sql = """
                    DELETE
                    FROM USUARIO
                    WHERE
                        ID = %s
                  """

            cursor.execute(sql, (id,))

            conexao.commit()

            return cursor.rowcount > 0

        except Exception:
            conexao.rollback()
            raise

        finally:
            self.desconectar(cursor, conexao)