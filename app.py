from flask import Flask, render_template, request
import pandas as pd
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

# MASTER SKILL LIST
ALL_SKILLS = [
    "python","java","c","c++","sql","html","css","javascript",
    "machine learning","data science","excel","power bi","tableau",
    "communication","management","aws","cloud","react","node"
]

# CLEAN TEXT
def clean_text(text):
    text = str(text).lower()
    text = re.sub(r'<.*?>', ' ', text)
    text = re.sub(r'[^\w\s]', ' ', text)
    return text

# EXTRACT SKILLS
def extract_all_skills(text):
    words = text.split()
    found = []

    for skill in ALL_SKILLS:
        skill_words = skill.split()
        if all(word in words for word in skill_words):
            found.append(skill)

    return list(set(found))


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/result', methods=['POST'])
def result():
    try:
        file = request.files['file']
        skills_input = request.form['skills']

        required_skills = [s.strip().lower() for s in skills_input.split(",") if s.strip()]

        df = pd.read_csv(file)

        if "Resume_str" not in df.columns:
            return "Error: Resume_str column missing"

        df["Cleaned"] = df["Resume_str"].apply(clean_text)

        resumes = df["Cleaned"].tolist()
        job_desc = " ".join(required_skills)

        texts = resumes + [job_desc]

        vectorizer = TfidfVectorizer(stop_words='english')
        vectors = vectorizer.fit_transform(texts)

        similarity = cosine_similarity(vectors[-1], vectors[:-1])
        df["Score"] = similarity[0]

        df_sorted = df.sort_values(by="Score", ascending=False)
        top = df_sorted.head(5)

        temp = []

        # PROCESS EACH CANDIDATE
        for _, row in top.iterrows():
            text = row["Cleaned"]

            candidate_skills = extract_all_skills(text)

            matched = list(set(candidate_skills) & set(required_skills))
            missing = list(set(required_skills) - set(candidate_skills))

            temp.append({
                "row": row,
                "skills": candidate_skills,
                "matched": matched,
                "missing": missing,
                "match_count": len(matched)
            })

        # 🔥 FIND BEST CANDIDATE
        best_index = 0
        best_value = -1

        for i, item in enumerate(temp):
            score = item["row"]["Score"]
            match_count = item["match_count"]

            value = score + (match_count * 0.1)

            if value > best_value:
                best_value = value
                best_index = i

        # 🔥 FINAL RESULT
        results = []

        for i, item in enumerate(temp):
            row = item["row"]

            if i == best_index:
                suggestion = "Strong Match"
            else:
                suggestion = "Needs Improvement"

            results.append({
                "ID": row.get("ID", "N/A"),
                "Category": row.get("Category", "N/A"),
                "Score": round(row["Score"], 3),

                "Skills": item["skills"] if item["skills"] else ["No skills found"],
                "Matched": item["matched"] if item["matched"] else ["No match"],
                "Missing": item["missing"] if item["missing"] else ["None"],

                "Suggestion": suggestion
            })

        return render_template('result.html', data=results)

    except Exception as e:
        return f"Error: {e}"


if __name__ == "__main__":
    app.run(debug=True)