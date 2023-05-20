


class Carro:
    def __init__(self, request):
        self.request=request 
        self.session=request.session
        carro= self.session.get("carro") #cada sesion tiene su carro

        if not carro:                                              #si la sesion no tiene carro entonces crea uno en forma de diccionario
            carro= self.session["carro"]= {}
                                                        # si la sesion tiene entonces lo usa
        self.carro= carro


    def agregar(self,producto): 
        if(str(producto.id) not in self.carro.keys()):                 #si el producto (id) no esta en el carrito agregalo
            self.carro[producto.id] = {
                "producto_id": producto.id,
                "nombre": producto.nombre,
                "precio": str(producto.precio),
                "cantidad": 1,
                "imagen": producto.imagen.url
            }                                                         # entonces agrega todo esto
        else:
            for key, value in self.carro.items():
                if key == str(producto.id):
                    value["cantidad"]= value["cantidad"]+1
                    value["precio"]= float(value["precio"])+ producto.precio
                    
                    break
        self.guardar_carro()

    def guardar_carro(self):
        self.session["carro"]= self.carro
        self.session.modified=True

    def eliminar_carrito(self, producto):
        producto.id= str(producto.id)
        if producto.id in self.carro:
            del self.carro[producto.id]
            self.guardar_carro()

            

    def restar_producto(self, producto):
        for key, value in self.carro.items():
                if key== str(producto.id):
                    value["cantidad"]= value["cantidad"]-1
                    value["precio"]= float(value["precio"])- producto.precio
                    if value["cantidad"] < 1:
                        self.eliminar_carrito(producto)
                    break
                
        self.guardar_carro()

    def limpiar_carrito(self):
        self.session["carro"] = {}
        self.session.modified=True

        
        