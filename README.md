# Post Quality Prediction Django Project

## Overview
This is a Django project that predicts the quality of a post for the **Mindplex.ai** platform. The prediction is based on two inputs:
- **User Reputation**
- **Interaction Delta (MPXR)**

---

## Features
- **Prediction Model**: Uses a pre-trained machine learning model to calculate the post quality score.
- **Web Interface**: Accepts input values and displays the predicted quality through a user-friendly form.

---

## Installation
1. Clone the repository and navigate to the project directory.
2. Set up a virtual environment and install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Place the `post_quality_model.joblib` file in the `predict` directory.
4. Run the server:
   ```bash
   python manage.py runserver
   ```
5. Access the app at `http://127.0.0.1:8000`.

---

## Usage
1. Open the web form in a browser.
2. Enter the following inputs:
   - **Reputation**: Numeric value for user reputation.
   - **MPXR**: Numeric value for interaction delta.
3. Submit the form to view the predicted post quality score.

---

## Files
- **`mdel.py`**: Contains the `PostQualityPredictor` class to load the model and make predictions.
- **`views.py`**: Processes user inputs and returns predictions.
- **`templates/predict.html`**: Provides the web interface for inputs and results.

---

## Example
1. Input:
   - Reputation: `150`
   - MPXR: `30`
2. Output: Predicted Quality: `92.4` (example result).
