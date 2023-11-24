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

    #----------------------------------------------------------------
    def agregar_tabla_cat1(self):
        try:    
            self.cursor.execute('''CREATE TABLE IF NOT EXISTS `cat1` (`id` int(5) NOT NULL,
                                `descripcion` varchar(70) NOT NULL,  PRIMARY KEY (`id`)) ''')
        except mysql.connector.Error as err:
            # Si tira error lo imprimos en pantalla
                raise err
                return err
        
        self.conn.commit()
    #---------------------------------------------------------------- 
    def agregar_tabla_cat2(self):
        try:    
            self.cursor.execute('''CREATE TABLE IF NOT EXISTS `cat2` (`id` int(5) NOT NULL,
                                `descripcion` varchar(70) NOT NULL,`id1` int(5) NOT NULL,PRIMARY KEY (`id`))  ''')
        except mysql.connector.Error as err:
            # Si tira error lo imprimos en pantalla
                raise err
                return err
        
        self.conn.commit()
            #---------------------------------------------------------------- 
    def agregar_tabla_cat3(self):
        try:    
            self.cursor.execute('''CREATE TABLE IF NOT EXISTS `cat3` (  `id` int(5) NOT NULL,
                                `descripcion` varchar(70) NOT NULL,`id2` int(5) NOT NULL,PRIMARY KEY (`id`))''')
        except mysql.connector.Error as err:
            # Si tira error lo imprimos en pantalla
                raise err
                return err
        
        self.conn.commit()
            #---------------------------------------------------------------- 

    def agregar_tabla_cat4(self):
        try:    
            self.cursor.execute('''CREATE TABLE IF NOT EXISTS `cat4` (`id` int(5) NOT NULL,
                                `descripcion` varchar(70) NOT NULL,`id3` int(5) NOT NULL,PRIMARY KEY (`id`))''')
        except mysql.connector.Error as err:
            # Si tira error lo imprimos en pantalla
                raise err
                return err
        
        self.conn.commit()
             #---------------------------------------------------------------- 

    def agregar_tabla_articulos(self):
        try:    
            self.cursor.execute('''CREATE TABLE IF NOT EXISTS `articulos` (  `id` int(6) NOT NULL AUTO_INCREMENT,
                            `descripcion` varchar(70) NOT NULL,`descripcion_red` varchar(40) NOT NULL,
                            `precio` decimal(10,2) NOT NULL,`cat1` int(5) DEFAULT NULL,`cat2` int(5) DEFAULT NULL,
                            `cat3` int(5) DEFAULT NULL,`cat4` int(5) DEFAULT NULL,`enoferta` tinyint(1) DEFAULT NULL,
                            `foto` varchar(30) DEFAULT NULL,PRIMARY KEY(`id`))''')
        except mysql.connector.Error as err:
            # Si tira error lo imprimos en pantalla
                raise err
                return err
        
        self.conn.commit()
        #---------------------------------------------------------------- 
    def agregar_tabla_clientes(self):
        try:    
            self.cursor.execute('''CREATE TABLE IF NOT EXISTS `clientes` (`id` int(6) NOT NULL AUTO_INCREMENT,
                                `nombre` varchar(70) NOT NULL,`usuario` varchar(20) NOT NULL,`password` varchar(20) NOT NULL,
                                PRIMARY KEY (`id`))''')
        except mysql.connector.Error as err:
            # Si tira error lo imprimos en pantalla
                raise err
                return err
        
        self.conn.commit()
         #---------------------------------------------------------------- 
    def agregar_tabla_cab_pedidos(self):
        try:    
            self.cursor.execute('''CREATE TABLE IF NOT EXISTS `cab_pedidos` (`id` int(7) NOT NULL,
                                `id_cliente` int(6) NOT NULL,`estado` varchar(15) NOT NULL,PRIMARY KEY (`id`))''')
        except mysql.connector.Error as err:
            # Si tira error lo imprimos en pantalla
                raise err
                return err
        
        self.conn.commit()
        #---------------------------------------------------------------- 
    def agregar_tabla_det_pedidos(self):
        try:    
            self.cursor.execute('''CREATE TABLE IF NOT EXISTS `det_pedidos` (  `id_articulo` int(6) NOT NULL,
                                `id_pedido` int(7) NOT NULL,`cantidad` decimal(10,3) NOT NULL,
                                `precio` decimal(10,2) NOT NULL,PRIMARY KEY (`id_articulo`,`id_pedido`))''')
        except mysql.connector.Error as err:
            # Si tira error lo imprimos en pantalla
                raise err
                return err
        
        self.conn.commit()
        #----------------------------------------------------------------
    def agregar_tabla_empleados(self):
        try:    
            self.cursor.execute('''CREATE TABLE IF NOT EXISTS `empleados` (`id` int(6) NOT NULL AUTO_INCREMENT,
                                `nombre` varchar(70) NOT NULL,`usuario` varchar(20) NOT NULL,`password` varchar(20) NOT NULL,
                                PRIMARY KEY (`id`))''')
        except mysql.connector.Error as err:
            # Si tira error lo imprimos en pantalla
                raise err
                return err
        
        self.conn.commit()

#--------------------------------------------------------------------
# Cuerpo del programa
#--------------------------------------------------------------------
# Crear una instancia de la clase Catalogo

o_importador = Importador(host='localhost', user='root', password='', database='urbanmarket1')
#o_importador = Importador(host='urbanmarket.mysql.pythonanywhere-services.com', user='urbanmarket', password='codoacodo1', database='base')


o_importador.agregar_tabla_cat1()
o_importador.agregar_tabla_cat2()
o_importador.agregar_tabla_cat3()
o_importador.agregar_tabla_cat4()
o_importador.agregar_tabla_articulos()
o_importador.agregar_tabla_clientes()
o_importador.agregar_tabla_cab_pedidos()
o_importador.agregar_tabla_det_pedidos()
o_importador.agregar_tabla_empleados()