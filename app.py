from flask import Flask, request, jsonify, render_template
from model.stock_prediction import predict_stock_price
from model.sentiment_analysis import get_news_with_sentiment

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    stock_symbol = data['stock_symbol']
    prediction = predict_stock_price(stock_symbol)
    return jsonify(prediction=prediction)

@app.route('/sentiment', methods=['POST'])
def sentiment():
    data = request.get_json()
    text = data['text']
    sentiment_result = analyze_sentiment(text)
    return jsonify(sentiment=sentiment_result)

@app.route('/news', methods=['POST'])
def news():
    data = request.get_json()
    stock_symbol = data['stock_symbol']
    articles_with_sentiments = get_news_with_sentiment(stock_symbol)
    response = [{
        'title': article,
        'sentiment': sentiment[0]
    } for article, sentiment in articles_with_sentiments]
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
