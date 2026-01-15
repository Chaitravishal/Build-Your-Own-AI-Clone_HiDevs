# HiDevs AI Clone - RAG Chatbot 🤖

A Retrieval-Augmented Generation (RAG) based AI chatbot built as part of the **HiDevs – Build Your Own AI Clone** program. This chatbot answers user queries by retrieving relevant documents from a vector database and generating accurate, context-aware responses using a large language model.

## 🚀 Features

- **Interactive UI** - Built with Streamlit for a seamless user experience
- **RAG Pipeline** - Retrieval-Augmented Generation for accurate responses
- **Vector Search** - FAISS-based similarity search for document retrieval
- **Context-Aware** - Generates responses based on retrieved relevant documents
- **Modular Architecture** - Clean, scalable, and maintainable codebase

## 🧠 Tech Stack

- **Python** - Core programming language
- **Streamlit** - Web interface framework
- **LangChain** - Framework for LLM applications
- **Groq API** - Fast LLM inference with Llama 3
- **FAISS** - Vector database for similarity search
- **HuggingFace Embeddings** - Text embeddings generation
- **python-dotenv** - Environment variable management

## 🏗️ Project Structure

```
Build-Your-Own-AI-Clone_HiDevs/
├── app.py                  # Main Streamlit application
├── test_chat.py           # Testing script for chatbot
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables (not in repo)
├── .gitignore            # Git ignore rules
├── data/
│   └── docs.txt          # Knowledge base documents
├── embeddings/
│   └── embed.py          # Embedding generation logic
├── faiss_index/
│   ├── index.faiss       # FAISS vector index
│   └── index.pkl         # Serialized document metadata
└── rag/
    └── retriever.py      # Document retrieval logic
```

## ⚙️ How It Works (RAG Pipeline)

1. **User Query** - User enters a question through the Streamlit interface
2. **Embedding** - Query is converted to a vector embedding
3. **Retrieval** - Most relevant documents are fetched from FAISS vector store
4. **Context Injection** - Retrieved documents are added to the prompt
5. **Generation** - LLM generates a grounded, accurate response
6. **Response Display** - Answer is shown to the user

## 🛠️ Setup Instructions

### Prerequisites
- Python 3.8 or higher
- Groq API key ([Get one here](https://console.groq.com))

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/Chaitravishal/Build-Your-Own-AI-Clone_HiDevs.git
cd Build-Your-Own-AI-Clone_HiDevs
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Set up environment variables**

Create a `.env` file in the root directory:
```bash
GROQ_API_KEY=your_groq_api_key_here
```

4. **Run the application**
```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

## 📝 Usage

1. Launch the application using `streamlit run app.py`
2. Enter your question in the text input box
3. Click "Submit" or press Enter
4. The chatbot will retrieve relevant information and generate a response
5. View the answer along with the source context

## 🧪 Testing

To test the chatbot functionality without the UI:
```bash
python test_chat.py
```

## 📚 Adding Your Own Knowledge Base

To customize the chatbot with your own data:

1. Edit `data/docs.txt` and add your documents
2. Run the embedding script to regenerate the vector index:
```bash
python embeddings/embed.py
```
3. Restart the Streamlit app

## 🔧 Configuration

Key configuration options in the code:

- **Model**: Llama 3 via Groq API (can be changed in `app.py`)
- **Chunk Size**: Document chunking parameters in `embed.py`
- **Retrieval Count**: Number of documents to retrieve (in `retriever.py`)
- **Temperature**: LLM creativity setting (in `app.py`)

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests

## 📄 License

This project is open source and available under the MIT License.

## 👨‍💻 Author

**Chaitravishal**
- GitHub: [@Chaitravishal](https://github.com/Chaitravishal)

## 🙏 Acknowledgments

- HiDevs for the AI Clone workshop
- LangChain community
- Groq for fast LLM inference
- Streamlit for the amazing framework

---

⭐ If you found this project helpful, please give it a star!
```
