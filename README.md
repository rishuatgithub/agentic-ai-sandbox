# Agentic AI Sandbox

A comprehensive collection of example implementations demonstrating agentic AI concepts using LangChain, LangGraph, and related libraries. This repository serves as a sandbox for exploring and learning about building intelligent agents, chatbots, RAG systems, and more.

## Overview

This sandbox includes:
- Basic to advanced agent implementations
- LangGraph-based workflows
- Integration with various LLMs (OpenAI, Anthropic, Google)
- Tool usage examples (web search, custom tools)
- Memory and state management
- RAG (Retrieval-Augmented Generation) systems
- MCP (Model Context Protocol) adapters
- Custom search integrations

## Repository Structure

### Root Level Examples
- `01_simple_agent.py` - Basic chatbot using LangGraph
- `02_complex_agent.py` - More complex agent setup
- `03_create_react_agent.py` - ReAct agent creation
- `04_create_react_agent_w_llm_config.py` - Agent with LLM configuration
- `05_create_react_agent_w_prompt.py` - Agent with custom prompts
- `06_create_react_agent_w_memory.py` - Agent with memory
- `07_create_react_agent_w_structuredOutput.py` - Structured output agents
- `08_create_react_agent_w_tools.py` - Agents with custom tools
- `09_create_react_agent_w_prebuilt_tools.py` - Using prebuilt tools
- `10_create_react_agent_w_memory.py` - Memory-enabled agents
- `11_create_react_agent_w_humanloop.py` - Human-in-the-loop agents
- `env_utils.py` - Environment utilities

### Subprojects

#### `langchain-agentic-ai/`
A series of LangChain-based agent examples:
- `01_simple_agent.py` - Basic agent
- `02_simple_agent_streaming_output.py` - Streaming responses
- `03_prompting_simple.py` - Simple prompting
- `04_prompting_fewshot.py` - Few-shot prompting
- `05_prompting_structured_output.py` - Structured outputs
- `06_tools.py` - Tool usage
- `07_websearch.py` - Web search integration
- `08_memory.py` - Memory management
- `09_mcp.py` - MCP client example
- `10_runtime_context.py` - Runtime context
- `11_state.py` - State management
- `12_middleware_summarization.py` - Summarization middleware
- `13_middleware_trim_del_messages.py` - Message trimming
- `14_hitl.py` - Human-in-the-loop

Specialized agents:
- `01-personal-chef/` - Personal chef agent using web search for recipes
- `02-rag-agent/` - RAG agent with PDF document processing
- `03-sql-agent/` - SQL query agent with Chinook database
- `mcp-server/` - MCP server implementation

#### `agentic-rag/`
A LangGraph project template for building RAG applications with LangGraph Server and Studio support.

#### `simple-agent/`
Another LangGraph project template for simple agents.

#### `custom-search/`
Google Custom Search API integration example.

#### `claude-skills/`
(Empty directory for Claude AI skills)

## Prerequisites

- Python 3.13 or higher
- API keys for LLM providers (OpenAI, Anthropic, Google, etc.)
- Optional: LangSmith for tracing
- Optional: Tavily for web search

## Installation

1. Clone the repository:
```bash
git clone https://github.com/rishushrivastava/agentic-ai-sandbox.git
cd agentic-ai-sandbox
```

2. Install dependencies using uv (recommended):
```bash
pip install uv
uv sync
```

Or using pip:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
Create a `.env` file in the root directory:
```bash
cp .env.example .env
```

Add your API keys:
```env
OPENAI_API_KEY=your_openai_key
ANTHROPIC_API_KEY=your_anthropic_key
GOOGLE_API_KEY=your_google_key
TAVILY_API_KEY=your_tavily_key
LANGSMITH_API_KEY=your_langsmith_key  # Optional
```

## Usage

### Running Root Level Examples

Most examples can be run directly with Python:

```bash
python 01_simple_agent.py
```

Follow the prompts or check the code for input methods.

### Running Subproject Agents

#### LangChain Agentic AI Examples
Navigate to the directory and run specific files:

```bash
cd langchain-agentic-ai
python 01_simple_agent.py
```

For specialized agents:
```bash
cd langchain-agentic-ai/01-personal-chef
python personal_chef_agent.py
```

#### Agentic RAG
```bash
cd agentic-rag
pip install -e . "langgraph-cli[inmem]"
langgraph dev
```

#### Simple Agent
```bash
cd simple-agent
pip install -e . "langgraph-cli[inmem]"
langgraph dev
```

#### Custom Search
```bash
cd custom-search
python main.py
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Resources

- [LangChain Documentation](https://python.langchain.com/)
- [LangGraph Documentation](https://langchain-ai.github.io/langgraph/)
- [LangGraph Studio](https://langchain-ai.github.io/langgraph/concepts/langgraph_studio/)
- [MCP Documentation](https://modelcontextprotocol.io/)
