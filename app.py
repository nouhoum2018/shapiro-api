from flask import Flask, request, jsonify
from scipy.stats import shapiro

app = Flask(__name__)

@app.route('/shapiro', methods=['POST'])
def shapiro_test():
    data = request.get_json()
    values = data.get('residus', [])

    if not isinstance(values, list) or len(values) < 3:
        return jsonify({'error': 'Liste de résidus invalide ou trop courte'}), 400

    W, p = shapiro(values)

    return jsonify({'W': W, 'p_value': p})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
