

# Instalar con pip install mysql-connector-python
import mysql.connector


#--------------------------------------------------------------------
class Importador:
    #----------------------------------------------------------------
    # Constructor de la clase
    def __init__(self, host, user, password, database):
        # Primero, establecemos una conexión sin especificar la base de datos
        self.conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password
        )
        self.cursor = self.conn.cursor()

        # Intentamos seleccionar la base de datos
        try:
            self.cursor.execute(f"USE {database}")
        except mysql.connector.Error as err:
            # Si la base de datos no existe, la creamos
            if err.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
                self.cursor.execute(f"CREATE DATABASE {database}")
                self.conn.database = database
            else:
                raise err
                return err

# -----------------------------------------------------------------------------------------------------
    def agregar_articulo(self,descripcion,descripcion_red,precio,cat1,cat2,cat3,cat4,enoferta,foto):
    #def agregar_articulo(self, id,descripcion,descripcion_red,precio):

        
        sql = "INSERT INTO articulos (descripcion, descripcion_red,precio,cat1,cat2,cat3,cat4,enoferta,foto) VALUES (%s, %s, %s, %s, %s,%s, %s, %s, %s)"
        #sql = "INSERT INTO articulos (id,descripcion, descripcion_red,precio) VALUES (%s,%s, %s, %s)"
        #valores = (id,descripcion, descripcion_red, precio)
        valores = (descripcion, descripcion_red, precio,cat1,cat2,cat3,cat4,enoferta,foto)
        self.cursor.execute(sql, valores)        
        self.conn.commit()
        return True
    
# Programa principal----------------------------------------------------------------------------------------------

o_importador = Importador(host='localhost', user='root', password='', database='urbanmarket1')
#o_importador = Importador(host='urbanmarket.mysql.pythonanywhere-services.com', user='urbanmarket', password='codoacodo1', database='base')

o_importador.agregar_articulo( "HARINA ESPECIAL MARUCA","HARINA MARUCA",45,5,5,5,5,True,"foto1.jg")
#o_importador.agregar_articulo(11, "HARINA ESPECIAL MARUCA","HARINA MARUCA",45.23)

