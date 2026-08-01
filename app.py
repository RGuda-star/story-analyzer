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
    if sentences:
        average_sentence_length = len(words) / len(sentences)
    else:
        average_sentence_length = 0
    features = {
        "unique_word_count": unique_word_count,
        "vocabulary_diversity": vocabulary_diversity,
        "max_repetition": max_repetition,
        "word_counts": word_counts,
        "average_sentence_length": average_sentence_length
    }

    return features

def detect_emotion(words):
    emotion_words = ["happy", "sad", "angry", "excited"]
    emotion_found = False

    for word in emotion_words:
        if word in words:
            emotion_found = True

    return emotion_found


def detect_conflict(words):
    conflict_words = ["fight", "betray", "problem", "helpless"]
    conflict_found = False

    for word in conflict_words:
        if word in words:
            conflict_found = True

    return conflict_found
character_names = ["raj", "arjun", "deva", "savita"]
def detect_characters(words):
    characters_found = set()

    for word in words:
        if word in character_names:
            characters_found.add(word)

    character_data = {
        "found": len(characters_found) > 0,
        "names": characters_found,
        "count": len(characters_found)
    }

    return character_data
setting_names = ["london", "paris", "mumbai", "atlanta"]
def detect_settings(words):
    setting_found = set()
    for word in words:
        if word in setting_names:
            setting_found.add(word)
    setting_data = {
        "found": len(setting_found) > 0,
        "names": setting_found, 
        "count": len(setting_found)

    }
    return setting_data

def detect_themes(words):
    theme_keywords = {
    "revenge": ["enemy", "avenge", "nemesis"],
    "family": ["mother", "father", "sibling"],
    "friendship": ["friend", "companion", "ally"],
    "sacrifice": ["surrender", "forgo", "leave"]
    }
    theme_found = set()
    for word in words:
        for theme, keywords in theme_keywords.items():
            if word in keywords:
                theme_found.add(theme)

    theme_data = {
        "found": len(theme_found)>0,
        "names": theme_found,
        "count": len(theme_found)
    }
    return theme_data

def detect_goals(words):
    goal_keywords = {
        "revenge": ["revenge", "avenge", "punish"],
        "search": ["find", "search", "discover"],
        "escape": ["escape", "run", "flee"],
        "protection": ["save", "protect", "defend"],
        "success": ["win", "achieve", "become"]
    }

    goals_found = set()

    for word in words:
        for goal, keywords in goal_keywords.items():
            if word in keywords:
                goals_found.add(goal)

    goal_data = {
        "found": len(goals_found) > 0,
        "names": goals_found,
        "count": len(goals_found)
    }

    return goal_data

def detect_stakes(words):
    stake_keywords = {
    "life": ["death", "kill", "murder", "die"],
    "family": ["family", "mother", "father", "sister", "brother"],
    "freedom": ["prison", "capture", "escape"],
    "world": ["world", "nation", "planet"],
    "reputation": ["honor", "respect", "fame"]
    }

    stakes_found = set()
    for word in words:
        for stake, keywords in stake_keywords.items():
            if word in keywords:
                stakes_found.add(stake)

    stake_data = {
        "found": len(stakes_found) > 0,
        "names": stakes_found,
        "count": len(stakes_found)
    }

    return stake_data

def detect_obstacles(words):
    obstacle_keywords = {
        "person": ["enemy", "villain", "killer"],
        "society": ["law", "government", "police"],
        "nature": ["storm", "earthquake", "fire"],
        "internal": ["fear", "doubt", "guilt"]
    }

    obstacles_found = set()

    for word in words:
        for obstacle, keywords in obstacle_keywords.items():
            if word in keywords:
                obstacles_found.add(obstacle)

    obstacle_data = {
        "found": len(obstacles_found) > 0,
        "names": obstacles_found,
        "count": len(obstacles_found)
    }

    return obstacle_data

def detect_story_structure(words):
    character_data = detect_characters(words)
    setting_data = detect_settings(words)
    theme_data = detect_themes(words)
    goal_data = detect_goals(words)
    stake_data = detect_stakes(words)
    obstacle_data = detect_obstacles(words)

    story_structure = {
        "characters": character_data,
        "settings": setting_data,
        "themes": theme_data,
        "goals": goal_data,
        "stakes": stake_data,
        "obstacles": obstacle_data
    }

    return story_structure
    

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
    
    emotion_found= detect_emotion(words)
    conflict_found = detect_conflict(words)
    story_structure = detect_story_structure(words)
    features.update({
        "word_count": len(words),
        "emotion_found": emotion_found,
        "conflict_found": conflict_found,
        "story_structure": story_structure,
        "the_count": text.count("the")
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
            if name == "story_structure":

                st.write("Story Structure:")

                characters = value["characters"]
                st.write("Characters Detected:")

                for character in characters["names"]:
                    st.write("- " + character)

                st.write("Total Characters:", characters["count"])


                settings = value["settings"]
                st.write("Settings Detected:")

                for setting in settings["names"]:
                    st.write("- " + setting)

                st.write("Total Settings:", settings["count"])


                themes = value["themes"]
                st.write("Themes Detected:")

                for theme in themes["names"]:
                    st.write("- " + theme)

                st.write("Total Themes:", themes["count"])
                goals = value["goals"]

                st.write("Goals Detected:")

                for goal in goals["names"]:
                    st.write("- " + goal)

                st.write("Total Goals:", goals["count"])

                stakes = value["stakes"]

                st.write("Stakes Detected:")

                for stake in stakes["names"]:
                    st.write("- " + stake)

                st.write("Total Stakes:", stakes["count"])

                obstacles = value["obstacles"]

                st.write("Obstacles Detected:")

                for obstacle in obstacles["names"]:
                    st.write("- " + obstacle)

                st.write("Total Obstacles:", obstacles["count"])

            else:
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
