# Getting Starting: imports
import streamlit as st
import pandas as pd

# Streamlit basics
st.title("Week 10: Getting Started with Streamlit")

st.write("This is a simple app to show you what streamlit can do")

st.write("""
You can also do multiple \\
lines \\
string
""")

st.header("This is how you do header")

st.subheader("This is how you do subheader")

# Working with data
st.header("1. Create some data")
grades = pd.DataFrame({
    "student": ["Amy", "Ben", "Cathy", "David", "Eva", "Frank", "Grace", "Henry", "Ivy", "Jack"],
    "class": ["A", "A", "A", "B", "B", "B", "C", "C", "C", "C"],
    "hours_studied": [2, 4, 5, 3, 6, 8, 1, 7, 5, 9],
    "quiz_score": [62, 71, 78, 66, 85, 91, 55, 88, 80, 95],
})
st.dataframe(grades)

# Data wrangling
st.header("2. Filter data")

minimum_score = 70
# minimum_score = st.slider("Passing score", 0, 100, 50)
filtered_students = grades[grades["quiz_score"] >= minimum_score]

st.write("Students who passed")
st.dataframe(filtered_students)

# Widgets
st.header("3. Widgets")
name = st.text_input("Student Name")
st.write("Hello", name)

score = st.number_input("Score", 0, 100)
st.write(name, "has", score, "points")

understood = st.checkbox("I understand")
st.write(understood)

if understood:
    st.write("Great")
else:
    st.write("Boo!!!")

# Data Visualisation
st.header("4. Working with Real Data")
pop = pd.read_csv("pop.csv")
pop = pop[pop['性別'] == '男女合計']
pop = pop[pop['區域別'] != '新竹市']
st.dataframe(pop)

st.subheader("Split-Apply-Combine")
results = pop.groupby('年月')['遷入人數'].mean()
st.dataframe(results)

st.metric(label="Population", value=results.iloc[0], delta=results.iloc[0]-results.iloc[1])


st.header("5. Graph it up")
st.bar_chart(results)

st.scatter_chart(
    pop,
    x="遷入人數",
    y="遷出人數",
    color="區域別",
    # size="人口數"
)

# Interactive Data Visualization, aka Dashboard
st.header("5. Make it interactive!")

region = st.selectbox(label = "Choose a region", options = ['東區','北區','香山'])
filtered_pop = pop[pop["區域別"] == region] # Filter data
st.scatter_chart(
    filtered_pop,
    x="遷入人數",
    y="遷出人數",
    # size="人口數"
)

x_select = st.selectbox(label = "Choose X", options = ['遷入人數','遷出人數','人口數', '出生人數','死亡人數'])
y_select = st.selectbox(label = "Choose Y", options = ['遷入人數','遷出人數','人口數', '出生人數','死亡人數'])
st.scatter_chart(
    filtered_pop,
    x=x_select,
    y=y_select,
)
