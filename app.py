from flask import Flask, request, jsonify
from scipy.stats import shapiro

app = Flask(__name__)

@app.route('/shapiro', methods=['POST'])
def shapiro_test():
    data = request.get_json()
    residus = data.get('residus', [])

    if not isinstance(residus, list) or len(residus) < 3:
        return jsonify({'error': 'Liste invalide ou trop courte'}), 400

    W, p_value = shapiro(residus)
    return jsonify({'W': W, 'p_value': p_value})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)

