
# # import streamlit as st
# # from utils.style import load_css
# # from utils.transition import page_transition
# # import base64

# # # 1. Page Configuration
# # st.set_page_config(page_title="Home", layout="wide")

# # # 2. Load your original global CSS
# # load_css()
# # page_transition("fade")

# # # 3. HOME PAGE SPECIFIC OVERRIDES
# # st.markdown(
# #     """
# #     <style>
# #     :root {
# #         --bottombar-height: 56px;
# #     }

# #     .stApp {
# #         padding-bottom: var(--bottombar-height);
# #     }

# #     /* ===== Bottom moving bar ===== */
# #     .top-bar {
# #         position: fixed;
# #         bottom: 0;
# #         left: 0;
# #         width: 100%;
# #         height: var(--bottombar-height);
# #         background: linear-gradient(90deg, #2563eb, #4f46e5, #2563eb);
# #         color: white !important;
# #         font-weight: 600;
# #         display: flex;
# #         align-items: center;
# #         justify-content: center;
# #         z-index: 999999;
# #         overflow: hidden;
# #     }

# #     .top-bar span {
# #         display: inline-block;
# #         white-space: nowrap;
# #         animation: moveText 15s linear infinite;
# #         font-size: 1.1rem;
# #     }

# #     @keyframes moveText {
# #         from { transform: translateX(100%); }
# #         to   { transform: translateX(-100%); }
# #     }

# #     /* ===== Floating background shapes ===== */
# #     .float-shape {
# #         position: fixed;
# #         border-radius: 50%;
# #         opacity: 0.18;
# #         filter: blur(2px);
# #         animation: float 12s ease-in-out infinite;
# #         z-index: 0;
# #     }

# #     .shape1 {
# #         width: 220px;
# #         height: 220px;
# #         background: #c084fc;
# #         top: 20%;
# #         left: 5%;
# #     }

# #     .shape2 {
# #         width: 300px;
# #         height: 300px;
# #         background: #a78bfa;
# #         bottom: 10%;
# #         right: 8%;
# #         animation-delay: 4s;
# #     }

# #     @keyframes float {
# #         0%   { transform: translateY(0px); }
# #         50%  { transform: translateY(-30px); }
# #         100% { transform: translateY(0px); }
# #     }

# #     /* ===== GIF Character ===== */
# #     .gif-character {
# #         position: fixed;

# #         /* POSITION CONTROLS */
# #         bottom: 160px;   /* distance from bottom */
# #         right: 70px;    /* distance from right */

# #         /* OR use these instead */
# #         /* top: 100px; left: 50px; */

# #         width: 280px; //140px
# #         z-index: 9999;

# #         animation: floatChar 4s ease-in-out infinite;
# #     }
# #     .gif-character img {
# #         width: 280px;
# #         height: 280px;
# #         object-fit: cover;
# #         border-radius: 50%;
# #     }


# #     @keyframes floatChar {
# #         0%   { transform: translateY(0px); }
# #         50%  { transform: translateY(-15px); }
# #         100% { transform: translateY(0px); }
# #     }
# #     </style>
# #     """,
# #     unsafe_allow_html=True
# # )

# # # ---------- BOTTOM BAR ----------
# # st.markdown(
# #     """
# #     <div class="top-bar">
# #         <span>✨ Welcome • Hindi to ISL Translator • Inclusive Communication • Accessibility First ✨</span>
# #     </div>
# #     """,
# #     unsafe_allow_html=True
# # )

# # # ---------- FLOATING SHAPES ----------
# # st.markdown(
# #     """
# #     <div class="float-shape shape1"></div>
# #     <div class="float-shape shape2"></div>
# #     """,
# #     unsafe_allow_html=True
# # )


# # # ---------- GIF CHARACTER ----------
# # with open("assets/character.gif", "rb") as f:
# #     gif_data = base64.b64encode(f.read()).decode()

# # st.markdown(
# #     f"""
# #     <div class="gif-character">
# #         <img src="data:image/gif;base64,{gif_data}" />
# #     </div>
# #     """,
# #     unsafe_allow_html=True
# # )

# # # ---------- CONTENT ----------
# # st.title("Home")
# # st.write("Welcome to the Hindi-ISL Bridge")

# # st.markdown("---")

# # col1, col2 = st.columns(2)

# # with col1:
# #     if st.button("Login"):
# #         st.switch_page("pages/form.py")

# # with col2:
# #     if st.button("Translate Hindi to ISL"):
# #         st.switch_page("pages/main.py")

# import streamlit as st
# from utils.style import load_css
# from utils.transition import page_transition
# import base64

# # 1. Page Configuration
# st.set_page_config(page_title="Home", layout="wide")

# # 2. Load your original global CSS
# load_css()
# page_transition("fade")

