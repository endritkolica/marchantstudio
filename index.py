from flask import Flask, render_template, request, jsonify
from flask_assets import Environment, Bundle

app = Flask(__name__)
assets = Environment(app)

# Bundle and minify static assets
js = Bundle('js/main.js', output='gen/packed.js')
css = Bundle('css/style.css', output='gen/packed.css')
assets.register('js_all', js)
assets.register('css_all', css)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scroll_header', methods=['POST'])
def scroll_header():
    scroll_y = request.json.get('scrollY', 0)
    if scroll_y > 100:
        return jsonify({
            'background': 'rgba(255, 255, 255, 0.98)',
            'boxShadow': '0 2px 10px rgba(0, 0, 0, 0.1)'
        })
    return jsonify({
        'background': 'rgba(255, 255, 255, 0.95)', 
        'boxShadow': 'none'
    })

@app.route('/portfolio_hover', methods=['POST'])
def portfolio_hover():
    hover_state = request.json.get('hover')
    if hover_state:
        return jsonify({'transform': 'scale(1.05)'})
    return jsonify({'transform': 'scale(1)'})

@app.route('/hero_parallax', methods=['POST']) 
def hero_parallax():
    scroll_y = request.json.get('scrollY', 0)
    return jsonify({
        'backgroundPositionY': f'{scroll_y * 0.5}px'
    })

@app.route('/page_load')
def page_load():
    return jsonify({
        'opacity': '1',
        'transform': 'translateY(0)',
        'transition': 'all 1.5s ease'
    })

if __name__ == '__main__':
    app.run(debug=True)

