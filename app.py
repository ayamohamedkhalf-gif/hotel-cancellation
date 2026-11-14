import streamlit as st
import pandas as pd
import joblib

model = joblib.load('hotel_model.pkl')

st.title("🏨 Hotel Booking Cancellation Predictor")
st.write("أدخل تفاصيل الحجز لمعرفة احتمالية الإلغاء وسياسة العربون المقترحة.")

lead_time = st.number_input("مدة الانتظار (Lead Time)", min_value=0, max_value=500, value=30)
stay_nights = st.number_input("عدد ليالي الإقامة", min_value=1, max_value=30, value=3)
adults = st.number_input("عدد البالغين", min_value=1, max_value=10, value=2)
parking = st.selectbox("موقف سيارات (0: لا، 1: نعم)", [0, 1])
prev_canc = st.number_input("إلغاءات سابقة", min_value=0, max_value=20, value=0)
adr = st.number_input("متوسط سعر الليلة (ADR)", min_value=0.0, max_value=1000.0, value=100.0)

if st.button("توقع حالة الحجز"):
    input_data = pd.DataFrame([[lead_time, stay_nights, adults, parking, prev_canc, adr]], 
                              columns=['lead_time', 'stays_in_week_nights', 'adults', 'required_car_parking_spaces', 'previous_cancellations', 'adr'])
    
    prob = model.predict_proba(input_data)[0][1]
    st.subheader(f"نسبة احتمالية الإلغاء: {prob * 100:.2f}%")
    
    if prob > 0.7:
        st.error("⚠️ خطر إلغاء عالي! التوصية: فرض عربون كامل (Full Deposit).")
    elif prob > 0.4:
        st.warning("⚡ خطر إلغاء متوسط. التوصية: طلب عربون جزئي (Partial Deposit).")
    else:
        st.success("✅ الحجز آمن نسبياً. التوصية: بدون عربون (No Deposit).")