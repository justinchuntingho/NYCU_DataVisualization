import streamlit as st
import pandas as pd

grades = pd.DataFrame({
    "student": ["Amy", "Ben", "Cathy", "David", "Eva", "Frank", "Grace", "Henry", "Ivy", "Jack"],
    "class": ["A", "A", "A", "B", "B", "B", "C", "C", "C", "C"],
    "hours_studied": [2, 4, 5, 3, 6, 8, 1, 7, 5, 9],
    "quiz_score": [62, 71, 78, 66, 85, 91, 55, 88, 80, 95],
})

# Better Layouts
st.header("Layout")
col1, col2 = st.columns(2)

with col1:
    st.metric("Average score", 10)

with col2:
    st.dataframe(grades)
st.sidebar.header("Control Panel")

# Sidebar
minimum_score = st.sidebar.slider("Passing score", 0, 100, 70)
filtered_students = grades[grades["quiz_score"] >= minimum_score]
st.dataframe(filtered_students)

# More Sidebar
st.sidebar.header("Reading Corner")
st.sidebar.write("""
“There is nothing like looking, if you want to find something. You certainly usually find something, if you look, but it is not always quite the something you were after.”
""")
st.sidebar.caption("From *The Hobbit* by J.R.R. Tolkien")


# Tabs
tab1, tab2 = st.tabs(["All", "Passed"])

with tab1:
    st.dataframe(grades)

with tab2:
    st.dataframe(filtered_students)

# Buttons
if st.button("Celebrate"):
    st.balloons()


