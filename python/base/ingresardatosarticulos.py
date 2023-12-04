

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
#------------------------------------------------------------------------------------------
    def agregar_articulo(self,id, descripcion, descripcion_red, precio, cat1,cat2,cat3,cat4,enoferta,foto):
        sql = "INSERT INTO articulos (id, descripcion, descripcion_red, precio, cat1,cat2,cat3,cat4,enoferta,foto)  VALUES (%s, %s,%s,%s, %s,%s,%s, %s,%s,%s)"
        valores = (id, descripcion, descripcion_red, precio, cat1,cat2,cat3,cat4,enoferta,foto)

        self.cursor.execute(sql, valores)
        self.conn.commit()
        return True

# -----------------------------------------------------------------------------------------------------
'''   def agregar_articulo(self,descripcion,descripcion_red,precio,cat1,cat2,cat3,cat4,enoferta,foto):
    #def agregar_articulo(self, id,descripcion,descripcion_red,precio):

        
        sql = "INSERT INTO articulos (descripcion, descripcion_red,precio,cat1,cat2,cat3,cat4,enoferta,foto) VALUES (%s, %s, %s, %s, %s,%s, %s, %s, %s)"
        #sql = "INSERT INTO articulos (id,descripcion, descripcion_red,precio) VALUES (%s,%s, %s, %s)"
        #valores = (id,descripcion, descripcion_red, precio)
        valores = (descripcion, descripcion_red, precio,cat1,cat2,cat3,cat4,enoferta,foto)
        self.cursor.execute(sql, valores)        
        self.conn.commit()
        return True
    '''
# Programa principal----------------------------------------------------------------------------------------------

#o_importador = Importador(host='localhost', user='root', password='', database='urbanmarket1')
o_importador = Importador(host='urbanmarket.mysql.pythonanywhere-services.com', user='urbanmarket', password='codoacodo1', database='urbanmarket$base')

#o_importador.agregar_articulo( "HARINA ESPECIAL MARUCA","HARINA MARUCA",45,5,5,5,5,True,"foto1.jg")
#o_importador.agregar_articulo(11, "HARINA ESPECIAL MARUCA","HARINA MARUCA",45.23)

o_importador.agregar_articulo(117, 'Mayonesa Clásica Hellmanns', 'Mayonesa Hellmanns', 850.00, 1, 13, 59, 96, 1, 'productos_1_1701200884.jpg')
o_importador.agregar_articulo(120, 'Detergente Cif Cremoso x 750 gr.', 'Cif Cremoso x750', 1500.00, 7, 54, 346, 613, 0, 'productos_2_1701441331.jpg')
o_importador.agregar_articulo(121, 'Aceite Cocinero x 1,5 lts', 'Cocinero x1,5lt', 900.00, 1, 2, 7, 7, 1, 'productos_3_1701441609.jpg')
o_importador.agregar_articulo(122, 'Ketchup Hellmanns x 500 grs.', 'Ketchup H x 500', 400.00, 1, 13, 23, 31, 0, 'productos_4_1701441806.jpg')
o_importador.agregar_articulo(123, 'Arroz Largo Fino Gallo x 500 grs', 'Arroz Gallox500', 600.00, 1, 8, 11, 16, 0, 'productos_5_1701441908.jpg')
o_importador.agregar_articulo(124, 'Shampoo 2x1 Pantene Pro-v x 700 ml.', 'Shampoo 2x1 Pantene', 1250.00, 11, 60, 402, 739, 1, 'productos_6_1701442069.jpg')
o_importador.agregar_articulo(125, 'Papel Higienico Scott x 30 mts', 'Papel Hig. Scott x30', 300.00, 7, 54, 344, 611, 0, 'productos_7_1701442226.jpg')
o_importador.agregar_articulo(126, 'Cacao Nesquik Bolsa x 800 grs', 'Cacao N. x800', 1500.00, 1, 22, 40, 59, 0, 'productos_8_1701442671.jpg')
o_importador.agregar_articulo(127, 'Gelatina Exquisita Frutilla x 40 grs.', 'Gelatina Ex. Frutilla x40', 220.00, 1, 23, 91, 150, 1, 'productos_9_1701443078.jpg')
o_importador.agregar_articulo(128, 'Bizcochuelo Exquisita  Coco x 540 grs', 'Bizcochuelo Ex. Cocox500', 950.00, 1, 5, 56, 90, 0, 'productos_10_1701443294.jpg')
o_importador.agregar_articulo(129, 'Mermelada La Campagnola BC damasco  x 390 grs', 'Mermelada Bc x390 grs.', 895.00, 1, 17, 45, 70, 1, 'productos_11_1701443417.jpg')
o_importador.agregar_articulo(130, 'Alimento para perros Dogui x 3 kgs.', 'Alimento perros Dogui x 3kg', 4000.00, 10, 51, 334, 553, 0, 'productos_12_1701443910.jpg')