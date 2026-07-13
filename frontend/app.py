
import streamlit as st
import requests
import base64
import os
from PIL import Image

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="🌱 AgriVision AI",
    page_icon="🌱",
    layout="wide"
)

# ---------------- BACKGROUND ---------------- #

def add_bg():

    if os.path.exists("background.jpg"):

        with open("background.jpg","rb") as img:

            encoded = base64.b64encode(img.read()).decode()

        st.markdown(f"""

        <style>

        .stApp{{
            background-image:
            linear-gradient(
                rgba(255,255,255,0.18),
                rgba(255,255,255,0.18)
            ),
            url("data:image/jpg;base64,{encoded}");

            background-size:cover;
            background-position:center;
            background-repeat:no-repeat;
            background-attachment:fixed;
        }}

        </style>

        """,unsafe_allow_html=True)

add_bg()

# ---------------- CSS ---------------- #

st.markdown("""
<style>

/* Main Background */
.stApp{
    background-color:#F4FFF6;
}

/* Main Title */
.main-title{
    font-size:64px;
    font-weight:800;
    color:#1B5E20;
    text-align:center;
    margin-bottom:0;
    text-shadow:2px 2px 10px rgba(0,0,0,.15);
}

/* Subtitle */
.sub-title{
    font-size:22px;
    color:#4E5D52;
    text-align:center;
    margin-top:-15px;
    margin-bottom:25px;
}

/* Glass Card */
.glass-card{
    background:rgba(255,255,255,.72);
    backdrop-filter:blur(12px);
    border-radius:20px;
    padding:25px;
    border:1px solid rgba(255,255,255,.5);
    box-shadow:0 8px 25px rgba(0,0,0,.15);
}

/* Result Card */
.result-card{
    background:white;
    border-radius:20px;
    padding:20px;
    box-shadow:0px 10px 25px rgba(0,0,0,.15);
}

/* Footer */
.footer{
    text-align:center;
    color:#666;
    margin-top:50px;
    font-size:16px;
}

.block-container{
    padding-top:2rem;
}

</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ---------------- #

st.markdown("""
<h1 class='main-title'>
🌱 AgriVision AI
</h1>
""", unsafe_allow_html=True)

st.markdown("""
<p class='sub-title'>
AI Powered Plant Disease Detection using <b>YOLOv8</b>
</p>
""", unsafe_allow_html=True)

st.divider()

# ---------------- IMAGE UPLOAD ---------------- #
st.markdown("""
    <div class="glass-card">

    <h3 style="text-align:center;color:#1B5E20;">
    📤 Upload Plant Leaf Images
    </h3>

    <p style="text-align:center;color:gray;">
    Supported Formats: JPG • JPEG • PNG
    </p>

    </div>
    """, unsafe_allow_html=True)

uploaded_files = st.file_uploader(
"",
    type=["jpg", "jpeg", "png"],
    accept_multiple_files=True,
    label_visibility="collapsed"
)
detect = False

if uploaded_files:

    st.success(f"✅ {len(uploaded_files)} image(s) selected.")

    detect = st.button(
        "🔍 Detect Disease",
        type="primary",
        use_container_width=True
    )

# ================= DASHBOARD ================= #

st.markdown("## 📊 Dashboard")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "📷 Images Uploaded",
        len(uploaded_files) if uploaded_files else 0
    )

with col2:
    st.metric(
        "🤖 Model",
        "YOLOv8"
    )

with col3:
    st.metric(
        "🌐 Backend",
        "Online"
    )

st.divider()
# ================= SIDEBAR ================= #

with st.sidebar:

    st.markdown("## 🌱 AgriVision AI")

    st.caption("AI Powered Crop Disease Detection")

    st.divider()

    # ---------- System Status ---------- #

    st.subheader("🖥 System Status")

    st.success("🟢 Backend Connected")

    st.success("🟢 Flask API Running")

    st.success("🟢 YOLOv8 Model Ready")

    st.divider()

    # ---------- Supported Crops ---------- #

    st.subheader("🌾 Supported Crops")

    crop1, crop2 = st.columns(2)

    with crop1:
        st.markdown("🍅 Tomato")
        st.markdown("🥔 Potato")

    with crop2:
        st.markdown("🫑 Pepper")

    st.divider()

    # ---------- Statistics ---------- #

    st.subheader("📊 Statistics")

    uploaded_count = len(uploaded_files) if uploaded_files else 0

    st.metric("Images Uploaded", uploaded_count)

    st.metric("Model", "YOLOv8")

    st.metric("Backend", "Flask")

    st.divider()

    # ---------- Tips ---------- #

    st.subheader("💡 Tips")

    st.info(
        """
✅ Upload a clear leaf image

✅ Keep only one leaf in frame

✅ Use good lighting

✅ Avoid blurry images
        """
    )

    st.divider()

    st.caption("Version 1.0")

# ---------------- PROCESS IMAGES ---------------- #

if uploaded_files and detect:
    st.markdown("""
    <div style="
    background:rgba(255,255,255,0.90);
    padding:25px;
    border-radius:20px;
    box-shadow:0px 8px 20px rgba(0,0,0,.15);
    margin-bottom:25px;
    ">

    <h2 style="color:#1B5E20;text-align:center;">
    🌿 Prediction Dashboard
    </h2>

    <p style="
    text-align:center;
    color:#555;
    font-size:18px;
    ">
    AI has analyzed the uploaded plant leaf image(s). Review the prediction, confidence, severity, and treatment below.
    </p>

    </div>
    """, unsafe_allow_html=True)

    st.success(f"✅ {len(uploaded_files)} image(s) uploaded successfully.")

    for file in uploaded_files:

        left, right = st.columns([1, 1])

        # ---------------- LEFT SIDE ---------------- #

        with left:

            image = Image.open(file)

            width, height = image.size

            st.markdown("""
            <div style="
            background:white;
            padding:20px;
            border-radius:18px;
            box-shadow:0px 8px 20px rgba(0,0,0,0.15);
            margin-bottom:15px;
            ">
            <h3 style="color:#1B5E20;text-align:center;">
            🖼 Uploaded Leaf Image
            </h3>
            </div>
            """, unsafe_allow_html=True)

            st.image(
                image,
                use_container_width=True
            )

            col1, col2 = st.columns(2)

            with col1:
                st.metric("📄 File", file.name)

            with col2:
                st.metric("📐 Size", f"{width} × {height}")

        # ---------------- RIGHT SIDE ---------------- #

        with right:

            st.markdown("### 🤖 AI Analysis")

            with st.spinner("Analyzing leaf image..."):

                try:

                    files = {
                        "image": (
                            file.name,
                            file.getvalue(),
                            file.type
                        )
                    }

                    response = requests.post(
                        "http://127.0.0.1:5000/upload",
                        files=files,
                        timeout=30
                    )

                    if response.status_code == 200:

                        result = response.json()

                        prediction = result["prediction"]

                        recommendation = result["recommendation"]

                        disease = prediction["disease"]

                        confidence = prediction["confidence"]

                        severity = recommendation["severity"]

                        treatment = recommendation["treatment"]

                    else:

                        st.error(f"❌ Backend Error ({response.status_code})")

                        st.code(response.text)

                        st.stop()

                except Exception:

                    st.error("❌ Cannot connect to Flask Backend")

                    st.info(
                        "Make sure backend is running:\n\npython3 app.py"
                    )

                    st.stop()

            st.markdown("---")

            st.markdown(f"""
                <div style="
                background:linear-gradient(135deg,#2E7D32,#43A047);
                padding:20px;
                border-radius:15px;
                text-align:center;
                color:white;
                margin-bottom:15px;
                ">
                <h3>🦠 Disease Detected</h3>
                <h2>{disease}</h2>
                </div>
                """, unsafe_allow_html=True)

            st.markdown("""
            <div style="
            background:white;
            padding:18px;
            border-radius:15px;
            box-shadow:0px 4px 10px rgba(0,0,0,0.15);
            margin-top:10px;
            margin-bottom:10px;
            ">
            <h3 style="color:#1B5E20;">📊 Confidence Score</h3>
            </div>
            """, unsafe_allow_html=True)

            st.metric(
                label="Confidence",
                value=f"{confidence}%"
            )

            st.progress(min(confidence / 100, 1.0))

            st.caption(f"Model Confidence: {confidence}%")

            st.markdown("""
            <div style="
            background:white;
            padding:18px;
            border-radius:15px;
            box-shadow:0px 4px 10px rgba(0,0,0,0.15);
            margin-top:15px;
            margin-bottom:15px;
            ">
            <h3 style="color:#1B5E20;">🚨 Severity Level</h3>
            </div>
            """, unsafe_allow_html=True)

            if severity.lower() == "low":
                st.markdown("""
                <div style="
                background:#E8F5E9;
                color:#2E7D32;
                padding:15px;
                border-radius:12px;
                text-align:center;
                font-size:22px;
                font-weight:bold;
                ">
                🟢 LOW
                </div>
                """, unsafe_allow_html=True)

            elif severity.lower() == "medium":
                st.markdown("""
                <div style="
                background:#FFF8E1;
                color:#F9A825;
                padding:15px;
                border-radius:12px;
                text-align:center;
                font-size:22px;
                font-weight:bold;
                ">
                🟡 MEDIUM
                </div>
                """, unsafe_allow_html=True)

            elif severity.lower() == "high":
                st.markdown("""
                <div style="
                background:#FFEBEE;
                color:#C62828;
                padding:15px;
                border-radius:12px;
                text-align:center;
                font-size:22px;
                font-weight:bold;
                ">
                🔴 HIGH
                </div>
                """, unsafe_allow_html=True)

            else:
                st.info(severity)

            st.markdown("---")

            st.markdown(f"""
                <div style="
                background:#E8F5E9;
                padding:20px;
                border-radius:18px;
                border-left:8px solid #2E7D32;
                box-shadow:0px 5px 12px rgba(0,0,0,0.12);
                margin-top:20px;
                ">

                <h3 style="color:#1B5E20;">
                💊 Treatment Recommendation
                </h3>

                <p style="
                font-size:18px;
                color:#333;
                line-height:1.8;
                ">
                ✅ {treatment}
                </p>

                </div>
                """, unsafe_allow_html=True)
            
            report = f"""
            🌱 AGRIVISION AI - PLANT DISEASE REPORT

            ----------------------------------------

            File Name : {file.name}

            Disease : {disease}

            Confidence : {confidence}%

            Severity : {severity}

            Treatment :
            {treatment}

            ----------------------------------------

            Generated by AgriVision AI
            """

            st.download_button(
                "📥 Download Report",
                data=report,
                file_name=f"{file.name}_report.txt",
                mime="text/plain",
                use_container_width=True
            )

            st.divider()

# ---------------- PROJECT INFORMATION ---------------- #

with st.expander("ℹ️ About AgriVision AI"):

    st.markdown("""
### 🌱 AgriVision AI

AgriVision AI is an AI-powered crop disease detection system developed using **YOLOv8**, **Flask**, and **Streamlit**.

### Features

- ✅ Multiple Image Upload
- ✅ AI Disease Detection
- ✅ Confidence Score
- ✅ Severity Level
- ✅ Treatment Recommendation
- ✅ Beautiful User Interface

### Tech Stack

- Python
- YOLOv8
- Flask
- Streamlit
- OpenCV

""")


st.markdown("<br><br>", unsafe_allow_html=True)

st.markdown("""
<hr>

<center>

<h4 style='color:#1B5E20'>
🌱 AgriVision AI
</h4>

AI Powered Crop Disease Detection

<br>

Developed for Hackathon using

<b>YOLOv8 • Flask • Streamlit</b>

</center>

""", unsafe_allow_html=True)
