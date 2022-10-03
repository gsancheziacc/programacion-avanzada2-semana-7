from src.repository.conecction import getConnection, closeConnection
from src.model.Empleado import Empleado

# FUNCIÓN QUE PERMITE OBTENER LISTA DE EMPLEADOS
def ObtenerEmpleados():
    clientes = []
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nombre, apellido, rut, direccion FROM EMPLEADO")
    for id, nombre, apellido, rut, direccion in cursor.fetchall():
        cliente = Empleado(id, nombre, apellido, rut, direccion)
        clientes.append(cliente)
    closeConnection(conn)
    return clientes

# FUNCIÓN QUE PERMITE CREAR UN EMPLEADO
def CrearEmpleado(nombre, apellido, rut, direccion):
    conn = getConnection()
    cursor = conn.cursor()
    sql = "INSERT INTO EMPLEADO (nombre, apellido, rut, direccion) VALUES (%s, %s, %s, %s)"
    data = (nombre, apellido, rut, direccion)
    cursor.execute(sql, data)
    conn.commit()
    closeConnection(conn)
    return True

# FUNCIÓN QUE PERMITE ELIMINAR UN EMPLEADO
def EliminarEmpleado(id):
    conn = getConnection()
    cursor = conn.cursor()
    sql = "DELETE FROM EMPLEADO WHERE ID = " + str(id)
    cursor.execute(sql)
    conn.commit()
    closeConnection(conn)
    return True
