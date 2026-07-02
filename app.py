import streamlit as st

st.title("Story Analyzer")

story = st.text_area("Paste your story idea here:")

def analyze_story_length(text):
    score = 50

    if len(text) > 300:
        score += 40

    elif len(text) > 100:
        score += 20


    return "Score: " + str(score) + "/100"

if st.button("Analyze the Story"):
    result = analyze_story_length(story)
    st.write(result)