# # 3. Load GIF as base64
# def get_base64_gif(path):
#     with open(path, "rb") as f:
#         data = f.read()
#     return base64.b64encode(data).decode("utf-8")

# gif_base64 = get_base64_gif("assets/character.gif")

# # 4. HOME PAGE SPECIFIC OVERRIDES
# st.markdown(
#     f"""
#     <style>
#     :root {{
#         --bottombar-height: 56px;
#     }}
#     .stApp {{
#         padding-bottom: var(--bottombar-height);
#         background: linear-gradient(135deg, #DCEDC2 0%, #FFD3B5 100%);
#         min-height: 100vh;
#     }}

#     /* ===== Bottom moving bar ===== */
#     .top-bar {{
#         position: fixed;
#         bottom: 0;
#         left: 0;
#         width: 100%;
#         height: var(--bottombar-height);
#         background: linear-gradient(90deg, #2563eb, #4f46e5, #2563eb);
#         color: white !important;
#         font-weight: 600;
#         display: flex;
#         align-items: center;
#         justify-content: center;
#         z-index: 999999;
#         overflow: hidden;
#     }}
#     .top-bar span {{
#         display: inline-block;
#         white-space: nowrap;
#         animation: moveText 15s linear infinite;
#         font-size: 1.1rem;
#     }}
#     @keyframes moveText {{
#         from {{ transform: translateX(100%); }}
#         to   {{ transform: translateX(-100%); }}
#     }}

#     /* ===== Floating background shapes ===== */
#     .float-shape {{
#         position: fixed;
#         border-radius: 50%;
#         opacity: 0.18;
#         filter: blur(2px);
#         animation: float 12s ease-in-out infinite;
#         z-index: 0;
#     }}
#     .shape1 {{
#         width: 220px; height: 220px;
#         background: #c084fc;
#         top: 20%; left: 5%;
#     }}
#     .shape2 {{
#         width: 300px; height: 300px;
#         background: #a78bfa;
#         bottom: 10%; right: 8%;
#         animation-delay: 4s;
#     }}
#     @keyframes float {{
#         0%   {{ transform: translateY(0px); }}
#         50%  {{ transform: translateY(-30px); }}
#         100% {{ transform: translateY(0px); }}
#     }}

#     /* ===== Character — fixed to right, true mask fade ===== */
#     .character-fixed {{
#         position: fixed;
#         right: 2%;
#         bottom: calc(var(--bottombar-height) + 0px);
#         width: 400px;
#         z-index: 100;
#         pointer-events: none;
#     }}

#     .character-gif {{
#         width: 400px;
#         height: auto;
#         display: block;
#         animation: character-float 4s ease-in-out infinite;

#         /* TRUE transparency mask — fades all four edges inward.
#            Works on any background including gradients. */
#         -webkit-mask-image: radial-gradient(
#             ellipse 75% 80% at 55% 45%,
#             black 30%,
#             rgba(0,0,0,0.6) 50%,
#             rgba(0,0,0,0.2) 65%,
#             transparent 80%
#         );
#         mask-image: radial-gradient(
#             ellipse 75% 80% at 55% 45%,
#             black 30%,
#             rgba(0,0,0,0.6) 50%,
#             rgba(0,0,0,0.2) 65%,
#             transparent 80%
#         );
#     }}

#     @keyframes character-float {{
#         0%, 100% {{ transform: translateY(0px);   }}
#         50%       {{ transform: translateY(-14px); }}
#     }}
#     </style>
#     """,
#     unsafe_allow_html=True
# )

# # ---------- BOTTOM BAR ----------
# st.markdown(
#     """
#     <div class="top-bar">
#         <span>✨ Welcome • Hindi to ISL Translator • Inclusive Communication • Accessibility First ✨</span>
#     </div>
#     """,
#     unsafe_allow_html=True
# )

# # ---------- FLOATING SHAPES ----------
# st.markdown(
#     """
#     <div class="float-shape shape1"></div>
#     <div class="float-shape shape2"></div>
#     """,
#     unsafe_allow_html=True
# )

# # ---------- CHARACTER GIF (fixed right) ----------
# st.markdown(
#     f"""
#     <div class="character-fixed">
#         <img class="character-gif"
#              src="data:image/gif;base64,{gif_base64}"
#              alt="Welcome character" />
#     </div>
#     """,
#     unsafe_allow_html=True
# )

# # ---------- CONTENT (left side) ----------
# st.title("Home")
# st.write("Welcome to the Hindi-ISL Bridge")
# st.markdown("---")

# col1, col2 = st.columns(2)
# with col1:
#     if st.button("Login"):
#         st.switch_page("pages/form.py")
# with col2:
#     if st.button("Translate Hindi to ISL"):
#         st.switch_page("pages/main.py")

import streamlit as st
from utils.style import load_css
from utils.transition import page_transition
import base64

