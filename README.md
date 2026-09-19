# Nepal Telecom Customer Care AI Chatbot

An AI-powered customer care chatbot developed to provide automated responses to Nepal Telecom customer queries.

## Features

* AI-based customer query answering
* Customer care information retrieval
* Retrieval-Augmented Generation (RAG)
* Knowledge base using Nepal Telecom data
* Django-based web application
* REST API for chatbot communication
* Text-to-Speech support
* User-friendly chatbot interface
* Local development support with LM Studio

## Technologies Used

* Python
* Django
* Django REST Framework
* HTML, CSS, JavaScript
* FAISS
* Sentence Transformers
* RAG
* Large Language Models (LLM)
* LM Studio
* Groq API
* Edge TTS

## Project Structure

```text
Nepal-telelcom-cutomer-care-chatbot/
│
├── chatbot/
│   ├── views.py
│   ├── urls.py
│   ├── models.py
│   └── ...
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/niva-sah/Nepal_telecom_customer_care_chatbot.git
cd Nepal_telecom_customer_care_chatbot
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

For Windows PowerShell:

```powershell
venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run migrations

```bash
python manage.py migrate
```

### 6. Start the development server

```bash
python manage.py runserver
```

Open the application in your browser:

```text
http://127.0.0.1:8000/
```

## Chatbot Architecture

```text
User Query
    ↓
Django Chatbot Interface
    ↓
Query Processing
    ↓
Knowledge Base / RAG
    ↓
FAISS Similarity Search
    ↓
Relevant Context
    ↓
LLM
    ↓
Generated Response
    ↓
Text-to-Speech
    ↓
User
```

## Knowledge Base

The chatbot uses Nepal Telecom customer-care information as its knowledge source. The data is processed into smaller text chunks and converted into embeddings for similarity-based retrieval.

## API

The chatbot provides an API endpoint for sending user queries and receiving chatbot responses.

Example:

```text
/chat_api/
```

## Environment Variables

Create a `.env` file for sensitive configuration such as API keys.

Example:

```env
GROQ_API_KEY=your_api_key_here
```

Do not upload your `.env` file or API keys to GitHub.

## Future Improvements

* Improve chatbot response accuracy
* Add multilingual support
* Add more Nepal Telecom services to the knowledge base
* Improve conversation memory
* Deploy the chatbot to a production server
* Add analytics for customer queries

## Author

**Niva Kumari Sah**

B.E. Computer Engineering
Nepal Engineering College, Pokhara University

## License

This project is developed for educational and project purposes.
