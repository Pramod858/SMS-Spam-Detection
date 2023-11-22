import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

from flask import Flask, render_template, request
from flasgger import Swagger
import pickle
from sklearn.feature_extraction.text import CountVectorizer

app = Flask(__name__)
Swagger(app)

# Load the Naive Bayes model and CountVectorizer
with open('naive_bayes_model.pkl', 'rb') as model_file:
    loaded_nb_model = pickle.load(model_file)

with open('count_vectorizer.pkl', 'rb') as vectorizer_file:
    loaded_vectorizer = pickle.load(vectorizer_file)

# Preprocess function
def preprocess_text(text):
    # Lowercasing
    text = text.lower()

    # Remove Punctuation using re
    text = re.sub(r'[^\w\s]', '', text)

    # Tokenization
    tokens = word_tokenize(text)

    # Remove Stopwords
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words]

    # Lemmatization
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(word) for word in tokens]

    # Join tokens back into a text string
    text = ' '.join(tokens)

    return text

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    """
    Predict if the text is spam or not

    ---
    parameters:
      - name: new_text
        in: formData
        type: string
        required: true
        description: Enter the text to predict
    responses:
      200:
        description: The prediction result
    """
    if request.method == 'POST':
        new_text = request.form['new_text']

        # Preprocess the new text
        new_text_preprocessed = preprocess_text(new_text)

        # Vectorize the new text
        new_text_vectorized = loaded_vectorizer.transform([new_text_preprocessed])

        # Predict the label
        numeric_prediction = loaded_nb_model.predict(new_text_vectorized)

        # Map numeric prediction to human-readable label
        human_readable_label = 'Spam' if numeric_prediction[0] == 1 else 'Non-Spam'

        return render_template('index.html', prediction=f'Predicted Label: {human_readable_label}', new_text=new_text)


if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0', port=5000)
