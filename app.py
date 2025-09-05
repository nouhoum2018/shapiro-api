from flask import Flask, request, jsonify
from scipy.stats import shapiro

app = Flask(__name__)

@app.route('/shapiro', methods=['POST'])
def shapiro_test():
    try:
        # Récupération des données JSON envoyées
        data = request.get_json(force=True)
        residus = data.get('residus', [])

        # Vérification de la validité des données
        if not isinstance(residus, list) or len(residus) < 3:
            return jsonify({'error': 'La liste des résidus doit contenir au moins 3 valeurs'}), 400

        # Application du test de Shapiro-Wilk
        W, p_value = shapiro(residus)

        # Conversion en float natif pour éviter les problèmes de sérialisation numpy.float64
        return jsonify({
            'W': float(W),
            'p_value': float(p_value)
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    # En local -> http://127.0.0.1:5000/shapiro
    app.run(host='0.0.0.0', port=5000)
