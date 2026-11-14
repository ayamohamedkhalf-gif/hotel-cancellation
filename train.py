import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

current_dir = os.path.dirname(os.path.abspath(__file__))
df = pd.read_csv(os.path.join(current_dir, "hotel_bookings.csv"))

# أعمدة ثابتة واضحة للتدريب
features = ['lead_time', 'stays_in_week_nights', 'adults', 'required_car_parking_spaces', 'previous_cancellations', 'adr']
X = df[features].fillna(0)
y = df['is_canceled']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

joblib.dump(model, os.path.join(current_dir, 'hotel_model.pkl'))
print("تم التدريب والحفظ بنجاح!")