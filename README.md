
# Laptop Price Prediction

This project focuses on developing a machine learning-based web application that predicts laptop prices based on various technical specifications. The application provides users with an easy-to-use interface for understanding how different features affect laptop pricing, enabling informed decision-making for both buyers and sellers.

---

## Features

### 1. **Predictive Model**
- **Target Variable:** Laptop price category.
- **Input Features:**
  - RAM
  - Weight
  - Pixels Per Inch (PPI)
  - HDD Capacity
  - SSD Capacity
  - Flash Storage
  - Performance Score (Normalized)

### 2. **User-Friendly Interface**
- Interactive frontend developed using **HTML, CSS, and JavaScript** for a smooth user experience.
- Backend built with **Django**, ensuring robust server-side operations and seamless integration with the machine learning model.

### 3. **Database**
- **SQLite** database used to manage and store user inputs effectively.

### 4. **Technology-Driven Insights**
- Provides insights into how laptop specifications influence pricing trends.

---

## How It Works

1. Users input laptop specifications into the web application through a form.
2. The application processes the data and feeds it to a trained machine learning model.
3. The model predicts the laptop’s price category based on the input specifications.
4. The result is displayed to the user in an easily interpretable format.

---

## Technology Stack

### Frontend
- **HTML**, **CSS**, **JavaScript**

### Backend
- **Django** Framework

### Database
- **SQLite**

### Machine Learning
- Trained model utilizing relevant features for price prediction.

---

## Requirements for the Project

### Python
- Version: 3.10 or higher
- Compatible with modern libraries and tools.

### Django Framework
- Version: 4.x or higher
- Leverages features such as class-based views and enhanced ORM capabilities.

### Libraries
- **NumPy**: For numerical operations.
- **Pandas**: For data manipulation.
- **joblib**: For loading the serialized machine learning model.
- **scikit-learn**: For building and training the machine learning model.

### Front-End Libraries
- Optional: **Bootstrap 5.x** for responsive design.

### Deployment
- **Gunicorn**: For WSGI server.
- **WhiteNoise**: For serving static files in production.

---

## Steps to Run the Project

1. Clone the repository or download the project files.
2. Navigate to the project directory in your terminal:
   ```bash
   cd laptop_price_prediction
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run database migrations:
   ```bash
   python manage.py migrate
   ```
5. Start the development server:
   ```bash
   python manage.py runserver
   ```
6. Open your browser and visit `http://127.0.0.1:8000` to access the application.

---

## Future Enhancements

- Expand dataset to include additional laptop brands and features.
- Incorporate advanced machine learning techniques for improved accuracy.
- Add data visualization tools for better insights.
- Enable user authentication for personalized predictions.

---
