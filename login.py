import psycopg
print (psycopg)

class Usuario:
    def __init__(self, login, senha):
        self.login = login
        self.senha = senha

#verifica se usuario recebido existe na base
def existe(usuario):
    # abrir uma conexao com PostgreSQL
    # obter uma abstracao do tipo cursor
    # executar um comando sql
    # verificar resultado
    # devolver True ou False
    
    with psycopg.connect(
        host="localhost",
        port=5432,
        dbname="20241_fatec_ipi_login_python",
        user="postgres",
        password="123456"
    ) as conexao:
      with conexao.cursor() as cursor:
        cursor.execute(
           'SELECT * FROM tb_usuario WHERE login=%s AND senha=%s',
           (usuario.login, usuario.senha)
        )  
        result = cursor.fetchone()
        #return #se result for igual a None, devolvo False , senao True 
        #return True if result != None else False
        return result != None
      

#def teste():
#   print(existe(Usuario('admin','admin')))    

#teste()    

def inserir(usuario):
   with psycopg.connect(
       host="localhost",
       port=5432,
       dbname="20241_fatec_ipi_login_python",
       user="postgres",
       password="123456"
    ) as conexao:
      with conexao.cursor() as cursor:
        cursor.execute(       
           'INSERT INTO tb_usuario (login, senha) VALUES (%s,%s)',
           (usuario.login, usuario.senha)
        )  
    
 

def menu():
   texto = '0-Sair\n1-login\n2-Logoff\n3-Inserir\n'
   usuario = None #ainda nao existe
   op = int(input(texto))
   while op != 0:
      if op == 1: 
         login = input('Digite login:')
         senha = input('Digite senha:')
         usuario = Usuario(login,senha)
         print("Usuario ok!" if existe(usuario) else "Usuario NOK" )              
      elif op == 2:
         usuario = None
         print('Logoff realizado com sucesso')
      elif op == 3:
         login = input('Digite login:')
         senha = input('Digite senha:')
         usuario = Usuario(login,senha)
         inserir(usuario)
      else: 
         print ("Jovem, somente valores validos")
      op = int(input(texto))

menu()
