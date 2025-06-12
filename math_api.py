from flask import Flask, request, jsonify
from sympy import symbols, sympify, diff, integrate
from sympy.abc import x  # símbolo común

app = Flask(__name__)

@app.route('/resolver', methods=['POST'])
def resolver():
    data = request.get_json()
    tipo = data.get('tipo')        # 'derivada' o 'integral'
    expresion = data.get('expresion')  # texto de la operación

    try:
        expr = sympify(expresion)
        if tipo == 'derivada':
            resultado = diff(expr, x)
        elif tipo == 'integral':
            resultado = integrate(expr, x)
        else:
            return jsonify({'error': 'Tipo no soportado'}), 400

        return jsonify({
            'original': str(expr),
            'resultado': str(resultado)
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
