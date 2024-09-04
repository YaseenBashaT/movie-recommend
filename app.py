from flask import Flask, request, render_template, jsonify
import recommendation

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    title = request.form['title']
    recommendations = recommendation.recommend_movie(title)
    return render_template('index.html', results=recommendations)

@app.route('/suggest')
def suggest():
    query = request.args.get('query', '')
    suggestions = recommendation.get_suggestions(query)
    return jsonify({'suggestions': suggestions})

if __name__ == '__main__':
    app.run(debug=True)
