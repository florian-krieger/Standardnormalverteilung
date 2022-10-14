import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats as stats

"""
# Die Standardnormalverteilung

"""

# slider
lower_quantil = st.slider('Untere Grenze', -3.0, 3.0, 0.01)
upper_quantil = st.slider('Obere Grenze', -3.0, 3.0, 0.01)

p = stats.norm(0, 1).cdf(upper_quantil) - stats.norm(0, 1).cdf(lower_quantil)

# data for normal distribution
x = np.linspace(-3, 3, 1000)
N_10 = stats.norm(0, 1)
area = np.arange(lower_quantil,
                 upper_quantil,
                 .001)

# plot
fig, ax = plt.subplots()

ax.plot(x, N_10.pdf(x), '#FF4C4F')

ax.fill_between(area,
                N_10.pdf(area),
                color='#FFB5B6')
st.pyplot(fig)


st.write("Wahrscheinlichkeit ist: **{:.2f}**".format(p))
