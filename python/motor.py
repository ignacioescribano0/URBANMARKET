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
        self.host =host
        self.user = user
        self.password=password
        self.database=database
        self.prepara_base()        
        # Intentamos seleccionar la base de datos
        try:
            self.cursor.execute(f"USE {database}")
        except mysql.connector.Error as err:
            raise err
        
        self.limpia_base()       
    #----------------------------------------------------------------
    def prepara_base(self):
        self.conexion = mysql.connector.connect(host=self.host,user=self.user,password=self.password)
        self.cursor = self.conexion.cursor(dictionary=True)
        try:
            self.cursor.execute(f"USE {self.database}")
        except mysql.connector.Error as err:
            raise err
    
    def limpia_base(self):
        self.cursor.close()
        self.conexion.close()
    #-----------------------------------------------------------------------------
    def consultar_categoria1(self): 
        self.prepara_base()    
        self.cursor.execute(f"SELECT * FROM cat1")
        categorias1 = self.cursor.fetchall() 
        self.limpia_base()
        return categorias1
    #----------------------------------------------------------------
    def consultar_categoria2(self,id1): 
        self.prepara_base()     
        self.cursor.execute(f"SELECT * FROM cat2 where id1='{id1}'")
        categorias2 = self.cursor.fetchall() 
        self.limpia_base()
        return categorias2
    #-------------------------------------------------------------------
    def consultar_categoria3(self,id2):
        self.prepara_base()   
        self.cursor.execute(f"SELECT * FROM cat3 where id2='{id2}'")
        categorias3 = self.cursor.fetchall() 
        self.limpia_base()
        return categorias3
    #-----------------------------------------------------------------------------------
    def consultar_categoria4(self,id3):      
        self.prepara_base()
        self.cursor.execute(f"SELECT * FROM cat4 where id3='{id3}'")
        categorias4 = self.cursor.fetchall() 
        self.limpia_base()
        return categorias4
    # -----------------------------------------------------------------------------------------------------
    def agregar_articulo(self,descripcion,descripcion_red,cat1,cat2,cat3,cat4,precio,enoferta,foto):
        self.prepara_base()
        sql = "INSERT INTO articulos (descripcion, descripcion_red,precio,cat1,cat2,cat3,cat4,enoferta,foto) VALUES (%s, %s, %s, %s, %s,%s, %s, %s, %s)"
        valores = (descripcion, descripcion_red, precio,cat1,cat2,cat3,cat4,enoferta,foto)
        self.cursor.execute(sql, valores)        
        self.conexion.commit()
        self.limpia_base()
        return True
    # ----------------------------------------------------------------------------------------------------------
    def listar_articulos1(self):
        self.prepara_base()
        self.cursor.execute(f"SELECT id,descripcion FROM articulos where id <2000 ")
        articulos = self.cursor.fetchall() 
        self.limpia_base()
        return articulos
    # ----------------------------------------------------------------------------------------------------------
    def listar_articulos(self):
        self.prepara_base()
        self.cursor.execute(f"select a.id as id, a.descripcion as descripcion,precio,c1.descripcion as ca1,c2.descripcion as ca2 from articulos as a , cat1 as c1,cat2 as c2 where a.cat1 = c1.id and c2.id1 = c1.id  and a.cat2= c2.id and a.cat1 =c1.id")
        articulos = self.cursor.fetchall() 
        self.limpia_base()
        return articulos
    # ----------------------------------------------------------------------------------------------------------
    def login(self,usuario,password):
        self.prepara_base()
        self.cursor.execute(f"select nombre from empleados where usuario='{usuario}' and password='{password}'")
        empleados = self.cursor.fetchall() 
        self.limpia_base()
        return empleados
    
    # ----------------------------------------------------------------------------------------------------------
    def listar_articulos_todos(self):
        self.prepara_base()
        self.cursor.execute("SELECT id,descripcion,precio,foto,enoferta FROM articulos")
        articulos = self.cursor.fetchall() 
        self.limpia_base()
        return articulos
    
     # -------------------------------------------------------------------------------------------------
    def listar_articulos_para_clientes_ofertas(self):
        self.prepara_base()
        self.cursor.execute("SELECT id,descripcion,precio,foto,enoferta FROM articulos where enoferta=1;")
        articulos = self.cursor.fetchall() 
        self.limpia_base()
        return articulos
    # ----------------------------------------------------------------------------------------------------------
    def listar_articulos_x_categoria(self,cat1,cat2,cat3,cat4):
        self.prepara_base()     
        self.cursor.execute(f"SELECT id,descripcion,precio,foto,enoferta FROM articulos where cat1='{cat1}' and cat2='{cat2}' and cat3='{cat3}' and cat4='{cat4}'")
                          
        articulos = self.cursor.fetchall() 
        self.limpia_base()
        return articulos
    #--------------------------------------------------------------------------------------------------------
    # ELIMINAR PRODUCTO----------------------------------------------------------------------------------------------------------
    def eliminar_articulos(self, id):
        self.prepara_base()
        self.cursor.execute(f"DELETE FROM articulos WHERE id = {id}")
        self.conexion.commit()
        return self.cursor.rowcount > 0

#   Programa Principal------------------------------------------------------------------
RUTA_DESTINO = './static/imagenes/'

#acceso_base = Accesobase(host='urbanmarket.mysql.pythonanywhere-services.com', user='urbanmarket', password='codoacodo1', database='urbanmarket$base')
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
    

@app.route("/login", methods=["POST"])
def login():
    usuario = request.form['usuario']
    contrasena = request.form['contrasena']
    consulta_empleados=acceso_base.login(usuario,contrasena)
    #print(f"{usuario} : {contrasena}")
    if len(consulta_empleados) > 0:
        return jsonify({"mensaje": "login exitoso"}), 201
    else:
         return jsonify({"mensaje": "No se encontro la combinacion usuario/password"}), 201
#-------------------------------------------------------------------------------------------    
@app.route("/articulos/clientes", methods=["GET"])
def listar_articulos_todos():
    consulta_articulos = acceso_base.listar_articulos_todos()
    return jsonify(consulta_articulos)
#-------------------------------------------------------------------------------------------    
@app.route("/articulos/ofertas", methods=["GET"])
def listar_articulos_para_clientes_ofertas():
    consulta_articulos_oferta = acceso_base.listar_articulos_para_clientes_ofertas()
    return jsonify(consulta_articulos_oferta)

#--------------------------------------------------------------------------------------------
@app.route("/articulos/categorias", methods=["POST"])
def listar_articulos_x_categoria():
    cat1 = request.form['cat1']
    cat2 = request.form['cat2']
    cat3 = request.form['cat3']
    cat4 = request.form['cat4']
    print(f"categoria 1:{cat1} categoria2:{cat2} categoria3:{cat3} categoria4:{cat4}")
    consulta_articulos_categoria = acceso_base.listar_articulos_x_categoria(cat1,cat2,cat3,cat4)
    return jsonify(consulta_articulos_categoria)
# DELETE eliminar producto -----------------------------------------------------------

@app.route("/articulos/<int:id>", methods=["DELETE"])
def eliminar_articulos(id):
    if acceso_base.eliminar_articulos(id):
        return jsonify({"mensaje": "Producto eliminado"}), 200
    else:
        return jsonify({"mensaje": "Producto no encontrado"}), 404

#-----------------------------------------------------------------------------

if __name__ == "__main__":
    app.run(debug=True)
