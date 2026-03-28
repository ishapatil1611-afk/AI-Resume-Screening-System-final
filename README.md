# 🎯 AI Resume Screening & Candidate Ranking System
(A sample resume data set is provided in the files named: "Resume.csv")

An advanced AI-powered web application that automates resume screening and intelligently ranks candidates based on job requirements using Natural Language Processing (NLP) and Machine Learning techniques.

---

## 📌 Problem Statement

Manual resume screening is time-consuming, error-prone, and inefficient. Recruiters often struggle to identify the best candidates quickly.

👉 This project solves that problem by:
- Automating resume analysis
- Extracting skills intelligently
- Ranking candidates objectively

---

## 🚀 Key Features

- 📂 Upload resume dataset (CSV format)
- 🧠 Automatic skill extraction using NLP
- 📊 Candidate ranking using TF-IDF & cosine similarity
- 🎯 Skill gap analysis:
  - ✅ Matched Skills
  - ❌ Missing Skills
- 🏆 Intelligent selection of **Strong Match Candidate**
- 🎨 Modern, interactive, and responsive UI
- ⚡ Fast and real-time processing

---

## 🛠️ Tech Stack

### 💻 Frontend
- HTML5
- CSS3 (Modern UI with animations)

### ⚙️ Backend
- Python
- Flask (Web Framework)

### 🧠 Machine Learning / NLP
- TF-IDF Vectorization
- Cosine Similarity
- Text Preprocessing (Cleaning, Tokenization)

### 📊 Data Handling
- Pandas

### ☁️ Deployment
- Render (Cloud Platform)

---

## 📂 Project Structure
AI-Resume-Screening-System/
│
├── app.py # Main Flask application
├── requirements.txt # Dependencies
├── Procfile # Deployment config
│
└── templates/
├── index.html # Input UI
└── result.html # Output UI

---

## ⚙️ How the System Works

### 🔹 Step 1: Input
- User uploads CSV containing resumes
- User enters required skills

### 🔹 Step 2: Text Processing
- Resume text is cleaned (remove symbols, HTML, etc.)
- Converted to lowercase for consistency

### 🔹 Step 3: Feature Extraction
- TF-IDF converts text into numerical vectors

### 🔹 Step 4: Similarity Calculation
- Cosine similarity compares job requirements with resumes

### 🔹 Step 5: Skill Analysis
- Extract all skills from resume
- Identify:
  - Matched skills
  - Missing skills

### 🔹 Step 6: Ranking
- Candidates ranked based on:
  - Similarity score
  - Skill match count

### 🔹 Step 7: Output
- Top 5 candidates displayed
- Strong match highlighted
- Visual skill tags shown

---

## 📊 Example Output

- Candidate Ranking
- Score (0–1 range)
- Skills detected
- Matched vs Missing skills
- Final suggestion (Strong Match / Needs Improvement)

---

---

## 💡 Future Enhancements

- 📈 Graph-based analytics dashboard
- 📄 Export results as PDF
- 🤖 AI chatbot for HR assistance
- 🎤 Voice input for job description
- 🧾 Resume parsing using advanced NLP models
- 🔐 Login system for recruiters

---

## 👩‍💻 Author

**Isha Patil**  
Computer Engineering Student 🚀

---

## 🧠 Key Concepts Used

- TF-IDF (Term Frequency - Inverse Document Frequency)
- Cosine Similarity
- Natural Language Processing (NLP)
- Skill Extraction
- Ranking Algorithms

---

## ⭐ Why This Project?

✔ Real-world application  
✔ Solves hiring inefficiency  
✔ Combines AI + Web Development  
✔ Fully deployable system  

---

## 🙌 Support

If you found this project useful:

⭐ Star this repository  
📢 Share with others  

---

## 🧾 License

This project is for educational purposes.
