import streamlit as st

st.title("Story Analyzer")

story = st.text_area("Paste your story idea here:")

def clean_text(text): 
    text = text.lower()
    sentences = text.split(".")
    sentences = [s for s in sentences if s]
    punctuation = [".", ",", "!", "?", ":", ";"]
    for p in punctuation:
        text = text.replace(p, "")
    words = text.split()
    return text, words, sentences

def extract_features(text, words, sentences):
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
    if word_counts:
        max_repetition = max(word_counts.values())
    else:
        max_repetition = 0
    features = {
        "unique_word_count": unique_word_count,
        "vocabulary_diversity": vocabulary_diversity,
        "max_repetition": max_repetition,
        "word_counts": word_counts
    }

    return features

def detect_story_elements(words):
    emotion_words = ["happy", "sad", "angry", "excited"]
    emotion_found = False

    for word in emotion_words:
        if word in words:
            emotion_found = True

    conflict_words = ["fight", "betray", "problem", "helpless"]
    conflict_found = False

    for word in conflict_words:
        if word in words:
            conflict_found = True

    return emotion_found, conflict_found

def calculate_score(features, text, emotion_found, conflict_found):
    score = 50

    for word, count in features["word_counts"].items():
        if count > 10:
            score -= 10

    if text.count("the") > 20:
        score -= 10

    if len(text) > 300:
        score += 40

    elif len(text) > 100:
        score += 20
    
    if emotion_found:
        score += 2

    if conflict_found:
        score += 2

    return score

def generate_feedback(emotion_found, conflict_found):
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
    return strengths, suggestions

def explain_score(features, emotion_found, conflict_found):
    explanations = []

    if emotion_found:
        explanations.append("Emotional elements improved the score")

    if conflict_found:
        explanations.append("Conflict elements improved the score")

    if features["word_count"] > 300:
        explanations.append("Longer story length improved the score")

    if features["max_repetition"] > 10:
        explanations.append("Repeated words lowered the score")

    return explanations

def analyze_story_features(text):
    text, words, sentences = clean_text(text)
    features = extract_features(text, words, sentences)
    if sentences:
        average_sentence_length = len(words) / len(sentences)
    else:
        average_sentence_length = 0
    
    emotion_found, conflict_found = detect_story_elements(words)
    features.update({
        "word_count": len(words),
        "emotion_found": emotion_found,
        "conflict_found": conflict_found,
        "the_count": text.count("the"),
        "average_sentence_length": average_sentence_length
    })
    score = calculate_score(features, text, emotion_found, conflict_found)
    
    strengths, suggestions = generate_feedback(emotion_found, conflict_found)
    explanations = explain_score(features, emotion_found, conflict_found)
    

    


    return score, strengths, suggestions, features, explanations

if st.button("Analyze the Story"):
    if not story:
        st.warning("Please paste a story first.")
    else:
        score, strengths, suggestions, features, explanations = analyze_story_features(story)
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
        st.write("Score Explanation:")
        for e in explanations:
            st.write("- " + e)
