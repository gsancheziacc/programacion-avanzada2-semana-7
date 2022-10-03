from src.repository.conecction import getConnection, closeConnection
from src.model.Cliente import Cliente

# FUNCIÓN QUE PERMITE OBTENER LISTA DE CLIENTES
def ObtenerClientes():
    clientes = []
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nombre, apellido, rut, direccion FROM Cliente")
    for id, nombre, apellido, rut, direccion in cursor.fetchall():
        cliente = Cliente(id, nombre, apellido, rut, direccion)
        clientes.append(cliente)
    closeConnection(conn)
    return clientes

# FUNCIÓN QUE PERMITE CREAR UN CLIENTE
def CrearCliente(nombre, apellido, rut, direccion):
    conn = getConnection()
    cursor = conn.cursor()
    sql = "INSERT INTO CLIENTE (nombre, apellido, rut, direccion) VALUES (%s, %s, %s, %s)"
    data = (nombre, apellido, rut, direccion)
    cursor.execute(sql, data)
    conn.commit()
    closeConnection(conn)
    return True

# FUNCIÓN QUE PERMITE ELIMINAR UN CLIENTE
def EliminarCliente(id):
    conn = getConnection()
    cursor = conn.cursor()
    sql = "DELETE FROM CLIENTE WHERE ID = " + str(id)
    cursor.execute(sql)
    conn.commit()
    closeConnection(conn)
    return True

