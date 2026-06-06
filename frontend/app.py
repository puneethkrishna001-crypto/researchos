import sys
import os
import time

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import streamlit as st

from graph.research_graph import research_graph
from output.pdf_generator import create_pdf

def show_source_cards():

    st.subheader("🔗 Source Explorer")

    sources = [
        "Web Search",
        "Web Scraper",
        "ChromaDB Memory",
        "Qwen 2.5 LLM"
    ]

    for source in sources:

        st.markdown(
            f"""
            <div class="source-card">
                <h4>{source}</h4>
                <p>Used during report generation</p>
            </div>
            """,
            unsafe_allow_html=True
        )
        
st.set_page_config(
    page_title="ResearchOS",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>

.stApp {
    background-color: #0b1120;
}

.main {
    color: white;
}

h1,h2,h3,h4,h5,h6 {
    color: white !important;
}

p, label, span {
    color: #d1d5db !important;
}

[data-testid="stSidebar"] {
    background-color: #111827;
}

[data-testid="stMetricValue"] {
    color: #60a5fa;
}

[data-testid="stMetricLabel"] {
    color: white;
}

.stTextInput input {
    background-color: #1f2937;
    color: white;
    border-radius: 10px;
}

.stButton button {
    width: 100%;
    border-radius: 10px;
    background-color: #2563eb;
    color: white;
    border: none;
    height: 3rem;
    font-weight: bold;
}

.stButton button:hover {
    background-color: #1d4ed8;
}

.agent-card {
    background-color: #111827;
    padding: 15px;
    border-radius: 12px;
    border: 1px solid #374151;
}

.source-card {
    background-color: #111827;
    padding: 15px;
    border-radius: 12px;
    border: 1px solid #374151;
    margin-bottom: 10px;
}

.arch-card {
    background-color: #111827;
    padding: 20px;
    border-radius: 12px;
    border: 1px solid #374151;
}

</style>
""", unsafe_allow_html=True)

if "history" not in st.session_state:
    st.session_state.history = []

if "latest_report" not in st.session_state:
    st.session_state.latest_report = ""

if "latest_query" not in st.session_state:
    st.session_state.latest_query = ""

with st.sidebar:

    st.title("🧠 ResearchOS")

    st.markdown("---")

    st.subheader("Research Mode")

    mode = st.selectbox(
        "Mode",
        [
            "Quick Research",
            "Deep Research",
            "Academic Research",
            "Market Research"
        ]
    )

    st.markdown("---")

    st.subheader("System Status")

    st.success("Memory Active")
    st.success("LangGraph Active")
    st.success("Qwen 2.5 Active")

    st.markdown("---")

    st.subheader("Recent Research")

    if len(st.session_state.history) == 0:
        st.caption("No research yet")
    else:
        for item in st.session_state.history[-10:][::-1]:
            st.write("•", item)

st.title("🚀 ResearchOS")

st.caption("Multi-Agent AI Research Platform")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Agents",
        "4"
    )

with col2:
    st.metric(
        "Memory",
        "Enabled"
    )

with col3:
    st.metric(
        "Model",
        "Qwen 2.5"
    )

st.markdown("---")

query = st.text_input(
    "Research Topic",
    placeholder="Example: Impact of AI on Healthcare in 2025"
)

generate = st.button(
    "Generate Research Report",
    use_container_width=True
)

if generate:

    if query.strip() == "":
        st.warning("Please enter a research topic")
        st.stop()

    if query not in st.session_state.history:
        st.session_state.history.append(query)

    st.markdown("## Agent Activity Center")

    memory_status = st.empty()
    researcher_status = st.empty()
    summarizer_status = st.empty()
    critic_status = st.empty()
    writer_status = st.empty()

    memory_status.info("🧠 Memory Agent Running")
    time.sleep(0.5)

    researcher_status.info("🔍 Research Agent Running")
    time.sleep(0.5)

    summarizer_status.info("📝 Summarizer Agent Running")
    time.sleep(0.5)

    critic_status.info("🧐 Critic Agent Running")
    time.sleep(0.5)

    writer_status.info("📄 Writer Agent Running")

    start_time = time.time()

    result = research_graph.invoke(
        {
            "query": query
        }
    )

    execution_time = round(
        time.time() - start_time,
        2
    )

    st.session_state.latest_report = result["report"]
    st.session_state.latest_query = query

    memory_status.success("🧠 Memory Agent Complete")
    researcher_status.success("🔍 Research Agent Complete")
    summarizer_status.success("📝 Summarizer Agent Complete")
    critic_status.success("🧐 Critic Agent Complete")
    writer_status.success("📄 Writer Agent Complete")

    st.markdown("---")

    m1, m2, m3, m4 = st.columns(4)

    with m1:
        st.metric(
            "Execution Time",
            f"{execution_time}s"
        )

    with m2:
        st.metric(
            "Sources",
            "3+"
        )

    with m3:
        st.metric(
            "Memory",
            "Used"
        )

    with m4:
        st.metric(
            "Status",
            "Complete"
        )

    st.markdown("---")

    tab1, tab2, tab3 = st.tabs(
        [
            "📄 Report",
            "💡 Insights",
            "🏗 Architecture"
        ]
    )

    with tab1:

        st.subheader("Generated Research Report")

        st.markdown(result["report"])

        pdf_path = create_pdf(
            result["report"],
            "research_report.pdf"
        )

        with open(pdf_path, "rb") as pdf:
            pdf_bytes = pdf.read()

        st.download_button(
            label="📥 Download PDF",
            data=pdf_bytes,
            file_name="research_report.pdf",
            mime="application/pdf"
        )

    with tab2:

        st.subheader("Key Insights")

        st.success("Research completed successfully")

        st.info(
            "Generated using multi-agent workflow with memory, summarization, validation and report generation."
        )

        st.metric(
            "Topic",
            query
        )

        st.metric(
            "Execution Time",
            f"{execution_time}s"
        )

    with tab3:

        st.subheader("System Workflow")

        st.code(
"""
Memory
   ↓
Researcher
   ↓
Summarizer
   ↓
Critic
   ↓
Writer
   ↓
Final Report
"""
        )