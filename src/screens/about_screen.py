import streamlit as st
from src.ui.base_layout import style_background_dashboard, style_base_layout


def about_screen():
    style_background_dashboard()
    style_base_layout()

    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap');

        /* Fix ghost/faded text Streamlit adds on scroll */
        h1, h2, h3, h4, h5, h6,
        [data-testid="stHeading"] * {
            opacity: 1 !important;
            color: #0F172A !important;
        }

        .about-tag {
            display: inline-block;
            background: #EEF2FF;
            border: 1px solid #C7D2FE;
            color: #4F46E5;
            font-size: 0.72rem;
            font-weight: 700;
            letter-spacing: 0.1em;
            text-transform: uppercase;
            padding: 4px 14px;
            border-radius: 100px;
            margin-bottom: 1rem;
            font-family: 'Plus Jakarta Sans', sans-serif;
        }
        .about-hero {
            text-align: center;
            padding: 2.5rem 1rem 2rem 1rem;
            max-width: 700px;
            margin: 0 auto;
        }
        .about-h1 {
            font-family: 'Plus Jakarta Sans', sans-serif;
            font-size: 2.25rem;
            font-weight: 800;
            color: #0F172A;
            letter-spacing: -0.04em;
            line-height: 1.15;
            margin-bottom: 1rem;
        }
        .about-h1 span { color: #4F46E5; }
        .about-sub {
            font-family: 'Plus Jakarta Sans', sans-serif;
            font-size: 0.9rem;
            color: #64748B;
            line-height: 1.75;
        }

        .section-wrap { padding: 0.5rem 0 1.5rem 0; }
        .section-h {
            font-family: 'Plus Jakarta Sans', sans-serif;
            font-size: 1.4rem;
            font-weight: 800;
            color: #0F172A !important;
            letter-spacing: -0.03em;
            margin-bottom: 0.3rem;
            opacity: 1 !important;
        }
        .section-p {
            font-family: 'Plus Jakarta Sans', sans-serif;
            font-size: 0.85rem;
            color: #64748B;
            margin-bottom: 1.5rem;
            line-height: 1.6;
        }

        .prob-card {
            background: #F8FAFC;
            border: 1px solid #E2E8F0;
            border-radius: 14px;
            padding: 1.5rem;
            height: 100%;
        }
        .prob-icon { font-size: 1.75rem; margin-bottom: 0.75rem; display: block; }
        .prob-title {
            font-family: 'Plus Jakarta Sans', sans-serif;
            font-size: 0.95rem; font-weight: 700;
            color: #0F172A; margin-bottom: 0.5rem;
        }
        .prob-desc {
            font-family: 'Plus Jakarta Sans', sans-serif;
            font-size: 0.8rem; color: #64748B; line-height: 1.65;
        }

        .step-row {
            display: flex; align-items: flex-start;
            gap: 1.25rem; margin-bottom: 1.5rem;
        }
        .step-n {
            width: 38px; height: 38px; background: #4F46E5;
            border-radius: 10px; display: flex;
            align-items: center; justify-content: center;
            font-size: 0.9rem; font-weight: 800; color: white;
            flex-shrink: 0;
            font-family: 'Plus Jakarta Sans', sans-serif;
        }
        .step-title {
            font-family: 'Plus Jakarta Sans', sans-serif;
            font-size: 0.95rem; font-weight: 700;
            color: #0F172A; margin-bottom: 0.25rem;
        }
        .step-desc {
            font-family: 'Plus Jakarta Sans', sans-serif;
            font-size: 0.8rem; color: #64748B; line-height: 1.6;
        }

        .stat-card {
            background: #F8FAFC;
            border: 1px solid #E2E8F0;
            border-radius: 14px;
            padding: 1.5rem;
            text-align: center;
        }
        .stat-n {
            font-family: 'Plus Jakarta Sans', sans-serif;
            font-size: 2rem; font-weight: 800;
            color: #4F46E5; letter-spacing: -0.04em;
            line-height: 1; margin-bottom: 0.4rem;
        }
        .stat-l {
            font-family: 'Plus Jakarta Sans', sans-serif;
            font-size: 0.75rem; color: #64748B; line-height: 1.5;
        }

        .tech-pill {
            display: inline-block;
            background: #EEF2FF; border: 1px solid #C7D2FE;
            color: #4F46E5; font-size: 0.72rem; font-weight: 600;
            padding: 4px 12px; border-radius: 6px; margin: 3px;
            font-family: 'Plus Jakarta Sans', sans-serif;
        }

        .builder-card {
            background: #F8FAFC; border: 1px solid #E2E8F0;
            border-radius: 14px; padding: 2rem;
            display: flex; align-items: flex-start; gap: 1.25rem;
        }
        .builder-av {
            width: 52px; height: 52px; background: #4F46E5;
            border-radius: 12px; display: flex;
            align-items: center; justify-content: center;
            font-size: 1.4rem; flex-shrink: 0;
        }
        .builder-name {
            font-family: 'Plus Jakarta Sans', sans-serif;
            font-size: 1rem; font-weight: 700; color: #0F172A; margin-bottom: 2px;
        }
        .builder-college {
            font-family: 'Plus Jakarta Sans', sans-serif;
            font-size: 0.78rem; color: #64748B; margin-bottom: 0.6rem;
        }
        .builder-quote {
            font-family: 'Plus Jakarta Sans', sans-serif;
            font-size: 0.82rem; color: #475569;
            line-height: 1.65; font-style: italic;
        }

        .divline { border-top: 1px solid #E2E8F0; margin: 2rem 0; }
        </style>
    """, unsafe_allow_html=True)

    # Back button
    if st.button("← Back to Home", type='secondary', key='about_back'):
        st.session_state['show_about'] = False
        st.rerun()

    # HERO
    st.markdown("""
        <div class="about-hero">
            <div class="about-tag">Why AttendX exists</div>
            <div class="about-h1">
                Attendance shouldn't take<br>
                <span>15 minutes of class time.</span>
            </div>
            <div class="about-sub">
                Every college, every class, every semester — the same drill.
                Sir calls out names, students say "present" for friends who aren't there,
                and 15 minutes of actual learning time disappears.
                AttendX fixes that with a photo and a few seconds.
            </div>
        </div>
        <div class="divline"></div>
    """, unsafe_allow_html=True)

    # PROBLEMS
    st.markdown("""
        <div class="section-wrap">
            <div class="section-h">The problems nobody talks about</div>
            <div class="section-p">These aren't edge cases. This happens in every class, every day.</div>
        </div>
    """, unsafe_allow_html=True)

    c1, c2 = st.columns(2, gap="medium")
    with c1:
        st.markdown("""
            <div class="prob-card">
                <span class="prob-icon">🎭</span>
                <div class="prob-title">Proxy attendance is everywhere</div>
                <div class="prob-desc">A friend marks you present when you're not even in the building.
                Teachers have no way to verify — just a name and a voice.
                AttendX makes proxy physically impossible. Your face has to be in the room.</div>
            </div>
        """, unsafe_allow_html=True)
    with c2:
        st.markdown("""
            <div class="prob-card">
                <span class="prob-icon">⏱️</span>
                <div class="prob-title">10–15 minutes lost every class</div>
                <div class="prob-desc">With 100+ students, calling names one by one eats into lecture time.
                Over a full semester, that's 10+ hours of teaching time wasted on roll call alone.
                AttendX does the same job in under 3 seconds.</div>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    c3, c4 = st.columns(2, gap="medium")
    with c3:
        st.markdown("""
            <div class="prob-card">
                <span class="prob-icon">📋</span>
                <div class="prob-title">Paper sheets for every subject</div>
                <div class="prob-desc">Physics sheet. Chemistry sheet. Maths sheet.
                Different registers, different classes, different teachers —
                sheets get lost, damaged, or quietly altered.
                AttendX keeps everything in one tamper-proof digital dashboard.</div>
            </div>
        """, unsafe_allow_html=True)
    with c4:
        st.markdown("""
            <div class="prob-card">
                <span class="prob-icon">📉</span>
                <div class="prob-title">Students find out too late</div>
                <div class="prob-desc">You only discover your attendance is below 75%
                when it's already too late to fix.
                The student portal shows live attendance per subject —
                so you always know exactly where you stand.</div>
            </div>
        """, unsafe_allow_html=True)

    st.markdown('<div class="divline"></div>', unsafe_allow_html=True)

    # HOW IT WORKS
    st.markdown("""
        <div class="section-wrap">
            <div class="section-h">How it works</div>
            <div class="section-p">Three steps. No manual entry. No paper.</div>
            <div class="step-row">
                <div class="step-n">1</div>
                <div>
                    <div class="step-title">Students enroll once with their face</div>
                    <div class="step-desc">Each student registers using their phone camera.
                    One photo is all it takes — the system generates a unique 128-dimensional
                    face embedding that acts as their biometric ID. No re-enrollment needed, ever.</div>
                </div>
            </div>
            <div class="step-row">
                <div class="step-n">2</div>
                <div>
                    <div class="step-title">Teacher takes a few classroom photos after class</div>
                    <div class="step-desc">After the lecture, the teacher uploads one or two photos
                    of the classroom. No need to do it during class — snap after everyone's seated,
                    upload later. The AI scans every face in every photo automatically.</div>
                </div>
            </div>
            <div class="step-row">
                <div class="step-n">3</div>
                <div>
                    <div class="step-title">Attendance is marked and logged instantly</div>
                    <div class="step-desc">Every detected face is matched against enrolled students.
                    Present, absent, and unrecognized — all logged to the database in seconds.
                    Teachers review and confirm. Students see their record update in real time.</div>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="divline"></div>', unsafe_allow_html=True)

    # STATS
    st.markdown("""
        <div class="section-wrap">
            <div class="section-h">The numbers</div>
            <div class="section-p">What this actually changes in a real classroom.</div>
        </div>
    """, unsafe_allow_html=True)

    s1, s2, s3, s4 = st.columns(4, gap="medium")
    with s1:
        st.markdown('<div class="stat-card"><div class="stat-n">&lt;3s</div><div class="stat-l">To mark an entire class present from one photo</div></div>', unsafe_allow_html=True)
    with s2:
        st.markdown('<div class="stat-card"><div class="stat-n">0</div><div class="stat-l">Proxy attendance possible with face verification</div></div>', unsafe_allow_html=True)
    with s3:
        st.markdown('<div class="stat-card"><div class="stat-n">10+</div><div class="stat-l">Hours of teaching time saved per subject per semester</div></div>', unsafe_allow_html=True)
    with s4:
        st.markdown('<div class="stat-card"><div class="stat-n">128D</div><div class="stat-l">Face embedding vector — unique to every student</div></div>', unsafe_allow_html=True)

    st.markdown('<div class="divline"></div>', unsafe_allow_html=True)

    # TECH
    st.markdown("""
        <div class="section-wrap">
            <div class="section-h">What's running under the hood</div>
            <div class="section-p">Not just a wrapper around a library — every piece has a reason.</div>
            <p style="font-family:'Plus Jakarta Sans',sans-serif; font-size:0.85rem;
               color:#475569; line-height:1.75; margin-bottom:1rem;">
                Face detection uses dlib's HOG-based detector to locate faces in classroom photos.
                Each face is passed through a pretrained ResNet-34 CNN — trained on millions of faces
                using triplet loss — to generate a 128-dimensional embedding that captures identity
                regardless of lighting or angle. A linear SVM classifies these embeddings against
                enrolled students, with a Euclidean distance threshold to avoid false matches.
            </p>
            <div>
                <span class="tech-pill">dlib HOG detector</span>
                <span class="tech-pill">ResNet-34 CNN</span>
                <span class="tech-pill">Triplet Loss</span>
                <span class="tech-pill">128-D Embeddings</span>
                <span class="tech-pill">Linear SVM</span>
                <span class="tech-pill">Resemblyzer LSTM</span>
                <span class="tech-pill">Supabase</span>
                <span class="tech-pill">Streamlit</span>
            </div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="divline"></div>', unsafe_allow_html=True)

    # BUILT BY
    st.markdown("""
        <div class="builder-card">
            <div class="builder-av">👨‍💻</div>
            <div>
                <div class="builder-name">Arnav Dasmal</div>
                <div class="builder-college">NIT Durgapur · Computer Science</div>
                <div class="builder-quote">
                    "I built AttendX because I've sat in too many classes where the first 15 minutes
                    disappeared to roll call — and watched friends mark each other present without
                    a second thought. There had to be a better way."
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)
