import streamlit as st

st.title("Story Analyzer")

story = st.text_area("Paste your story idea here:")

def analyze_story_features(text):
    text = text.lower()
    punctuation = [".", ",", "!", "?", ":", ";"]
    for p in punctuation:
        text = text.replace(p, "")
    words = text.split()
    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    score = 50

    if text.count("the") > 20:
        score -= 10

    if len(text) > 300:
        score += 40

    elif len(text) > 100:
        score += 20
    
    emotion_words = ["happy", "sad", "angry", "excited"]
    emotion_found = False

    for word in emotion_words:
        if word in words:
            score += 2
            emotion_found = True
    
    conflict_words = ["fight", "betray", "problem", "helpless"]
    conflict_found = False

    for word in conflict_words:
        if word in words:
            score += 2
            conflict_found = True
    
    strengths = []
    suggestions = []
    if emotion_found:
        strengths.append("Emotional elements detected")
    if conflict_found == False:
        suggestions.append("Consider adding stronger conflict")
    if emotion_found == False:
        strengths.append("No strong emotional signals detected")
    if conflict_found:
        suggestions.append("Strong conflict detected")


    return score, strengths, suggestions

if st.button("Analyze the Story"):
    if not story:
        st.warning("Please paste a story first.")
    else:
        score, strengths, suggestions = analyze_story_features(story)
        st.metric("Score", score)
        st.write("Strengths:")
        for s in strengths:
            st.write("- " + s)
        st.write("Suggestions:")
        for s in suggestions:
            st.write("- " + s)
