# AI Research Agent

An intelligent research assistant powered by LLMs and LangGraph that performs comprehensive research tasks, retrieves information from multiple sources, and generates structured research reports.

## Live Demo
https://emmanuelchukwu-ai-research-agent-app-streamlit-vlvtep.streamlit.app/

## Overview

The AI Research Agent is a sophisticated automation tool designed to conduct autonomous research using multiple data sources and analytical tools. It combines large language models (LLMs) with retrieval-augmented generation (RAG), web search, academic databases, and specialized tools to provide comprehensive, well-sourced answers to research queries.

The project provides both a **command-line interface** and a **Streamlit web application** for interactive research sessions.

## Features

- **Multi-Source Research**: Integrates data from ArXiv, Wikipedia, Google Search, and local vector databases
- **Structured Reports**: Generates organized research reports with introduction, findings, technical explanations, and sources
- **RAG-Enhanced Search**: Uses Pinecone vector database for semantic document retrieval
- **Configurable Research Depth**: Choose between quick answers and deep, thorough research
- **Conversation Memory**: Maintains context across multiple queries with persistent memory management
- **PDF Export**: Generate and download research reports as PDF documents
- **Multiple LLM Support**: Flexible LLM selection with adjustable temperature controls
- **Tool Ecosystem**: Includes calculators, summarizers, and specialized research tools

## Technology Stack

- **LLM Framework**: LangChain + LangGraph
- **Language Models**: OpenAI (GPT-4, GPT-4o, GPT-4o-mini)
- **Vector Database**: Pinecone
- **Web Framework**: Streamlit
- **Data Sources**:
  - ArXiv (academic papers)
  - Wikipedia
  - Google Search (via SerpAPI)
  - Local document embeddings
- **Document Processing**: LangChain text splitters, ReportLab (PDF generation)

## Prerequisites

- Python 3.8 or higher
- API Keys for:
  - **OpenAI API** (for LLM access)
  - **Pinecone** (for vector database)
  - **SerpAPI** (for Google Search)

## Installation

### 1. Clone Repository

```bash
git clone <repository-url>
cd ai-research-agent
```

### 2. Create Virtual Environment

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root:

```env
OPENAI_API_KEY=your_openai_api_key
PINECONE_API_KEY=your_pinecone_api_key
SERPAPI_API_KEY=your_serpapi_api_key
```

### 5. Initialize Vector Database (Optional)

Pre-load academic documents into Pinecone:

```bash
python ingest.py
```

This loads 10 ArXiv papers about "large language models" into the vector store.

## Usage

### Command-Line Interface

Run the interactive CLI:

```bash
python main.py
```

This opens an interactive loop where you can ask questions:

```
Ask your agent: What are the latest advances in transformer architectures?

Final Answer:
[Comprehensive research report with structured findings]
```

### Streamlit Web Application

Launch the web interface:

```bash
streamlit run app_streamlit.py
```

The Streamlit app provides:

- **Interactive chat interface** for research queries
- **Configurable parameters**:
  - Model selection (gpt-4, gpt-4o, gpt-4o-mini)
  - Temperature (0-2 for creativity control)
  - Research depth (quick, balanced, deep)
- **Conversation history** with memory management
- **PDF export** for research reports
- **Clear/reset memory** options

Access the app at `http://localhost:8501`

### Testing

Test LLM configuration:

```bash
python test_llm.py
```

## Project Structure

```
ai-research-agent/
├── main.py                          # CLI entry point
├── app_streamlit.py                 # Streamlit web app
├── ingest.py                        # Document ingestion script
├── requirements.txt                 # Project dependencies
├── conversation_memory.json         # Persistent conversation history
│
└── app/
    ├── __init__.py
    ├── agent.py                     # Core agent builder
    ├── memory_manager.py            # Memory persistence logic
    │
    ├── config/
    │   ├── settings.py              # Environment configuration
    │   └── llm.py                   # LLM initialization
    │
    ├── prompts/
    │   └── agent_prompt.py          # System prompts for agent
    │
    ├── graphs/
    │   └── research_graph.py        # LangGraph workflow definition
    │
    ├── rag/
    │   └── pinecone_setup.py        # Vector database setup
    │
    └── tools/
        ├── arxiv_tools.py           # ArXiv paper search
        ├── web_search.py            # Google Search integration
        ├── wikipedia_tool.py        # Wikipedia lookups
        ├── rag_tools.py             # Vector DB semantic search
        ├── calculator.py            # Math calculations
        ├── summarizer.py            # Text summarization
        └── dummy_tool.py            # Utility functions
```

