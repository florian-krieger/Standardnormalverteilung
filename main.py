import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats as stats

"""
# Die Standardnormalverteilung

"""

with st.sidebar:
    """
    # Eingabe $$z$$-Wert(e)
    
    Bitte geben Sie ihr gewünschten $$z$$-Wert bzw. den Bereich zwischen zwei $$z$$-Werten ein. 
    """

    all_modes = ["Linksseitig vom z-Wert",
                 "Rechtsseitig vom z-Wert",
                 "Zwischen zwei z-Werten"]

    mode = st.radio(
        "Welcher Art?",
        (all_modes[0],
         all_modes[1],
         all_modes[2])
    )

    if mode == all_modes[0]:
        upper_z = st.slider('Oberer z-Wert', -3.0, 3.0, value=0.0, step=0.01)
        p = stats.norm(0, 1).cdf(upper_z)
        lower_z = -3.0  # only for visual purposes

    elif mode == all_modes[1]:
        lower_z = st.slider('Unterer z-Wert', -3.0, 3.0, value=0.0, step=0.01)
        p = 1 - stats.norm(0, 1).cdf(lower_z)
        upper_z = 3.0  # only for visual purposes

    else:
        lower_z, upper_z  = st.slider('Untere und oberer z-Wert', -3.0, 3.0, value=(-1.0, 1.0), step=0.01)
        p = stats.norm(0, 1).cdf(upper_z) - stats.norm(0, 1).cdf(lower_z)

# data for normal distribution
x = np.linspace(-3, 3, 1000)
N_10 = stats.norm(0, 1)
area = np.arange(lower_z,
                 upper_z,
                 .001)

# plot
fig, ax = plt.subplots()

ax.plot(x, N_10.pdf(x), '#FF4C4F')

ax.fill_between(area,
                N_10.pdf(area),
                color='#FFB5B6')

plt.xlabel("z-Wert")
plt.ylabel("Wahrscheinlichkeitsdichte")
plt.yticks([])

st.pyplot(fig)

st.write("Wahrscheinlichkeit ist: **{:.2f}**".format(p))
