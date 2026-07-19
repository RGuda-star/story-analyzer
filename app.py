import streamlit as st

st.title("Story Analyzer")

story = st.text_area("Paste your story idea here:")

def analyze_story_features(text):
    score = 50
    text = text.lower()
    sentences = text.split(".")
    sentences = [s for s in sentences if s]
    punctuation = [".", ",", "!", "?", ":", ";"]
    for p in punctuation:
        text = text.replace(p, "")
    words = text.split()
    if sentences:
        average_sentence_length = len(words) / len(sentences)
    else:
        average_sentence_length = 0
    unique_words = set(words)
    unique_word_count = len(unique_words)
    if words:
        vocabulary_diversity = unique_word_count / len(words)
    else:
        vocabulary_diversity = 0
    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    
    for word, count in word_counts.items():
        if count > 10:
            score -= 10
    

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

    features = {
        "word_count": len(words),
        "unique_word_count": unique_word_count,
        "max_repetition": max(word_counts.values()),
        "emotion_found": emotion_found,
        "conflict_found": conflict_found,
        "the_count": text.count("the"),
        "average_sentence_length": average_sentence_length,
        "vocabulary_diversity": vocabulary_diversity
    }


    return score, strengths, suggestions, features

if st.button("Analyze the Story"):
    if not story:
        st.warning("Please paste a story first.")
    else:
        score, strengths, suggestions, features = analyze_story_features(story)
        st.metric("Score", score)
        st.write("Features:")
        for name, value in features.items():
            st.write(name + ":" + str(value))
        st.write("Strengths:")
        for s in strengths:
            st.write("- " + s)
        st.write("Suggestions:")
        for s in suggestions:
            st.write("- " + s)
