#----------------------------------------------------------------------------------
# Instalar con pip install Flask
from flask import Flask, request, jsonify

# Instalar con pip install flask-cors
from flask_cors import CORS

# Instalar con pip install mysql-connector-python
import mysql.connector

# Si es necesario, pip install Werkzeug
from werkzeug.utils import secure_filename

# No es necesario instalar, es parte del sistema standard de Python
import os
import time
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
        self.cursor = self.conn.cursor(dictionary=True)

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

        return categorias3
    #-----------------------------------------------------------------------------------
    def consultar_categoria4(self,id3):      
        self.cursor.execute(f"SELECT * FROM cat4 where id3='{id3}'")
        categorias4 = self.cursor.fetchall() 
        return categorias4
    # -----------------------------------------------------------------------------------------------------
    def agregar_articulo(self,descripcion,descripcion_red,cat1,cat2,cat3,cat4,precio,enoferta,foto):
        sql = "INSERT INTO articulos (descripcion, descripcion_red,precio,cat1,cat2,cat3,cat4,enoferta,foto) VALUES (%s, %s, %s, %s, %s,%s, %s, %s, %s)"
        valores = (descripcion, descripcion_red, precio,cat1,cat2,cat3,cat4,enoferta,foto)
        self.cursor.execute(sql, valores)        
        self.conn.commit()
        return True
    # ----------------------------------------------------------------------------------------------------------
    def listar_articulos1(self):
        self.cursor.execute(f"SELECT id,descripcion FROM articulos where id <2000 ")
        articulos = self.cursor.fetchall() 
        return articulos
    # ----------------------------------------------------------------------------------------------------------
    def listar_articulos(self):
        #self.cursor.execute(f"SELECT id,descripcion,precio,cat1 FROM articulos where id <2000 ")
        #self.cursor.execute(f"select a.id, a.descripcion,precio,c1.descripcion as desc1,c2.descripcion as desc2
        #    from articulos as a , cat1 as c1,cat2 as c2
        #    where a.cat1 = c1.id and c2.id1 = c1.id")
        self.cursor.execute(f"select a.id as id, a.descripcion as descripcion,precio,c1.descripcion as ca1,c2.descripcion as ca2 from articulos as a , cat1 as c1,cat2 as c2 where a.cat1 = c1.id and c2.id1 = c1.id  and a.cat2= c2.id and a.cat1 =c1.id")
        articulos = self.cursor.fetchall() 
        return articulos

#   Programa Principal------------------------------------------------------------------
RUTA_DESTINO = './static/imagenes/'

#o_importador = Accesobase(host='urbanmarket.mysql.pythonanywhere-services.com', user='urbanmarket', password='codoacodo1', database='urbanmarket$base')
acceso_base = Accesobase(host='localhost', user='root', password='', database='urbanmarket1')



# Rutas flask ----------------------------------------------------------------

@app.route("/categorias/cat1", methods=["GET"])
def listar_categoria1():
    categoria1 = acceso_base.consultar_categoria1()
    return jsonify(categoria1)

@app.route("/categorias/cat2/<int:codigo>", methods=["GET"])
def listar_categoria2(codigo):
    categoria2 = acceso_base.consultar_categoria2(codigo)
    return jsonify(categoria2) 

@app.route("/categorias/cat3/<int:codigo>", methods=["GET"])
def listar_categoria3(codigo):
    categoria3 = acceso_base.consultar_categoria3(codigo)
    return jsonify(categoria3)

@app.route("/categorias/cat4/<int:codigo>", methods=["GET"])
def listar_categoria4(codigo):
    categoria4 = acceso_base.consultar_categoria4(codigo)
    return jsonify(categoria4)

@app.route("/articulos", methods=["GET"])
def listar_articulos():
    consulta_articulos = acceso_base.listar_articulos()
    return jsonify(consulta_articulos)

@app.route("/articulos1", methods=["GET"])
def listar_articulos1():
    consulta_articulos = acceso_base.listar_articulos1()
    return jsonify(consulta_articulos)

@app.route("/articulos", methods=["POST"])
def agregar_articulo():
    #Recojo los datos del form
    nombre_imagen=""
    descripcion = request.form['descripcion']
    descripcion_red = request.form['descripcion_red']
    cat1 = request.form['cat1']
    cat2 = request.form['cat2']
    cat3 = request.form['cat3']
    cat4 = request.form['cat4']
    precio = request.form['precio']
    oferta = request.form['oferta']
    imagen = request.files['imagen']
    # Genero el nombre de la imagen
    nombre_imagen = secure_filename(imagen.filename)
    nombre_base, extension = os.path.splitext(nombre_imagen)
    nombre_imagen = f"{nombre_base}_{int(time.time())}{extension}"
    

    if oferta == "true":
        oferta = True
    else: 
        oferta = False 

    if acceso_base.agregar_articulo( descripcion,descripcion_red,cat1,cat2,cat3,cat4, precio, oferta, nombre_imagen):
        imagen.save(os.path.join(RUTA_DESTINO, nombre_imagen))
        return jsonify({"mensaje": "Producto agregado"}), 201
    else:
        return jsonify({"mensaje": "Producto ya existe"}), 400


if __name__ == "__main__":
    app.run(debug=True)
