import streamlit as st

st.set_page_config(page_title="Maturalny Quiz z Matematyki", page_icon="📘")

st.title("📘 Maturalny Quiz z Matematyki (1 pkt każde)")

st.markdown("Wybierz poprawne odpowiedzi do poniższych zadań.")

score = 0  # Licznik punktów

with st.form("quiz_form"):
    ### ZADANIE 1 ###
    st.markdown("#### Zadanie 1")
    st.latex(r"\left( \sqrt{32} - \sqrt{2} \right)^2")
    q1 = st.radio("Odpowiedź:", ["A. 16", "B. 18", "C. 30", "D. 34"], key="q1")

    with st.expander("Pokaż rozwiązanie"):
        st.latex(r"""
        \left( \sqrt{32} - \sqrt{2} \right)^2 = 
        \left( 4\sqrt{2} - \sqrt{2} \right)^2 =
        \left( 3\sqrt{2} \right)^2 = 9 \cdot 2 = 18
        """)

    ### ZADANIE 2 ###
    st.markdown("#### Zadanie 2")
    st.latex(r"\frac{5^{12} + 5^{13} + 5^{14}}{5^{12}}")
    q2 = st.radio("Odpowiedź:", ["A. 30", "B. 31", "C. $5^{12}$", "D. $5^{27}$"], key="q2")

    with st.expander("Pokaż rozwiązanie"):
        st.latex(r"""
        \frac{5^{12} + 5^{13} + 5^{14}}{5^{12}} =
        \frac{5^{12}(1 + 5 + 25)}{5^{12}} = 1 + 5 + 25 = 31
        """)

    ### ZADANIE 3 ###
    st.markdown("#### Zadanie 3")
    st.latex(r"\log_3 108 - 2\log_3 2")
    q3 = st.radio("Odpowiedź:", ["A. 3", "B. 9", "C. \log_3 104", "D. 2\log_3 54"], key="q3")

    with st.expander("Pokaż rozwiązanie"):
        st.latex(r"""
        \log_3 108 - 2\log_3 2 =
        \log_3 108 - \log_3 2^2 =
        \log_3 108 - \log_3 4 =
        \log_3 \left( \frac{108}{4} \right) =
        \log_3 27 = 3
        """)

    submitted = st.form_submit_button("Sprawdź odpowiedzi")

if submitted:
    # Sprawdzanie poprawnych odpowiedzi
    if q1.startswith("B"): score += 1
    if q2.startswith("B"): score += 1
    if q3.startswith("B"): score += 1


    st.success(f"Twój wynik: {score}/3 punktów")

    if score == 3:
        st.balloons()
        st.markdown("🎉 **Świetna robota! Wszystkie odpowiedzi poprawne.**")
    elif score == 1:
        st.warning("✅ Jedna odpowiedź poprawna. Spróbuj ponownie!")
    else:
        st.error("❌ Żadna odpowiedź nie jest poprawna. Powtórz materiał.")

    st.markdown("---")
    st.caption("Quiz został przygotowany na podstawie zadań maturalnych z matematyki.")

