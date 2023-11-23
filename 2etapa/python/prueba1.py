#----------------------------------------------------------------------------------
# Instalar con pip install Flask
from flask import Flask, request, jsonify

# Instalar con pip install flask-cors
from flask_cors import CORS

# Instalar con pip install mysql-connector-python
import mysql.connector
#----------------------------------------------------------------------------------

app = Flask(__name__)
CORS(app)  # Esto habilitará CORS para todas las rutas

#instancio un objeto coneccion con la base urbanmarket



#--------------------------------------------------------------------
class Accesobase:
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
            

        # Cerrar el cursor inicial y abrir uno nuevo con el parámetro dictionary=True
        self.cursor.close()
        #self.cursor = self.conn.cursor(dictionary=True)
    def obtiene_coneccion(self):
        return self.conn

class Categorias:
    #----------------------------------------------------------------
    # Constructor de la clase
    def __init__(self, acceso):
        self.cursor = acceso.cursor(dictionary=True)
    #----------------------------------------------------------------
    def consultar_categoria1(self):      
        self.cursor.execute(f"SELECT * FROM cat1")
        categorias1 = self.cursor.fetchall() 
        return categorias1
    #----------------------------------------------------------------
    def consultar_categoria2(self,id1):      
        self.cursor.execute(f"SELECT * FROM cat2 where id1='{id1}'")
        categorias2 = self.cursor.fetchall() 
        return categorias2
    #-------------------------------------------------------------------
    def consultar_categoria3(self,id2):      
        self.cursor.execute(f"SELECT * FROM cat3 where id2='{id2}'")
        categorias3 = self.cursor.fetchall() 
        #print()
        #print("-"*50)
        """"for categoria in categorias2:
           print(f"Codigo     : {categoria['id']}")
           print(f"Descripcion: {categoria['descripcion']}")
           print(f"Codigo     : {categoria['id']}")
           print("-"*50)     """

        return categorias3
    #-----------------------------------------------------------------------------------
    def consultar_categoria4(self,id3):      
        self.cursor.execute(f"SELECT * FROM cat4 where id3='{id3}'")
        categorias4 = self.cursor.fetchall() 
        #print()
        #print("-"*50)
        """"for categoria in categorias2:
           print(f"Codigo     : {categoria['id']}")
           print(f"Descripcion: {categoria['descripcion']}")
           print(f"Codigo     : {categoria['id']}")
           print("-"*50)     """

        return categorias4
    #------------------------------------------------------------------------------
class Articulos:
    # Constructor de la clase
    def __init__(self, acceso):
        self.cursor = acceso.cursor(dictionary=True)
    #---------------------------------------------------------------- 
    def listar(self,id1):
        self.cursor.execute(f"SELECT id,descripcion FROM articulos where cat1={id1}  and id <20000 ")
        articulos = self.cursor.fetchall() 
        return articulos


#   Programa Principal------------------------------------------------------------------
acceso_um = Accesobase(host='localhost', user='root', password='', database='urbanmarket')
categorias = Categorias(acceso_um.obtiene_coneccion())
articulos  = Articulos(acceso_um.obtiene_coneccion())


# Rutas flask ----------------------------------------------------------------

@app.route("/categorias/cat1", methods=["GET"])
def listar_categoria1():
    categoria1 = categorias.consultar_categoria1()
    return jsonify(categoria1)

@app.route("/categorias/cat2/<int:codigo>", methods=["GET"])
def listar_categoria2(codigo):
    categoria2 = categorias.consultar_categoria2(codigo)
    return jsonify(categoria2) 

@app.route("/categorias/cat3/<int:codigo>", methods=["GET"])
def listar_categoria3(codigo):
    categoria3 = categorias.consultar_categoria3(codigo)
    return jsonify(categoria3)

@app.route("/categorias/cat4/<int:codigo>", methods=["GET"])
def listar_categoria4(codigo):
    categoria4 = categorias.consultar_categoria4(codigo)
    return jsonify(categoria4)

@app.route("/articulos/<int:id1>", methods=["GET"])
def listar_articulos(id1):
    consulta_articulos = articulos.listar(id1)
    return jsonify(consulta_articulos)

if __name__ == "__main__":
    app.run(debug=True)
