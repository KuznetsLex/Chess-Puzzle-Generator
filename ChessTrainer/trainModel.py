import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import joblib

# Загрузка данных
data = pd.read_csv('chess_data.csv')

# Разделение на признаки и целевую переменную
X = data[['first_line_percentage', 'second_line_percentage', 'third_line_percentage', 'bad_moves_percentage']]
y = data['user_rating']

# Разделение на обучающую и тестовую выборки
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Стандартизация данных
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Создание и обучение модели
model = LinearRegression()
model.fit(X_train, y_train)

# Предсказания на тестовой выборке
y_pred = model.predict(X_test)

# Оценка модели
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error: {mse}")
print(f"R^2 Score: {r2}")

# Сохранение модели и масштабировщика
joblib.dump(model, 'chess_rating_predictor.pkl')
joblib.dump(scaler, 'scaler.pkl')
