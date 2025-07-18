# 💎 Diamond Price Prediction

This project predicts the price of diamonds based on their physical and quality characteristics using various machine learning regression models. The goal is to determine which model best estimates diamond prices using historical data.

## 📂 Project Structure

- `Diamond_price_Prediction.ipynb`: Jupyter Notebook containing data preprocessing, model training, and evaluation.
- `main.py`: Flask app for backend prediction.
- `templates/index.html`: Web interface for user input and prediction display.
- `model.pkl`: Trained XGBoost model.

## 📊 Dataset Features

The dataset contains the following features used to predict the diamond price:

- `carat`: Weight of the diamond
- `cut`: Quality of the cut (Fair, Good, Very Good, Premium, Ideal)
- `color`: Diamond color (D [best] to J [worst])
- `clarity`: Measure of diamond clarity (I1, SI2, SI1, VS2, VS1, VVS2, VVS1, IF)
- `depth`: Total depth percentage
- `table`: Width of the top of the diamond
- `x`: Length in mm
- `y`: Width in mm
- `z`: Depth in mm

## 🧪 Machine Learning Models & Results

| Model         | RMSE     | MAE     | R² Score    |
|---------------|----------|---------|-------------|
| LinearRegression | 1014.63 | 675.07  | 93.63%      |
| Lasso         | 1014.66 | 676.24  | 93.63%      |
| Ridge         | 1014.63 | 675.11  | 93.63%      |
| ElasticNet    | 1533.36 | 1060.95 | 85.45%      |
| XGBoost ✅     | 587.81  | 297.16  | **97.86%**  |

> 🔥 **XGBoost** was the best-performing model with the highest R² score. It has been saved and deployed in the web app.

## 🌐 Web App

Built using **Flask**, the web app allows users to input diamond features and get real-time price predictions using the trained XGBoost model.

### 🚀 How to Run

```bash
# Install required libraries
pip install -r .\requirements.txt

# Run the Flask app
python main.py
```

# 📈 Future Improvements
Integrate real-time market pricing APIs

Add user login and history tracking

Deploy on cloud (Heroku, Vercel, etc.)


## 📄 License

This project is licensed under the MIT License.

---
**Made ❤️ by Brijesh Rakhasiya**

