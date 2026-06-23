import streamlit as st
from rag import build_rag_chain

st.set_page_config(page_title="Solar Feasibility Assistant", page_icon="☀️", )

st.title("Solar Energy Feasibility Assistant")
st.caption("AI- powered RAG assistant for solar adoption guidance | project for 1M1B - IBM SkillsBuild Internship")

@st.cache_resource

def get_chain():
    return build_rag_chain()

chain = get_chain()

st.markdown("### Tell us about your situation")

col1, col2 = st.columns(2)

with col1:
    location = st.text_input("Location", placeholder="e.g. Hyderabad, Telangana")
    rooftop_area = st.number_input("Rooftop size (in sq ft)", min_value=50, max_value=5000, value=500)
with col2:
    monthly_bill = st.number_input("Monthly electricity bill (in INR)", min_value=500, max_value=50000, value=3000)
    applliances = st.text_input("What do you want to power", placeholder="e.g. lights, fan, water pump")

if st.button("Check Feasibility", type="primary"):
    query = (
        f"I have a {rooftop_area} sq ft rooftop in {location}. "
        f"Monthly electricity bill in INR {monthly_bill}."
        f"I want to power {applliances}. "
        f"What solar system do i need and what government schemes can i use?"

    )

    with st.spinner("Analysing your solar feasability..."):
        try:
            answer  = chain.invoke(query)
            st.markdown("### Feasability report")
            st.markdown(answer)

        except Exception as e:
            st.error(f"Something went wrong: {e}")



st.divider()
st.caption("Build with IBM Granite, LangChain, ChromaDB | Solar Feasability Assistant")