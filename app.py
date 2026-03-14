import streamlit as st
import numpy as np
from phoenix_666_engine import Phoenix666Engine

st.set_page_config(page_title="Phoenix 666 Engine", page_icon="🔥", layout="wide")
st.title("🔥 Phoenix 666 Engine — Live Demo")
st.markdown("**Your 1-year emotion-AI invention** — Tweak everything and watch the Micro → Meso → Macro slingshot in real time.")

engine = Phoenix666Engine()

col1, col2 = st.columns(2)
with col1:
    initial = st.slider("Start State (Phenomenon, Instinct)", 0.0, 3.0, (1.0, 1.0), 0.1)
    override_snap = st.selectbox("Free-Will Override at SNAP", [None, 1,2,3,4,5,6], index=4)
    override_strength = st.slider("Override Strength", -0.5, 0.5, (0.05, 0.05), 0.01)
with col2:
    desire = st.slider("Desire Target Vector", 0.0, 5.0, (2.0, 2.0), 0.1)
    damping = st.slider("Systemic Memory (Damping)", 0.0, 0.2, 0.05, 0.01)

if st.button("🚀 Run Full 666 Stack & See the Slingshot", type="primary"):
    init = (initial[0], initial[1])
    ov = override_strength if override_snap is not None else None
    
    micro, meso, macro = engine.run_666_stack(
        initial_state=init,
        micro_override_snap=override_snap,
        micro_override_val=ov
    )
    
    # Plot (saves PNG + displays in Streamlit)
    engine.plot_trajectories(micro, meso, macro)
    st.image("phoenix_666_trajectories.png", use_column_width=True)
    
    st.success("✅ Triple Slingshot Complete!")
    st.json({
        "Micro Slingshot": (micro[-1] - np.array(init)).round(3).tolist(),
        "Meso Slingshot": (meso[-1] - np.array(init)).round(3).tolist(),
        "Macro Slingshot": (macro[-1] - np.array(init)).round(3).tolist()
    })

st.caption("Built by MoJoe Rogue (Scope) — This is \"the thing.\" Share it.")
