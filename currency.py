import streamlit as st
import requests

# ==========================================
# PAGE CONFIGURATION
# ==========================================
st.set_page_config(
    page_title="Jayasri's Currency Converter",
    page_icon="💱",
    layout="centered"
)

# ==========================================
# CUSTOM CSS
# ==========================================
st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
}

/* ==========================================
   MAIN BACKGROUND
   ========================================== */
.stApp {
    background:
        radial-gradient(circle at 5% 5%, #dbeafe 0%, transparent 28%),
        radial-gradient(circle at 95% 10%, #fce7f3 0%, transparent 28%),
        radial-gradient(circle at 50% 100%, #ccfbf1 0%, transparent 30%),
        linear-gradient(135deg, #f8fbff, #eef7ff, #fff7fb);
}

/* ==========================================
   MAIN CONTAINER
   ========================================== */
.block-container {
    max-width: 850px;
    padding-top: 35px;
    padding-bottom: 40px;
}

/* ==========================================
   MAIN TITLE
   ========================================== */
.main-title {
    text-align: center;
    font-size: 42px;
    font-weight: 800;

    background: linear-gradient(
        90deg,
        #0891b2,
        #2563eb,
        #db2777
    );

    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;

    margin-bottom: 5px;
}

/* ==========================================
   SUBTITLE
   ========================================== */
.subtitle {
    text-align: center;
    color: #475569;
    font-size: 16px;
    font-weight: 500;
    margin-bottom: 30px;
}

/* ==========================================
   MAIN CARD
   ========================================== */
.converter-card {
    background: rgba(255, 255, 255, 0.88);

    border: 1px solid rgba(37, 99, 235, 0.15);

    border-radius: 25px;

    padding: 30px;

    box-shadow:
        0 15px 45px rgba(37, 99, 235, 0.12),
        0 5px 20px rgba(219, 39, 119, 0.08);
}

/* ==========================================
   SECTION TITLE
   ========================================== */
.section-title {
    text-align: center;
    color: #1e293b;
    font-size: 22px;
    font-weight: 700;
    margin-bottom: 20px;
}

/* ==========================================
   INPUT LABELS
   ========================================== */
.stNumberInput label,
.stSelectbox label {
    color: #334155 !important;
    font-weight: 600 !important;
}

/* ==========================================
   INPUT BOXES
   ========================================== */
.stNumberInput input {
    background-color: #ffffff !important;
    color: #1e293b !important;
    border: 2px solid #bfdbfe !important;
    border-radius: 12px !important;
}

/* ==========================================
   SELECT BOX
   ========================================== */
.stSelectbox div[data-baseweb="select"] > div {
    background-color: #ffffff !important;
    color: #1e293b !important;
    border: 2px solid #bfdbfe !important;
    border-radius: 12px !important;
}

/* ==========================================
   CONVERT BUTTON
   ========================================== */
.stButton > button {
    width: 100%;

    border-radius: 15px;

    border: none;

    background: linear-gradient(
        90deg,
        #0891b2,
        #2563eb,
        #db2777
    );

    color: white;

    font-size: 17px;

    font-weight: 700;

    padding: 13px;

    box-shadow:
        0 8px 25px rgba(37, 99, 235, 0.25);

    transition: all 0.25s ease;
}

/* Button hover */
.stButton > button:hover {
    transform: translateY(-3px);

    box-shadow:
        0 12px 30px rgba(219, 39, 119, 0.30);
}

/* ==========================================
   RESULT CARD
   ========================================== */
.result-card {
    background:
        linear-gradient(
            135deg,
            rgba(14, 165, 233, 0.12),
            rgba(219, 39, 119, 0.10)
        );

    border: 1px solid rgba(37, 99, 235, 0.15);

    border-radius: 22px;

    padding: 28px;

    margin-top: 25px;

    text-align: center;

    box-shadow:
        0 10px 30px rgba(37, 99, 235, 0.08);
}

/* ==========================================
   RESULT LABEL
   ========================================== */
.result-label {
    color: #64748b;
    font-size: 14px;
    font-weight: 600;
}

/* ==========================================
   RESULT AMOUNT
   ========================================== */
.result-amount {
    color: #1e3a8a;
    font-size: 38px;
    font-weight: 800;
    margin: 10px 0;
}

/* ==========================================
   EXCHANGE RATE BOX
   ========================================== */
.rate-box {
    background: rgba(255, 255, 255, 0.85);

    border: 1px solid #dbeafe;

    border-radius: 15px;

    padding: 15px;

    margin-top: 15px;

    color: #334155;

    box-shadow:
        0 5px 15px rgba(37, 99, 235, 0.06);
}

/* ==========================================
   INFORMATION CARDS
   ========================================== */
.info-card {
    background: rgba(255, 255, 255, 0.90);

    border: 1px solid #dbeafe;

    border-radius: 18px;

    padding: 18px;

    text-align: center;

    box-shadow:
        0 8px 20px rgba(37, 99, 235, 0.07);
}

/* ==========================================
   INFORMATION TITLE
   ========================================== */
.info-title {
    color: #64748b;
    font-size: 13px;
    font-weight: 600;
}

/* ==========================================
   INFORMATION VALUE
   ========================================== */
.info-value {
    color: #1e40af;
    font-size: 20px;
    font-weight: 700;
    margin-top: 5px;
}

/* ==========================================
   FOOTER
   ========================================== */
.footer {
    text-align: center;

    color: #64748b;

    font-size: 13px;

    margin-top: 25px;
}

</style>
""", unsafe_allow_html=True)


# ==========================================
# HEADER
# ==========================================
st.markdown(
    '<div class="main-title">💱 JAYASRI\'S CURRENCY CONVERTER</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">🌎 Convert currencies instantly using live exchange rates</div>',
    unsafe_allow_html=True
)


# ==========================================
# CURRENCY DATA
# ==========================================
currencies = {
    "🇮🇳 INR - Indian Rupee": "INR",
    "🇺🇸 USD - US Dollar": "USD",
    "🇪🇺 EUR - Euro": "EUR",
    "🇬🇧 GBP - British Pound": "GBP",
    "🇯🇵 JPY - Japanese Yen": "JPY",
    "🇦🇺 AUD - Australian Dollar": "AUD",
    "🇨🇦 CAD - Canadian Dollar": "CAD",
    "🇨🇭 CHF - Swiss Franc": "CHF",
    "🇸🇬 SGD - Singapore Dollar": "SGD",
    "🇦🇪 AED - UAE Dirham": "AED",
    "🇸🇦 SAR - Saudi Riyal": "SAR",
    "🇰🇷 KRW - South Korean Won": "KRW"
}


# ==========================================
# CONVERTER CARD
# ==========================================
st.markdown(
    '<div class="converter-card">',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-title">💰 CONVERT YOUR MONEY</div>',
    unsafe_allow_html=True
)


# ==========================================
# AMOUNT
# ==========================================
amount = st.number_input(
    "💵 Enter Amount",
    min_value=0.01,
    value=100.0,
    step=1.0
)

st.write("")


# ==========================================
# CURRENCY SELECTION
# ==========================================
col1, col2 = st.columns(2)

with col1:

    from_currency_name = st.selectbox(
        "🌐 From Currency",
        list(currencies.keys()),
        index=0
    )

with col2:

    to_currency_name = st.selectbox(
        "🎯 To Currency",
        list(currencies.keys()),
        index=1
    )


st.write("")


# ==========================================
# CONVERT BUTTON
# ==========================================
convert = st.button(
    "⚡ CONVERT NOW",
    use_container_width=True
)

st.markdown("</div>", unsafe_allow_html=True)


# ==========================================
# CONVERSION
# ==========================================
if convert:

    from_currency = currencies[from_currency_name]
    to_currency = currencies[to_currency_name]

    # Same currency
    if from_currency == to_currency:

        converted_amount = amount
        rate = 1.0

        st.markdown(
            """
            <div class="result-card">
                <div class="result-label">
                    CONVERSION RESULT
                </div>

                <div class="result-amount">
                    1.00 {0}
                </div>

                <div class="rate-box">
                    💱 1 {0} =
                    <strong>1.0000 {0}</strong>
                </div>
            </div>
            """.format(to_currency),
            unsafe_allow_html=True
        )

    else:

        try:

            # ======================================
            # FRANKFURTER API
            # ======================================
            url = (
                "https://api.frankfurter.app/latest"
                f"?amount={amount}"
                f"&from={from_currency}"
                f"&to={to_currency}"
            )

            response = requests.get(
                url,
                timeout=10
            )

            # ======================================
            # SUCCESS
            # ======================================
            if response.status_code == 200:

                data = response.json()

                converted_amount = data["rates"][to_currency]

                # Calculate rate for 1 unit
                rate = converted_amount / amount

                # ==================================
                # RESULT CARD
                # ==================================
                st.markdown(
                    '<div class="result-card">',
                    unsafe_allow_html=True
                )

                st.markdown(
                    '<div class="result-label">'
                    'CONVERSION RESULT'
                    '</div>',
                    unsafe_allow_html=True
                )

                st.markdown(
                    f"""
                    <div class="result-amount">
                        {converted_amount:,.2f} {to_currency}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                st.markdown(
                    f"""
                    <div class="rate-box">
                        💱 1 {from_currency} =
                        <strong>
                            {rate:,.4f} {to_currency}
                        </strong>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                st.markdown(
                    "</div>",
                    unsafe_allow_html=True
                )

                st.write("")

                # ==================================
                # INFORMATION CARDS
                # ==================================
                info1, info2 = st.columns(2)

                with info1:

                    st.markdown(
                        f"""
                        <div class="info-card">

                            <div class="info-title">
                                💵 YOU ENTERED
                            </div>

                            <div class="info-value">
                                {amount:,.2f} {from_currency}
                            </div>

                        </div>
                        """,
                        unsafe_allow_html=True
                    )

                with info2:

                    st.markdown(
                        f"""
                        <div class="info-card">

                            <div class="info-title">
                                💰 YOU RECEIVE
                            </div>

                            <div class="info-value">
                                {converted_amount:,.2f} {to_currency}
                            </div>

                        </div>
                        """,
                        unsafe_allow_html=True
                    )

            # ======================================
            # API ERROR
            # ======================================
            else:

                st.error(
                    "❌ Unable to fetch exchange rates. "
                    "Please try again."
                )

        # ==========================================
        # INTERNET ERROR
        # ==========================================
        except requests.exceptions.RequestException:

            st.error(
                "🌐 Internet connection problem. "
                "Please check your connection and try again."
            )

        # ==========================================
        # OTHER ERROR
        # ==========================================
        except Exception as e:

            st.error(
                f"⚠️ Something went wrong: {e}"
            )


# ==========================================
# FOOTER
# ==========================================
st.markdown(
    """
    <div class="footer">
        💱 Jayasri's Currency Converter
        • Built with ❤️ using Streamlit
    </div>
    """,
    unsafe_allow_html=True
)