import numpy as np
import tensorflow as tf
from newsapi import NewsApiClient
import os

# Initialize the NewsApiClient
newsapi = NewsApiClient(api_key=os.getenv('NEWSAPI_KEY'))

def get_company_news_titles(company_name):
    # Define parameters for the API request
    query_params = {
        'q': company_name,
        'language': 'en',
        'sort_by': 'publishedAt',
        'page_size': 25
    }
    # Make the API request
    news_data = newsapi.get_everything(**query_params)
    # Extract titles from the response
    titles = [article['title'] for article in news_data['articles']]
    return titles

# Load the saved model
reloaded_model = tf.keras.models.load_model('path_to_your_saved_model')

def analyze_news_titles(titles):
    # Calculate sigmoid values using the reloaded model
    reloaded_results = tf.sigmoid(reloaded_model(tf.constant(titles)))
    # Convert tensor to numpy array
    results = reloaded_results.numpy()
    return results

def get_news_with_sentiment(company_name):
    titles = get_company_news_titles(company_name)
    sentiments = analyze_news_titles(titles)
    return list(zip(titles, sentiments))
