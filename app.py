from flask import Flask, render_template, request
import joblib

app = Flask(__name__)
model = joblib.load('weather_model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        input_features = [
            float(request.form['maxtempC']),
            float(request.form['mintempC']),
            float(request.form['cloudcover']),
            float(request.form['sunHour']),
            float(request.form['HeatIndexC']),
            float(request.form['precipMM']),
            float(request.form['pressure']),
        ]
        prediction = model.predict([input_features])[0]
        temperature = round(prediction[0], 2)
        humidity = round(prediction[1], 2)
        windspeed = round(prediction[2], 2)

        return render_template('result.html',
                               temperature=temperature,
                               humidity=humidity,
                               windspeed=windspeed)
    except Exception as e:
        return render_template('result.html', error=str(e))

# ✅ Blog route
@app.route('/blog')
def blog():
    return render_template('blog.html')

if __name__ == '__main__':
    app.run(debug=True)
