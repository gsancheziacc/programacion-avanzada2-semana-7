from src.repository.ClienteRepository import ObtenerClientes, CrearCliente, EliminarCliente

#CrearCliente("Juan", "Rodriguez", "2-7", "por allá")
EliminarCliente(4)

clientes = ObtenerClientes()
for i in range(len(clientes)):
    print(clientes[i].__str__())