# 1. Page Configuration
st.set_page_config(page_title="Home", layout="wide")

# 2. Load global CSS + transition
load_css()
page_transition("fade")

# 3. Load GIF as base64
def get_base64_gif(path):
    with open(path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode("utf-8")

gif_base64 = get_base64_gif("assets/character.gif")

# ---------- STYLES ----------
st.markdown(
    f"""
    <style>

    .stApp {{
        background: #F4F4F4;
        min-height: 100vh;
        padding-bottom: 60px; /* prevents overlap with bottom bar */
    }}

    /* ===== Floating shapes ===== */
.float-shape {{
    position: fixed;
    border-radius: 50%;
    opacity: 0.18;
    filter: blur(2px);
    animation: float 12s ease-in-out infinite;
    z-index: 0;
}}

.shape1 {{
    width: 220px; height: 220px;
    background: #ff7f50; /* coral */
    top: 20%; left: 5%;
}}

.shape2 {{
    width: 200px; height: 200px;
    background: #ff6f61; /* softer coral-red */
    bottom: 10%; right: 38%;
    animation-delay: 4s;
}}

@keyframes float {{
    0%   {{ transform: translateY(0px); }}
    50%  {{ transform: translateY(-30px); }}
    100% {{ transform: translateY(0px); }}
}}

    /* ===== Character ===== */
    .character-fixed {{
        position: fixed;
        right: 2%;
        bottom: 80px;
        width: 400px;
        z-index: 100;
        pointer-events: none;
    }}

    .character-gif {{
        width: 400px;
        animation: character-float 4s ease-in-out infinite;
    }}

    @keyframes character-float {{
        0%, 100% {{ transform: translateY(0px); }}
        50%       {{ transform: translateY(-14px); }}
    }}

    /* ===== Title ===== */
    .product-title a {{
        font-size: 2.8rem;
        font-weight: 800;
        color: #1e1b4b;
        text-decoration: none;
    }}

    .product-title a:hover {{
        color: #4f46e5;
        text-decoration: underline;
    }}

    /* ===== Bottom Bar ===== */
    .bottom-bar {{
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        height: 50px;
        background: linear-gradient(90deg, #FF8C94, #FFAAA6, #FFD3B5, #FFAAA6, #FF8C94);
        background-size: 200% 100%;
        animation: gradientShift 8s ease infinite;
        color: #2d3748;
        font-weight: 700;
        display: flex;
        align-items: center;
        justify-content: center;
        z-index: 999999;
        border-top: 3px solid #FF8C94;
        box-shadow: 0 -4px 20px rgba(255, 140, 148, 0.3);
        overflow: hidden;
    }}

    @keyframes gradientShift {{
        0% {{ background-position: 0% 50%; }}
        50% {{ background-position: 100% 50%; }}
        100% {{ background-position: 0% 50%; }}
    }}

    .bottom-bar span {{
        white-space: nowrap;
        animation: moveText 15s linear infinite;
    }}

    @keyframes moveText {{
        from {{ transform: translateX(100%); }}
        to   {{ transform: translateX(-100%); }}
    }}

    /* ===== Description ===== */
    .product-description {{
        margin-top: 1rem;
        max-width: 520px;
        font-size: 1.05rem;
        line-height: 1.7;
        background: rgba(255,255,255,0.6);
        border-left: 4px solid #4f46e5;
        border-radius: 8px;
        padding: 1rem;
    }}

    .product-description a {{
        text-decoration: none;
        color: #374151;
    }}

    .product-description a:hover {{
        color: #4f46e5;
    }}

    </style>
    """,
    unsafe_allow_html=True
)

# ---------- FLOATING SHAPES ----------
st.markdown("""
<div class="float-shape shape1"></div>
<div class="float-shape shape2"></div>
""", unsafe_allow_html=True)

# ---------- CHARACTER ----------
st.markdown(
    f"""
    <div class="character-fixed">
        <img class="character-gif"
             src="data:image/gif;base64,{gif_base64}">
    </div>
    """,
    unsafe_allow_html=True
)

# ---------- CONTENT ----------
st.markdown("""
<div class="product-title">
    <a href="pages/about.py" target="_self">Hindi to ISL Machine</a>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="product-description">
    <a href="pages/about.py" target="_self">
        Bridging the gap between spoken Hindi and Indian Sign Language (ISL) —
        making communication seamless, inclusive, and accessible.<br><br>
        <em>↗ Click to learn more</em>
    </a>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# Button
col1, _ = st.columns([3,8])
with col1:
    if st.button("Translate Hindi to ISL"):
        st.switch_page("pages/main.py")

# ---------- BOTTOM BAR ----------
st.markdown("""
<div class="bottom-bar">
    <span>✨ Welcome • Hindi to ISL Translator • Inclusive Communication • Accessibility First ✨</span>
</div>
""", unsafe_allow_html=True)