from flask import Flask, render_template, request
from cesar_afin import cifrar, descifrar

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/procesar', methods=['POST'])
def procesar():
    mensaje = request.form['mensaje']
    alfabeto= request.form['alfabeto']
    clave_a = int(request.form['clave_a'])
    clave_b = int(request.form['clave_b'])
    accion = request.form['accion']
    
    if accion == 'cifrar':
        resultado = cifrar(mensaje, clave_a, clave_b, alfabeto)
    else:
        resultado = descifrar(mensaje, clave_a, clave_b, alfabeto)
    
    print(f"Mensaje: {mensaje}")
    print(f"Alfabeto: {alfabeto}")
    print(f"Clave (base, desplazamiento): {clave_a, clave_b}")
    print(f"Accion: {accion}")
    print(f"Resultado: {resultado}")
    
    response = f"<h2>Resultado:</h2><p>{resultado}</p>"

    return response

if __name__ == '__main__':
    app.run(debug=True)