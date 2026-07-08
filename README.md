# AttendX — AI-Powered Attendance System

> Eliminate proxy attendance and roll call time with face recognition. One classroom photo marks the entire class in under 3 seconds.

**Live Demo:** [attendx-3pojjrh3lyn48w9xejki2v.streamlit.app](https://attendx-3pojjrh3lyn48w9xejki2v.streamlit.app)

---

## The Problem

Every college, every class, every semester — the same drill. A teacher calls out 100+ names, students say "present" for friends who aren't there, and 15 minutes of actual learning time disappears. On top of that:

- **Proxy attendance** is rampant — no way to verify who's actually in the room
- **Paper registers** for every subject get lost, damaged, or quietly altered
- **Students discover low attendance** only when it's too late to fix
- **10+ hours** of teaching time wasted per subject per semester on roll call alone

AttendX fixes all of this with a photo and a few seconds.

---

## How It Works

```
Student enrolls once → Teacher snaps classroom photo → AI marks attendance instantly
```

1. **Student enrolls** using their phone camera — one photo generates a unique 128-D face embedding stored as their biometric ID
2. **Teacher uploads** one or two classroom photos after the lecture
3. **AI scans** every face, matches against enrolled students, and logs attendance to the database in seconds

---

## Features

- 📷 **Face Recognition Login** — students log in via camera, no passwords
- 🎓 **Teacher Dashboard** — manage subjects, upload photos, run AI attendance
- 👨‍🎓 **Student Portal** — view enrolled subjects and live attendance stats per subject
- 🔗 **QR/Link Enrollment** — teachers share a join code, students self-enroll instantly
- 📊 **Attendance Records** — full history with present/absent breakdown per class
- 🛡️ **Proxy-proof** — face must physically be in the room to be marked present

---

## ML/DL Stack

| Component | Technology | Purpose |
|---|---|---|
| Face Detection | dlib HOG + Linear SVM | Locate faces in classroom photo |
| Face Embedding | ResNet-34 CNN (pretrained, triplet loss) | Generate 128-D identity vector per face |
| Identity Classification | scikit-learn Linear SVM | Match embedding to enrolled student |
| Distance Verification | Euclidean distance (threshold 0.6) | Prevent false matches |
| Voice Embedding | Resemblyzer LSTM (GE2E loss) | Speaker verification fallback |
| Database | Supabase (PostgreSQL) | Store embeddings, subjects, attendance logs |

**Key design decision:** Uses pretrained embedding model + lightweight SVM instead of training a classifier from scratch — enabling one-photo enrollment (few-shot recognition) without retraining the deep network per student.

---

## Tech Stack

- **Frontend:** Streamlit
- **ML/DL:** dlib, face_recognition, Resemblyzer, scikit-learn, PyTorch, librosa
- **Database:** Supabase (PostgreSQL)
- **Deployment:** Streamlit Community Cloud
- **Language:** Python 3.11

---

## Project Structure

```
AttendX/
├── app.py                          # Main entry point
├── src/
│   ├── screens/
│   │   ├── home_screen.py          # Landing page
│   │   ├── teacher_screen.py       # Teacher dashboard + login
│   │   ├── student_screen.py       # Student portal + face login
│   │   └── about_screen.py         # About page
│   ├── pipelines/
│   │   ├── face_pipeline.py        # Face detection + embedding + classification
│   │   └── voice_pipeline.py       # Speaker verification
│   ├── components/                 # Reusable UI components + dialogs
│   ├── database/
│   │   ├── config.py               # Supabase client
│   │   └── db.py                   # All database operations
│   └── ui/
│       └── base_layout.py          # Global CSS + theme
└── requirements.txt
```

---

## Setup & Run Locally

**Prerequisites:** Python 3.11, Git

```bash
# Clone the repo
git clone https://github.com/ArnavsD4/AttendX.git
cd AttendX

# Create virtual environment
py -3.11 -m venv venv
.\venv\Scripts\Activate.ps1   # Windows
# source venv/bin/activate    # Mac/Linux

# Install dependencies
pip install -r requirements.txt
```

Create `.streamlit/secrets.toml`:
```toml
SUPABASE_URL = "your-supabase-url"
SUPABASE_KEY = "your-supabase-anon-key"
```

```bash
# Run the app
streamlit run app.py
```

---

## Database Schema

```sql
teachers       — teacher_id, name, username, password
students       — student_id, name, face_embedding, voice_embedding
subjects       — subject_id, name, subject_code, section, teacher_id
subject_students — enrollment mapping (subject_id, student_id)
attendance_logs  — subject_id, student_id, timestamp, is_present
```

---

## Built By

**Arnav Dasmal** — NIT Durgapur, Computer Science

*"I built AttendX because I've sat in too many classes where the first 15 minutes disappeared to roll call — and watched friends mark each other present without a second thought. There had to be a better way."*

---

## License

MIT License — feel free to use, modify, and build on this.
