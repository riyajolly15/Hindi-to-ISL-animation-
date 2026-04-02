import streamlit as st

def load_css():
    st.markdown(
        """
        <style>
        /* ===== GLOBAL APP STYLES ===== */
        :root {
            --bottombar-height: 52px;
            --mint: #A8E6CE;
            --sage: #DCEDC2;
            --peach: #FFD3B5;
            --coral: #FFAAA6;
            --salmon: #FF8C94;
        }

        .stApp {
            background: linear-gradient(135deg, #DCEDC2 0%, #FFD3B5 100%);
            padding-bottom: var(--bottombar-height);
        }

        /* Headings */
        h1 {
            color: #2d3748;
            font-weight: 800;
            font-size: 3rem;
            letter-spacing: -0.5px;
        }

        h3 {
            color: #FF8C94;
            font-size: 1.8rem;
            font-weight: 700;
        }

        label {
            color: #e85d6c !important;
            font-weight: 600;
            font-size: 1.2rem;
            letter-spacing: 0.3px;
        }

        /* ===== BOTTOM BAR STYLES ===== */
        .top-bar {
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            height: var(--bottombar-height);
            background: linear-gradient(90deg, #FF8C94, #FFAAA6, #FFD3B5, #FFAAA6, #FF8C94);
            background-size: 200% 100%;
            animation: gradientShift 8s ease infinite;
            color: #2d3748 !important;
            font-weight: 700;
            display: flex;
            align-items: center;
            justify-content: center;
            z-index: 999999;
            overflow: hidden;
            text-align: center;
            border-top: 3px solid #FF8C94;
            box-shadow: 0 -4px 20px rgba(255, 140, 148, 0.3);
        }

        @keyframes gradientShift {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }

        .top-bar span {
            display: inline-block;
            white-space: nowrap;
            animation: moveText 15s linear infinite;
            font-size: 1.1rem;
        }

        @keyframes moveText {
            from { transform: translateX(100%); }
            to   { transform: translateX(-100%); }
        }

        /* ===== FLOATING BACKGROUND SHAPES ===== */
        .float-shape {
            position: fixed;
            opacity: 0.25;
            filter: blur(80px);
            animation: float 12s ease-in-out infinite;
            z-index: -1;
        }

        /* Sharp-edged shapes */
        .shape1 {
            width: 280px;
            height: 280px;
            background: #A8E6CE;
            top: 15%;
            left: 3%;
            border-radius: 4px;
            transform: rotate(15deg);
        }

        .shape2 {
            width: 320px;
            height: 320px;
            background: #FF8C94;
            bottom: 15%;
            right: 3%;
            animation-delay: 4s;
            border-radius: 4px;
            transform: rotate(-10deg);
        }

        .shape3 {
            width: 200px;
            height: 200px;
            background: #FFAAA6;
            top: 50%;
            right: 15%;
            animation-delay: 2s;
            border-radius: 4px;
            transform: rotate(25deg);
        }

        @keyframes float {
            0%, 100% { transform: translateY(0px) rotate(15deg); }
            50%      { transform: translateY(-25px) rotate(15deg); }
        }

        /* ===== UNIVERSAL BUTTON STYLE ===== */
        button {
            background: linear-gradient(135deg, #FF8C94, #FFAAA6) !important;
            color: #2d3748 !important;
            font-size: 18px !important;
            font-weight: 700 !important;
            padding: 14px 28px !important;
            border-radius: 4px !important;
            border: 2px solid #FF8C94 !important;
            box-shadow: 4px 4px 0px #e07a82;
            transition: all 0.15s ease !important;
            width: 100%;
            text-transform: uppercase;
            letter-spacing: 1px;
        }

        button:hover {
            transform: translate(-2px, -2px) !important;
            box-shadow: 6px 6px 0px #e07a82 !important;
            background: linear-gradient(135deg, #FFAAA6, #FFD3B5) !important;
        }

        button:active {
            transform: translate(2px, 2px) !important;
            box-shadow: 2px 2px 0px #e07a82 !important;
        }

        /* ===== CARD STYLES ===== */
        .card {
            background-color: #ffffff;
            padding: 28px;
            border-radius: 4px;
            border: 2px solid #A8E6CE;
            box-shadow: 6px 6px 0px #8ed4b8;
        }

        /* ===== TEXTAREA STYLES ===== */
        textarea {
            background-color: #fefefe !important;
            color: #2d3748 !important;
            font-size: 18px !important;
            border-radius: 4px !important;
            border: 2px solid #DCEDC2 !important;
            box-shadow: inset 0 2px 4px rgba(0,0,0,0.04);
            transition: border-color 0.2s ease, box-shadow 0.2s ease;
        }

        textarea:focus {
            border-color: #A8E6CE !important;
            box-shadow: 0 0 0 3px rgba(168, 230, 206, 0.3) !important;
            outline: none !important;
        }

        /* ===== INPUT FIELDS ===== */
        input[type="text"], input[type="number"], select {
            border-radius: 4px !important;
            border: 2px solid #DCEDC2 !important;
            padding: 12px !important;
            font-size: 16px !important;
            transition: border-color 0.2s ease;
        }

        input[type="text"]:focus, input[type="number"]:focus, select:focus {
            border-color: #A8E6CE !important;
            box-shadow: 0 0 0 3px rgba(168, 230, 206, 0.3) !important;
        }

        /* ===== SCROLLBAR ===== */
        ::-webkit-scrollbar {
            width: 10px;
        }

        ::-webkit-scrollbar-track {
            background: #DCEDC2;
        }

        ::-webkit-scrollbar-thumb {
            background: #FFAAA6;
            border-radius: 2px;
        }

        ::-webkit-scrollbar-thumb:hover {
            background: #FF8C94;
        }

        /* ===== SELECTION HIGHLIGHT ===== */
        ::selection {
            background: #A8E6CE;
            color: #2d3748;
        }
        </style>

        <div class="top-bar">
            <span>✨ Welcome • Hindi to ISL Translator • Inclusive Communication • Accessibility First ✨</span>
        </div>
        <div class="float-shape shape1"></div>
        <div class="float-shape shape2"></div>
        <div class="float-shape shape3"></div>
        """,
        unsafe_allow_html=True
    )