## Agent Tools

The research agent has access to the following tools:

| Tool                 | Purpose                                        | Source         |
| -------------------- | ---------------------------------------------- | -------------- |
| **Web Search**       | Real-time information from search engines      | SerpAPI/Google |
| **ArXiv Search**     | Academic papers and preprints                  | ArXiv API      |
| **Wikipedia Search** | General knowledge and encyclopedic information | Wikipedia      |
| **RAG Search**       | Semantic search over ingested documents        | Pinecone       |
| **Calculator**       | Mathematical computations                      | Built-in       |
| **Text Summarizer**  | Condense long texts into summaries             | LangChain      |
| **Current Year**     | Get current date/time information              | Built-in       |

## Configuration

### Model Selection

Adjust the LLM model in Streamlit sidebar or API calls:

- `gpt-4`: Most capable, higher cost
- `gpt-4o`: Optimized performance
- `gpt-4o-mini`: Fast and budget-friendly

### Research Depth

- **Quick**: Uses 1-2 most relevant tools, concise answers
- **Balanced**: Moderate research using multiple sources
- **Deep**: Thorough investigation with extensive tool usage

### Temperature Control

- `0`: Deterministic, focused answers
- `0.5-1.0`: Balanced creativity and consistency
- `1.5-2.0`: Creative, diverse responses

## Dependencies

See `requirements.txt` for complete list:

- `langchain` - LLM framework
- `langgraph` - Agentic workflow
- `langchain-openai` - OpenAI integration
- `pinecone-client` - Vector database client
- `streamlit` - Web UI framework
- `arxiv` - ArXiv API client
- `wikipedia` - Wikipedia API client
- `google-search-results` - Google Search integration
- `reportlab` - PDF generation
- `python-dotenv` - Environment variable management

## Memory Management

The agent maintains conversation history in `conversation_memory.json` for:

- Multi-turn conversations with context awareness
- Persistent memory across sessions
- Manual reset/clear options in Streamlit UI

## Troubleshooting

### API Key Issues

- Verify all required API keys are in `.env`
- Check API key permissions and quotas

### Vector Database Connection

- Ensure Pinecone API key is valid
- Verify network connectivity to Pinecone servers

### Module Import Errors

- Reinstall dependencies: `pip install -r requirements.txt --force-reinstall`
- Ensure Python version is 3.8+

## Environment Variables

Required environment variables:

```
OPENAI_API_KEY          # OpenAI API key for LLM access
PINECONE_API_KEY        # Pinecone vector database API key
SERPAPI_API_KEY         # SerpAPI key for Google Search
```

Optional:

```
PINECONE_INDEX_NAME     # Pinecone index name (if custom)
```

## Development

### Adding New Tools

Create a new tool file in `app/tools/`:

```python
# app/tools/my_tool.py
from langchain.tools import tool

@tool
def my_research_tool(query: str) -> str:
    """Description of tool for agent"""
    # Implementation
    return result
```

Then import and add to `app/agent.py`:

```python
from app.tools.my_tool import my_research_tool

tools = [my_research_tool, ... existing tools]
```

### Customizing System Prompt

Edit `app/prompts/agent_prompt.py` to modify agent behavior and output format.

### Extending the Research Graph

Modify `app/graphs/research_graph.py` to change the agent workflow and decision-making process.

## Performance Considerations

- **Large Queries**: Deep research mode may take 2-5 minutes
- **Token Limits**: Responses are optimized for GPT-4's context window
- **API Costs**: Deep research uses more API calls; monitor usage
- **Vector Database**: Initialize with relevant documents for better RAG performance

## Support & Contributions

### Issues & Bug Reports

Report issues and bugs on [GitHub Issues](https://github.com/EmmanuelChukwu/ai-research-agent/issues)

### Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Contact

For questions or inquiries, contact: emmschuks18@gmail.com

---

**Last Updated**: March 2026
