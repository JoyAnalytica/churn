import streamlit as mode_app
import pickle
import numpy as np

# ১. মডেল লোড করা
filename = 'savedmodel.sav'
try:
    load_model = pickle.load(open(filename, 'rb'))
except FileNotFoundError:
    mode_app.error(f"❌ '{filename}' ফাইলটি পাওয়া যায়নি!")

# ২. ওয়েব অ্যাপের ইন্টারফেস/ডিজাইন তৈরি করা
mode_app.title("📊 Customer Churn Prediction Web App")
mode_app.write("গ্রাহকের প্রয়োজনীয় তথ্য ইনপুট দিন এবং তিনি Churn করবেন কি না তা প্রেডিক্ট করুন।")

mode_app.subheader("গ্রাহকের তথ্যসমূহ (Input Features):")

# আপনার কলাম অনুযায়ী ইনপুট বক্স ও ড্রপডাউন
age = mode_app.number_input("👤 Age (বয়স)", min_value=1, max_value=120, value=40)
monthly_charges = mode_app.number_input("💰 Monthly Charges (মাসিক বিল)", min_value=0.0, value=60.0)
tenure_months = mode_app.number_input("⏳ Tenure Months (কত মাস ধরে আছেন)", min_value=0, value=12)

# Num_Products এর জন্য সুন্দর ড্রপডাউন (Dropdown Menu)
num_products = mode_app.selectbox("📦 Num Products (কয়টি প্রোডাক্ট ব্যবহার করছেন)", options=[1, 2, 3, 4], index=0)

# ৩. প্রেডিকশন বাটন তৈরি
if mode_app.button("🔮 Predict Churn"):
    # ইনপুট ডেটাকে সঠিক ক্রমানুসারে মডেলের জন্য সাজানো: [Age, Monthly_Charges, Tenure_Months, Num_Products]
    user_input = np.array([[age, monthly_charges, tenure_months, num_products]])
    
    # প্রেডিকশন করা
    prediction = load_model.predict(user_input)
    
    # রেজাল্ট স্ক্রিনে দেখানো
    mode_app.success(f"🎯 আপনার মডেলের প্রেডিকশন রেজাল্ট: {prediction[0]}")
    
    # Churn এর ব্যাখ্যা (যদি মডেল ০ বা ১ দেয়)
    if int(round(prediction[0])) == 1:
        mode_app.warning("⚠️ এই গ্রাহকের চলে যাওয়ার (Churn) সম্ভাবনা বেশি!")
    else:
        mode_app.info("✅ এই গ্রাহকের থেকে যাওয়ার সম্ভাবনা বেশি।")
    