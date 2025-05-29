from flask import Flask, request, jsonify
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

productos = [
    {"id": 1, "nombre": "Destornillador estrella #2", "precio": 8700},
    {"id": 2, "nombre": "Alicate de 6 pulgadas", "precio": 11500},
    {"id": 3, "nombre": "Martillo", "precio": 7500}
]

class ProductoLista(Resource):
    def get(self):
        return jsonify({"productos":productos})

    def post(self):
        nuevo_producto = request.json
        nuevo_producto["id"] = len(productos) + 1
        productos.append(nuevo_producto)
        return jsonify({"Mensaje": "Producto agregado", "Producto": nuevo_producto})

class Producto(Resource):
    def get(self,id_producto):
        producto = next((p for p in productos if p["id"] == id_producto), None)
        if producto:
            return jsonify(producto)
        return jsonify({"mensaje" : "Producto no encontrado"})

    def put(self, id_producto):
        producto = next((p for p in productos if p["id"] == id_producto), None)
        if producto:
            datos = request.json
            producto.update(datos)
            return jsonify({"mensaje": "Producto actualizado","Producto": producto})
        return jsonify({"mensaje" : "Producto no encontrado"})
    
    def delete(self, id_producto):
        global productos
        productos = [p for p in productos if p["id"] != id_producto]
        return jsonify({"Mensaje": "Producto modificado"})

api.add_resource(ProductoLista, "/productos")
api.add_resource(Producto, "/productos/<int:id_producto>")

if __name__=="__main__":
    app.run(host="0.0.0.0",port=5090,debug=True)

