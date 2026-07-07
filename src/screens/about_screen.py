import streamlit as st
from src.ui.base_layout import style_background_dashboard, style_base_layout


def about_screen():
    style_background_dashboard()
    style_base_layout()

    # Back button
    if st.button("← Back to Home", type='secondary', key='about_back'):
        st.session_state['show_about'] = False
        st.rerun()

    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap');

        .about-hero {
            padding: 3rem 0 2rem 0;
            text-align: center;
        }
        .about-hero-tag {
            display: inline-block;
            background: rgba(79,70,229,0.12);
            border: 1px solid rgba(79,70,229,0.25);
            color: #818CF8;
            font-size: 0.72rem;
            font-weight: 600;
            letter-spacing: 0.1em;
            text-transform: uppercase;
            padding: 4px 14px;
            border-radius: 100px;
            margin-bottom: 1.25rem;
        }
        .about-hero-title {
            font-family: 'Plus Jakarta Sans', sans-serif;
            font-size: 2.25rem;
            font-weight: 800;
            color: #F1F5F9;
            letter-spacing: -0.04em;
            line-height: 1.15;
            margin-bottom: 1rem;
        }
        .about-hero-title span { color: #818CF8; }
        .about-hero-sub {
            font-family: 'Plus Jakarta Sans', sans-serif;
            font-size: 0.95rem;
            color: #64748B;
            line-height: 1.7;
            max-width: 600px;
            margin: 0 auto;
        }

        .section-title {
            font-family: 'Plus Jakarta Sans', sans-serif;
            font-size: 1.4rem;
            font-weight: 800;
            color: #F1F5F9;
            letter-spacing: -0.03em;
            margin-bottom: 0.4rem;
        }
        .section-sub {
            font-family: 'Plus Jakarta Sans', sans-serif;
            font-size: 0.85rem;
            color: #475569;
            margin-bottom: 1.75rem;
            line-height: 1.6;
        }

        .problem-card {
            background: #0D1117;
            border: 1px solid #1E293B;
            border-radius: 14px;
            padding: 1.5rem;
            height: 100%;
        }
        .problem-card-icon {
            font-size: 1.75rem;
            margin-bottom: 0.75rem;
            display: block;
        }
        .problem-card-title {
            font-family: 'Plus Jakarta Sans', sans-serif;
            font-size: 0.95rem;
            font-weight: 700;
            color: #E2E8F0;
            margin-bottom: 0.5rem;
        }
        .problem-card-desc {
            font-family: 'Plus Jakarta Sans', sans-serif;
            font-size: 0.8rem;
            color: #475569;
            line-height: 1.65;
        }

        .step-wrap {
            display: flex;
            align-items: flex-start;
            gap: 1.25rem;
            margin-bottom: 1.5rem;
        }
        .step-num {
            width: 36px; height: 36px;
            background: #4F46E5;
            border-radius: 10px;
            display: flex; align-items: center; justify-content: center;
            font-size: 0.85rem;
            font-weight: 800;
            color: white;
            flex-shrink: 0;
            font-family: 'Plus Jakarta Sans', sans-serif;
        }
        .step-content-title {
            font-family: 'Plus Jakarta Sans', sans-serif;
            font-size: 0.95rem;
            font-weight: 700;
            color: #E2E8F0;
            margin-bottom: 0.25rem;
        }
        .step-content-desc {
            font-family: 'Plus Jakarta Sans', sans-serif;
            font-size: 0.8rem;
            color: #475569;
            line-height: 1.6;
        }

        .stat-card {
            background: #0D1117;
            border: 1px solid #1E293B;
            border-radius: 14px;
            padding: 1.5rem;
            text-align: center;
        }
        .stat-num {
            font-family: 'Plus Jakarta Sans', sans-serif;
            font-size: 2rem;
            font-weight: 800;
            color: #818CF8;
            letter-spacing: -0.04em;
            line-height: 1;
            margin-bottom: 0.4rem;
        }
        .stat-label {
            font-family: 'Plus Jakarta Sans', sans-serif;
            font-size: 0.78rem;
            color: #475569;
            line-height: 1.5;
        }

        .tech-pill {
            display: inline-block;
            background: rgba(79,70,229,0.1);
            border: 1px solid rgba(79,70,229,0.2);
            color: #818CF8;
            font-size: 0.75rem;
            font-weight: 600;
            padding: 4px 12px;
            border-radius: 6px;
            margin: 3px;
            font-family: 'Plus Jakarta Sans', sans-serif;
        }

        .builder-card {
            background: #0D1117;
            border: 1px solid #1E293B;
            border-radius: 14px;
            padding: 2rem;
            display: flex;
            align-items: center;
            gap: 1.5rem;
        }
        .builder-avatar {
            width: 56px; height: 56px;
            background: #4F46E5;
            border-radius: 14px;
            display: flex; align-items: center; justify-content: center;
            font-size: 1.5rem;
            flex-shrink: 0;
        }
        .builder-name {
            font-family: 'Plus Jakarta Sans', sans-serif;
            font-size: 1.1rem;
            font-weight: 700;
            color: #E2E8F0;
            margin-bottom: 2px;
        }
        .builder-college {
            font-family: 'Plus Jakarta Sans', sans-serif;
            font-size: 0.8rem;
            color: #475569;
            margin-bottom: 0.5rem;
        }
        .builder-note {
            font-family: 'Plus Jakarta Sans', sans-serif;
            font-size: 0.82rem;
            color: #64748B;
            line-height: 1.6;
            font-style: italic;
        }

        .divider-section {
            border-top: 1px solid #1E293B;
            margin: 2.5rem 0;
        }
        </style>

        <!-- HERO -->
        <div class="about-hero">
            <div class="about-hero-tag">Why AttendX exists</div>
            <div class="about-hero-title">
                Attendance shouldn't take<br><span>15 minutes of class time.</span>
            </div>
            <div class="about-hero-sub">
                Every college, every class, every semester — the same drill.
                Sir calls out names, students say "present" for friends who aren't there,
                and 15 minutes of actual learning time disappears.
                AttendX fixes that with a photo and a few seconds.
            </div>
        </div>

        <div class="divider-section"></div>

        <!-- PROBLEMS -->
        <div class="section-title">The problems nobody talks about</div>
        <div class="section-sub">These aren't edge cases. This happens in every class, every day.</div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2, gap="medium")
    with col1:
        st.markdown("""
            <div class="problem-card">
                <span class="problem-card-icon">🎭</span>
                <div class="problem-card-title">Proxy attendance is everywhere</div>
                <div class="problem-card-desc">
                    A friend marks you present when you're not even in the building.
                    Teachers have no way to verify — just a name and a voice.
                    AttendX makes proxy physically impossible. Your face has to be in the room.
                </div>
            </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
            <div class="problem-card">
                <span class="problem-card-icon">⏱️</span>
                <div class="problem-card-title">10–15 minutes lost every class</div>
                <div class="problem-card-desc">
                    With 100+ students, calling names one by one eats into lecture time.
                    Over a full semester, that's 10+ hours of teaching time wasted on roll call alone.
                    AttendX does the same job in under 3 seconds.
                </div>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    col3, col4 = st.columns(2, gap="medium")
    with col3:
        st.markdown("""
            <div class="problem-card">
                <span class="problem-card-icon">📋</span>
                <div class="problem-card-title">Paper sheets for every subject</div>
                <div class="problem-card-desc">
                    Physics sheet. Chemistry sheet. Maths sheet.
                    Different registers, different classes, different teachers —
                    sheets get lost, damaged, or quietly altered.
                    AttendX keeps everything in one tamper-proof digital dashboard.
                </div>
            </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown("""
            <div class="problem-card">
                <span class="problem-card-icon">📉</span>
                <div class="problem-card-title">Students find out too late</div>
                <div class="problem-card-desc">
                    You only discover your attendance is below 75% when it's already too late to fix.
                    The student portal shows live attendance per subject —
                    so you always know exactly where you stand before it becomes a problem.
                </div>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("""<div class="divider-section"></div>""", unsafe_allow_html=True)

    # HOW IT WORKS
    st.markdown("""
        <div class="section-title">How it works</div>
        <div class="section-sub">Three steps. No manual entry. No paper.</div>

        <div class="step-wrap">
            <div class="step-num">1</div>
            <div>
                <div class="step-content-title">Students enroll once with their face</div>
                <div class="step-content-desc">
                    Each student registers using their phone camera. One photo is all it takes —
                    the system generates a unique 128-dimensional face embedding that acts as
                    their biometric ID. No re-enrollment needed, ever.
                </div>
            </div>
        </div>

        <div class="step-wrap">
            <div class="step-num">2</div>
            <div>
                <div class="step-content-title">Teacher takes a few classroom photos after class</div>
                <div class="step-content-desc">
                    After the lecture, the teacher uploads one or two photos of the classroom.
                    No need to do it during class — snap after everyone's seated, upload later.
                    The AI scans every face in every photo automatically.
                </div>
            </div>
        </div>

        <div class="step-wrap">
            <div class="step-num">3</div>
            <div>
                <div class="step-content-title">Attendance is marked and logged instantly</div>
                <div class="step-content-desc">
                    Every detected face is matched against enrolled students.
                    Present, absent, and unrecognized — all logged to the database in seconds.
                    Teachers review and confirm. Students see their record update in real time.
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""<div class="divider-section"></div>""", unsafe_allow_html=True)

    # STATS
    st.markdown("""
        <div class="section-title">The numbers</div>
        <div class="section-sub">What this actually changes in a real classroom.</div>
    """, unsafe_allow_html=True)

    s1, s2, s3, s4 = st.columns(4, gap="medium")
    with s1:
        st.markdown("""
            <div class="stat-card">
                <div class="stat-num">&lt;3s</div>
                <div class="stat-label">To mark an entire class present from one photo</div>
            </div>
        """, unsafe_allow_html=True)
    with s2:
        st.markdown("""
            <div class="stat-card">
                <div class="stat-num">0</div>
                <div class="stat-label">Proxy attendance possible with face verification</div>
            </div>
        """, unsafe_allow_html=True)
    with s3:
        st.markdown("""
            <div class="stat-card">
                <div class="stat-num">10+</div>
                <div class="stat-label">Hours of teaching time saved per subject per semester</div>
            </div>
        """, unsafe_allow_html=True)
    with s4:
        st.markdown("""
            <div class="stat-card">
                <div class="stat-num">128D</div>
                <div class="stat-label">Face embedding vector — unique to every student</div>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("""<div class="divider-section"></div>""", unsafe_allow_html=True)

    # TECH STACK
    st.markdown("""
        <div class="section-title">What's running under the hood</div>
        <div class="section-sub">
            Not just a wrapper around a library — every piece has a reason.
        </div>
        <p style="font-family:'Plus Jakarta Sans',sans-serif; font-size:0.85rem; color:#475569; line-height:1.7; margin-bottom:1rem;">
            Face detection uses dlib's HOG-based detector to locate faces in classroom photos.
            Each face is then passed through a pretrained ResNet-34 CNN — trained on millions of faces
            using triplet loss — to generate a 128-dimensional embedding that captures identity regardless
            of lighting or angle. A linear SVM classifies these embeddings against enrolled students,
            with a Euclidean distance threshold to avoid false matches.
            The result: one-photo enrollment, instant classroom-scale recognition.
        </p>
        <div style="margin-top:0.75rem;">
            <span class="tech-pill">dlib HOG detector</span>
            <span class="tech-pill">ResNet-34 CNN</span>
            <span class="tech-pill">Triplet Loss</span>
            <span class="tech-pill">128-D Embeddings</span>
            <span class="tech-pill">Linear SVM</span>
            <span class="tech-pill">Resemblyzer LSTM</span>
            <span class="tech-pill">Supabase</span>
            <span class="tech-pill">Streamlit</span>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""<div class="divider-section"></div>""", unsafe_allow_html=True)

    # BUILT BY
    st.markdown("""
        <div class="builder-card">
            <div class="builder-avatar">👨‍💻</div>
            <div>
                <div class="builder-name">Arnav Dasmal</div>
                <div class="builder-college">NIT Durgapur · Computer Science</div>
                <div class="builder-note">
                    "I built AttendX because I've sat in too many classes where the first 15 minutes
                    disappeared to roll call — and watched friends mark each other present without
                    a second thought. There had to be a better way."
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)
