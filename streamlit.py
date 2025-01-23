import streamlit as st #pip install streamlit
import time
import joblib  #ML model save, load #pip install joblib
# joblib.dump(regressor, "./~pkl")
# model = joblib.load("models/~.pkl")
import numpy as np

st.title("APT / ADS 지표 활용")
st.header("ㅎ.........")

iter = st.empty()
bar = st.progress(0)

for i in range(10):
    iter.text(f"Progress...{i+1}")
    bar.progress(i+1)
    time.sleep(0.01)

#step1.
# user_input = st.chat_input("요구사항을 말하시오")
# if user_input:
#     st.write(f"사용자입력: {user_input}")

#step2.
# with st.chat_message("user"):
#     st.write("안뇽~")
#     st.line_chart(np.random.randn(30, 3))

#step3.
# user_input = st.chat_input("퀘스쳔?")
# if user_input:
#     st.chat_message(name="user").write(user_input)
#     st.chat_message(name="ai").write(user_input)
#     st.chat_message(name="user").write(user_input)
#     st.chat_message(name="ai").write(user_input)

#step4.
if "message" not in st.session_state:
    st.session_state["message"] = []

for role, msg in st.session_state["message"]:
    st.chat_message(name=role).write(msg)

user_input = st.chat_input("퀘스쳔?")
if user_input:
    st.chat_message(name="user").write(user_input)
    st.chat_message(name="ai").write(user_input)

    st.session_state["message"].append("user", user_input)
    st.session_state["message"].append("ai", user_input)