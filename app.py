from flask import Flask, render_template, request, jsonify
from models.recommendation_engine import RecommendationEngine
from models.data_analyzer import DataAnalyzer
import config

app = Flask(__name__)
app.config.from_object(config.Config)

# Initialize components
recommendation_engine = RecommendationEngine()
data_analyzer = DataAnalyzer()

@app.route('/')
def dashboard():
    """Main dashboard page"""
    return render_template('dashboard.html')

@app.route('/recommendations')
def recommendations():
    """Recommendations page"""
    return render_template('recommendations.html')

@app.route('/api/recommendations', methods=['POST'])
def get_recommendations():
    """API endpoint to get recommendations"""
    try:
        data = request.get_json()
        recommendations = recommendation_engine.generate_recommendations(data)
        return jsonify({
            'success': True,
            'recommendations': recommendations
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/analysis', methods=['POST'])
def analyze_data():
    """API endpoint for data analysis"""
    try:
        data = request.get_json()
        analysis = data_analyzer.analyze(data)
        return jsonify({
            'success': True,
            'analysis': analysis
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

if __name__ == '__main__':
    app.run(debug=True)
