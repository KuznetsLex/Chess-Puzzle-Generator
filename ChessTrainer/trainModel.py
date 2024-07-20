import joblib
import pandas as pd
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from xgboost import XGBRegressor

# Загрузка данных
data = pd.read_csv('chess_data.csv')

# Проверка и заполнение NaN значений в признаках
features = data[['first_line_percentage', 'second_line_percentage', 'third_line_percentage', 'bad_moves_percentage']]
features = features.fillna(features.median())  # заполняю Nan медианными значениями

targets = data['user_rating']

# Разделение данных на тренировочный и тестовый наборы
X_train, X_test, y_train, y_test = train_test_split(features, targets, test_size=0.2,
                                                    random_state=42)  # 20% - тестовая выборка, 80% - тренировочный набор

# Масштабирование данных
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Определение параметров для GridSearchCV
param_grid = {
    'n_estimators': [100, 200, 300],
    'max_depth': [3, 5, 7],
    'learning_rate': [0.01, 0.1, 0.2],
    'subsample': [0.7, 0.8, 1.0],
}

# Поиск наилучших параметров модели
grid_search = GridSearchCV(estimator=XGBRegressor(random_state=42), param_grid=param_grid,
                           scoring='neg_mean_absolute_error', cv=5,
                           n_jobs=-1)  # поиск по минимальной величине абсолютной ошибки
grid_search.fit(X_train_scaled, y_train)

# Наилучшая модель
best_model = grid_search.best_estimator_

# Оценка модели на тестовом наборе
y_pred = best_model.predict(X_test_scaled)
mae = mean_absolute_error(y_test, y_pred)
# print(f'Mean Absolute Error: {mae}')
# print(f'Best Parameters: {grid_search.best_params_}')

# Сохранение модели и scaler
joblib.dump(best_model, 'chess_rating_model.pkl')
joblib.dump(scaler, 'scaler.pkl')


# Функция для предсказания рейтинга пользователя
def predict_user_rating(first_line_percentage, second_line_percentage, third_line_percentage, bad_moves_percentage):
    input_data = pd.DataFrame({
        'first_line_percentage': [first_line_percentage],
        'second_line_percentage': [second_line_percentage],
        'third_line_percentage': [third_line_percentage],
        'bad_moves_percentage': [bad_moves_percentage]
    })
    input_data_scaled = scaler.transform(input_data)
    predicted_rating = best_model.predict(input_data_scaled)
    return predicted_rating[0]


# Пример использования функции для предсказания рейтинга пользователя (comment)
predicted_rating = predict_user_rating(75, 5, 15, 5)  # Predicted Rating - 1698
