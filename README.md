# SMS-Spam-Detection with Flask

![SMS Spam Detection](https://github.com/Pramod858/SMS-Spam-Detection/assets/80105491/870c086f-3d4e-4e11-a085-aec3fc74d913)

This project implements a simple spam detection system using a Naive Bayes classifier and exposes it through a Flask web application. It includes Swagger documentation for easy testing.

## Getting Started

### Prerequisites

- [Docker](https://www.docker.com/) installed

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Pramod858/SMS-Spam-Detection.git
    ```

2. Change into the project directory:

    ```bash
    cd "SMS-Spam-Detection"
    ```

3. Build the Docker image:

    ```bash
    docker build -t spam_detection_app .
    ```
    ###or
   ```bash
    docker build -t spam_detection_app -f Dockerfile.txt .
    ```

5. Run the Docker container:

    ```bash
    docker run -p 5000:5000 spam_detection_app
    ```

The web application should now be accessible at [http://localhost:5000](http://localhost:5000).

## Usage

1. Open the web application in your browser.

2. Enter a text in the provided form and click "Predict" to see whether it's classified as spam or not.

3. Swagger documentation is available at [http://localhost:5000/apidocs/](http://localhost:5000/apidocs/) for testing the API endpoints.

## Customization

- You can modify the `app.py` file to include additional features, improve preprocessing, or enhance the model.

- Add your trained Naive Bayes model and CountVectorizer to the project.

## Acknowledgments

- [Flask](https://flask.palletsprojects.com/)
- [NLTK](https://www.nltk.org/)
- [Scikit-learn](https://scikit-learn.org/)
- [Flasgger](https://github.com/flasgger/flasgger)
