import streamlit as st
import pandas as pd
import plotly.express as px

# Page Setup
st.set_page_config(
    page_title="OIL HSSE • SIF-AI Safety Dashboard",
    page_icon="🛡️",
    layout="wide"
)

# Header
st.title("🛡️ OIL HSSE • SIF-AI Safety Incident Triage")
st.caption("Automated SIF-Potential Detection & IOGP Life-Saving Rules Mapping")

st.divider()

# 1. Top KPI Metric Overview
col1, col2, col3, col4 = st.columns(4)
col1.metric(label="Total Safety Logs", value="148", delta="12 new today")
col2.metric(label="SIF-Potential Precursors", value="31 (20.9%)", delta="High Risk", delta_color="inverse")
col3.metric(label="Top IOGP Trigger", value=" oil implanting")
col4.metric(label="Critical Focus Asset", value="Rig #04 (delhi)")

st.divider()

# 2. Main Workspace (2 Columns: Live Classifier & Analytics)
left_col, right_col = st.columns([1, 1])

with left_col:
    st.subheader("🔍 Live Incident Triage Simulator")
    st.write("Enter an unsafe condition / near-miss report below to evaluate fatal risk:")
    
    sample_text = (
        "During night shift workover at Rig #04, high-pressure hydraulic line was opened "
        "without secondary lockout-tagout or bleeding pressure."
    )
    user_input = st.text_area("Observation Report Text:", value=sample_text, height=130)
    
    if st.button("🚀 Analyze Incident Risk", type="primary", use_container_width=True):
        st.write("---")
        # Beginner rule logic for prototype demo
        is_sif = any(word in user_input.lower() for word in ["pressure", "height", "lockout", "gas", "confined", "fall", "wire"])
        
        if is_sif:
            st.error("🚨 **CRITICAL: SIF-POTENTIAL DETECTED**")
            st.markdown("""
            * **Mapped IOGP Life-Saving Rule:** `Energy Isolation` / `Line of Fire`
            * **High-Energy Source:** Hydraulic / Pressurized Fluid
            * **Compromised Barrier:** Lockout-Tagout (LOTO) & Depressurization Procedure
            """)
        else:
            st.success("✅ **LOW RISK / NON-SIF**")
            st.markdown("""
            * **Mapped IOGP Rule:** `General Workplace Housekeeping`
            * **Action:** Standard monthly review
            """)
            
        # Human-In-The-Loop Validation
        st.caption("HSE Officer Verification:")
        btn_col1, btn_col2 = st.columns(2)
        btn_col1.button("✓ Agree with AI", use_container_width=True)
        btn_col2.button("✗ Override AI", use_container_width=True)

with right_col:
    st.subheader("📊 SIF Precursor Breakdown")
    
    # Mock Data for IOGP Rules
    chart_data = pd.DataFrame({
        "IOGP Rule": ["Energy Isolation", "Line of Fire", "Working at Height", "Confined Space", "Hot Work"],
        "SIF Precursor Count": [14, 9, 5, 2, 1]
    })
    
    fig = px.bar(
        chart_data, 
        x="SIF Precursor Count", 
        y="IOGP Rule", 
        orientation="h",
        color="SIF Precursor Count",
        color_continuous_scale="Reds",
        title="Top Compromised Life-Saving Rules"
    )
    fig.update_layout(height=350, margin=dict(l=20, r=20, t=40, b=20))
    st.plotly_chart(fig, use_container_width=True)

st.divider()

# 3. Batch Incident Table
st.subheader("📋 Recent High-Risk Safety Observations")
mock_table = pd.DataFrame({
    "Report ID": ["OIL-2026-881", "OIL-2026-882", "OIL-2026-883", "OIL-2026-884"],
    "Rig / Site": ["Rig #04 (Moran)", "Wellhead #12", "Duliajan Plant", "Rig #02 (Digboi)"],
    "Observation Summary": [
        "Hydraulic line disconnected under residual pressure",
        "Tripping hazard near walkway stairs",
        "Confined space entry permit expired by 2 hours",
        "Missing safety latch on main hoisting crane hook"
    ],
    "Classification": ["SIF-Potential", "Non-SIF", "SIF-Potential", "SIF-Potential"],
    "IOGP Rule": ["Energy Isolation", "Housekeeping", "Confined Space", "Safe Mechanical Lifting"]
})
st.dataframe(mock_table, use_container_width=True)
