import streamlit as st
import pandas as pd
import joblib

# تحميل الموديل
model = joblib.load('hotel_model.pkl')

st.title("Hotel Cancellation Prediction App")

# إدخال البيانات من المستخدم
lead_time = st.number_input('Lead Time', min_value=0, max_value=1000, value=50)
stays_in_weekend_nights = st.number_input('Stays in Weekend Nights', min_value=0, max_value=20, value=1)
stays_in_week_nights = st.number_input('Stays in Week Nights', min_value=0, max_value=50, value=2)
adults = st.number_input('Adults', min_value=1, max_value=10, value=2)
children = st.number_input('Children', min_value=0, max_value=10, value=0)
is_repeated_guest = st.selectbox('Is Repeated Guest', [0, 1])
previous_cancellations = st.number_input('Previous Cancellations', min_value=0, max_value=20, value=0)
booking_changes = st.number_input('Booking Changes', min_value=0, max_value=20, value=0)
days_in_waiting_list = st.number_input('Days in Waiting List', min_value=0, max_value=100, value=0)
adr = st.number_input('ADR (Average Daily Rate)', min_value=0.0, max_value=5000.0, value=100.0)

if st.button('توقع حالة الحجز'):
    # تجهيز الداتا بنفس الأسماء والترتيب المظبوط
    input_data = pd.DataFrame([[
        lead_time, stays_in_weekend_nights, stays_in_week_nights, 
        adults, children, is_repeated_guest, previous_cancellations, 
        booking_changes, days_in_waiting_list, adr
    ]], columns=[
        'lead_time', 'stays_in_weekend_nights', 'stays_in_week_nights', 
        'adults', 'children', 'is_repeated_guest', 'previous_cancellations', 
        'booking_changes', 'days_in_waiting_list', 'adr'
    ])
    
    prediction = model.predict(input_data)[0]
    
    if prediction == 1:
        st.error('⚠️ تحذير: هذا الحجز مهدد بنسبة كبيرة للإلغاء!')
    else:
        st.success('✅ الحجز مؤكد وغالباً لن يتم إلغاؤه.')