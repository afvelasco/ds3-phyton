import unittest
import json 
from app import app

class TestMicroservicio(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.client = app.test_client()
    
    def test_1_get_productos(self):
        response = self.client.get("/productos")
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertIn("productos",data)
    
    def test_2_post_productos(self):
        nuevo_producto = {"nombre": "palustre","precio": 4900}
        response = self.client.post("/productos",json=nuevo_producto)
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data["Mensaje"], "Producto agregado")
        self.assertEqual(data["Producto"]["nombre"], "palustre")

    def test_3_get_un_producto(self):
        response = self.client.get("/productos/2")
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertIn("id", data)
        self.assertEqual(data["id"],2)
        
    def test_4_get_un_producto_no_exixtente(self):
        response = self.client.get("/productos/29")
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data["mensaje"], "Producto no encontrado")

    def test_5_put_producto(self):
        update_data = {"precio": 13700}
        response = self.client.put("/productos/1", json=update_data)
        self.assertEqual(response.status_code,200)
        data = json.loads(response.data)
        self.assertEqual(data["mensaje"], "Producto actualizado")
        self.assertEqual(data["Producto"]["precio"],13700)

    def test_6_put_un_producto_no_exixtente(self):
        response = self.client.put("/productos/27")
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data["mensaje"], "Producto no encontrado")

    def test_7_delete_producto(self):
        response = self.client.delete("/productos/1")
        self.assertEqual(response.status_code,200)
        data = json.loads(response.data)
        self.assertEqual(data["Mensaje"], "Producto eliminado")
        
if __name__=="__main__":
    unittest.main()
