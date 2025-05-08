from flask import Flask, jsonify
import hashlib
import mysql.connector

programa = Flask(__name__)
miDB =mysql.connector.connect(host="localhost",
                              port=3306,
                              user="root",
                              password="",
                              db="ejemploms2")

@programa.route("/")
def index():
    return "Validación de Usuario"

@programa.route("/validar/<id>/<pas>")
def validar(id, pas):
    hash_pas = hashlib.sha512(pas.encode("utf-8")).hexdigest()
    micursor = miDB.cursor()
    sql = f"SELECT nombre FROM usuarios WHERE id_usuario='{id}' and contrasena='{hash_pas}'"
    micursor.execute(sql)
    resultado = micursor.fetchall()
    if len(resultado)==0:
        return jsonify({'valida': False, 'nombre': ''})
    else:
        return jsonify({'valida': True, 'nombre': resultado[0][0]})

if __name__=="__main__":
    programa.run(port=5101, host="0.0.0.0", debug=True)