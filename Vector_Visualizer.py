import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from streamlit_extras.colored_header import colored_header

# Function to visualize vectors
def visualize_vectors(vectors):
    fig, ax = plt.subplots()
    
    # Create a Cartesian coordinate system
    ax.axhline(y=0, color='k')
    ax.axvline(x=0, color='k')
    
    for i, (length, angle_degrees, color) in enumerate(vectors):
        angle_radians = np.deg2rad(angle_degrees)
        x = length * np.cos(angle_radians)
        y = length * np.sin(angle_radians)
        
        ax.quiver(0, 0, x, y, angles='xy', scale_units='xy', scale=1, color=color,
                  label=f"Vector {i + 1} ({round(length, 2)}, {round(angle_degrees, 2)}°)")

    max_length = max([v[0] for v in vectors])
    ax.set_xlim(-max_length, max_length)
    ax.set_ylim(-max_length, max_length)
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.legend()
    return fig

show = False

# Streamlit app

st.set_page_config("Vector visualizer💻📌", None, "wide")

hide_streamlit_style = """
            <style>
            footer {visibility: hidden;}
            p {font-size: 1.1rem;}
            h3 {font-size: calc(1.6rem + .6vw);}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center;   font-size: 3.5rem;'>Vector Visualizer</h1>", unsafe_allow_html=True)

col1, col2 = st.columns(2, gap="large")

with col1:
  colored_header(label="Vectors Detail🎯",
               description='', color_name="red-80")
  num_vectors = st.number_input("Enter the number of vectors:", min_value=1, value=1, step=1)

  vectors = []
  for i in range(num_vectors):
      with st.expander(f"Vector {i + 1}"):
        length = st.number_input(f"Length of Vector {i + 1}:", min_value=0.1, step=0.1)
        angle = st.number_input(f"Angle of Vector {i + 1} (in degrees):", min_value=0.0, step=1.0)
        color = st.color_picker(f"Color of Vector {i + 1}:")

      vectors.append((length, angle, color))


with col2:
    colored_header(label="Vectors Visualization🚀",
                description='', color_name="red-80")
    st.pyplot(visualize_vectors(vectors), use_container_width=True)

st.divider()