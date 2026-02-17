import streamlit as st
from app.graphs.research_graph import build_graph
from app.memory_manager import load_memory, save_memory, clear_memory
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from io import BytesIO
from langchain_classic.memory import ConversationBufferMemory

# ---------- Page Config ----------
st.set_page_config(
    page_title="AI Research Copilot",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------- Custom CSS ----------
st.markdown("""
<style>
    .main {
        padding-top: 1rem;
    }
    .stTitle {
        color: #1f77b4;
        font-size: 2.5rem;
    }
    .stSubheader {
        color: #1f77b4;
    }
</style>
""", unsafe_allow_html=True)

# ---------- Helpers ----------
def load_graph(memory, model, temperature, research_depth):
    return build_graph(memory, model=model, temperature=temperature, research_depth=research_depth)

def generate_pdf(text: str) -> bytes:
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer)
    styles = getSampleStyleSheet()
    story = []
    for block in text.split("\n"):
        story.append(Paragraph(block, styles['BodyText']))
        story.append(Spacer(1, 8))
    doc.build(story)
    return buffer.getvalue()

# ---------- Session State Initialization ----------
if "memory_initialized" not in st.session_state:
    persistent_memory = load_memory()
    st.session_state.history = persistent_memory.get("history", [])
    st.session_state.messages = persistent_memory.get("messages", [])
    st.session_state.memory_initialized = True

if "history" not in st.session_state:
    st.session_state.history = []

if "messages" not in st.session_state:
    st.session_state.messages = []

if "memory" not in st.session_state:
    st.session_state.memory = ConversationBufferMemory(memory_key="history", output_key="output")

# ---------- SIDEBAR SETTINGS ----------
st.sidebar.title("⚙️ Settings")
st.sidebar.markdown("Configure your research agent")
st.sidebar.markdown("---")

# Model Selection
st.sidebar.subheader("🤖 Model Configuration")
model = st.sidebar.selectbox(
    "Select LLM Model",
    ["gpt-4o-mini", "gpt-4-turbo", "gpt-4o"],
    help="Choose the language model for research"
)

# Temperature Control
st.sidebar.subheader("🌡️ Temperature Control")
temperature = st.sidebar.slider(
    "Temperature (Creativity)",
    min_value=0.0,
    max_value=2.0,
    value=0.0,
    step=0.1,
    help="Lower = precise; Higher = creative"
)

# Research Depth Toggle
st.sidebar.subheader("🔍 Research Depth")
research_depth = st.sidebar.radio(
    "Select research depth",
    ["quick", "balanced", "deep"],
    help="""
    - Quick: Fast, concise answers
    - Balanced: Standard research
    - Deep: Thorough analysis with multiple sources
    """
)

# Display Research Depth Description
depth_descriptions = {
    "quick": "⚡ Quick answers with minimal tool usage",
    "balanced": "⚖️ Balanced research using multiple sources",
    "deep": "🔬 Deep analysis with cross-referenced sources"
}
st.sidebar.info(f"Mode: {depth_descriptions[research_depth]}")

st.sidebar.markdown("---")

# Memory & History Section
st.sidebar.subheader("💾 History Management")
col1, col2 = st.sidebar.columns(2)

with col1:
    if st.button("📋 View Stats", use_container_width=True):
        st.sidebar.metric("Total Queries", len(st.session_state.history))
        st.sidebar.metric("Messages", len(st.session_state.messages))

with col2:
    if st.button("🗑️ Clear All", use_container_width=True):
        st.session_state.history = []
        st.session_state.messages = []
        st.session_state.memory.clear()
        clear_memory()
        st.rerun()

st.sidebar.markdown("---")

# Footer
st.sidebar.markdown("### 📚 About")
st.sidebar.markdown("""
**AI Research Copilot**

An autonomous research agent powered by LangGraph + RAG.

**Built by:** Emmanuel Chukwu
""")

# ---------- Main Content Area ----------
st.title("🧠 AI Research Copilot")
st.markdown("""
Ask research questions and get structured reports. The agent remembers conversations and adapts to your settings.
""")

# Display Current Settings
with st.expander("📊 Current Settings", expanded=False):
    col1, col2, col3 = st.columns(3)
    col1.metric("Model", model)
    col2.metric("Temperature", temperature)
    col3.metric("Depth", research_depth.capitalize())

st.markdown("---")

# ---------- Chat Interface ----------
# Query Input
query = st.chat_input("Ask a research question...", key="query_input")

# Display Chat History
st.subheader("💬 Conversation")
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ---------- Process Query ----------
if query:
    # Add user message
    st.session_state.messages.append({"role": "user", "content": query})
    
    # Display user message
    with st.chat_message("user"):
        st.markdown(query)

    # Load graph with settings
    graph = load_graph(st.session_state.memory, model, temperature, research_depth)

    # Run agent
    with st.spinner(f"🔄 Researching ({research_depth} depth)... This may take 10-30 seconds ⏳"):
        result = graph.invoke({"input": query})

    report = result["output"]

    # Add assistant message
    st.session_state.messages.append({"role": "assistant", "content": report})
    
    # Display assistant message
    with st.chat_message("assistant"):
        st.markdown(report)

    # Save to history
    st.session_state.history.append({"query": query, "report": report})
    
    # Persist memory to disk
    save_memory(st.session_state.messages, st.session_state.history)

    # Rerun to update display
    st.rerun()

# ---------- Research History Section ----------
st.markdown("---")
st.subheader("📜 Research History")

if st.session_state.history:
    # History filters
    col1, col2 = st.columns([3, 1])
    with col1:
        search_term = st.text_input("🔎 Search history...", placeholder="Filter by query text")
    
    # Filter history
    filtered_history = [
        item for item in st.session_state.history
        if search_term.lower() in item['query'].lower()
    ] if search_term else st.session_state.history

    # Display history
    for idx, item in enumerate(reversed(filtered_history)):
        with st.expander(f"🔎 {item['query'][:60]}...", expanded=False):
            st.markdown(item["report"])
            
            # PDF Download Button
            pdf_data = generate_pdf(item["report"])
            st.download_button(
                label="📥 Download PDF",
                data=pdf_data,
                file_name=f"AI_research_report_{idx}.pdf",
                mime="application/pdf",
                key=f"download_{idx}"
            )
else:
    st.info("📭 No research history yet. Ask a question to get started!")
