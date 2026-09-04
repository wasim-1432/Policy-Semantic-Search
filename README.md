# 🔎 Policy Semantic Search System

A semantic search system for company policy documents using **Text Embeddings, FAISS Vector Search, and Metadata Filtering**.

This project allows users to search policy documents using natural-language queries instead of relying only on exact keyword matching.

The system supports metadata-based filtering using:

- 🏢 Department
- 📄 Document Type
- 📅 Date
- 🔐 Access Level

The application is built using **Python, Sentence Transformers, FAISS, NumPy, and Streamlit**.

---

## 📌 Project Overview

Traditional keyword search mainly searches for exact words in documents.

For example, the user searches:

~~~text
How many vacation days can an employee take?
~~~

But the document contains:

~~~text
Employees are entitled to 24 days of annual leave every year.
~~~

A keyword-based search may not perform well because the query contains:

~~~text
vacation days
~~~

while the document contains:

~~~text
annual leave
~~~

Semantic search solves this problem by converting both the query and documents into numerical representations called **embeddings**.

The system then compares these embeddings using vector similarity and retrieves the most relevant document chunks.

---

# 🚀 Features

- 🔎 Semantic Search
- 🧠 Text Embeddings
- ⚡ FAISS Vector Search
- 🏷️ Metadata Filtering
- 🏢 Department Filtering
- 📄 Document Type Filtering
- 📅 Date Filtering
- 🔐 Access Level Filtering
- 📊 Similarity Scores
- 📚 Multiple Policy Documents
- 💻 Streamlit Web Interface
- 💾 Persistent FAISS Index
- 🧩 Modular Project Structure

---

# 🏗️ System Architecture

~~~text
                  Policy Documents
                         │
                         ▼
                 Document Loader
                         │
                         ▼
                     Chunking
                         │
                         ▼
                Text + Metadata
                         │
                         ▼
                 Embedding Model
                         │
                         ▼
                Vector Embeddings
                         │
                         ▼
                    FAISS Index
                         │
                         │
                    User Query
                         │
                         ▼
                 Query Embedding
                         │
                         ▼
                Similarity Search
                         │
                         ▼
                Metadata Filtering
                         │
                         ▼
                   Top-K Results
                         │
                         ▼
                   Streamlit UI
~~~

---

# 📂 Project Structure

~~~text
policy-semantic-search/
│
├── data/
│   └── policies/
│       ├── hr_leave_policy.txt
│       ├── it_security_policy.txt
│       ├── finance_expense_policy.txt
│       └── remote_work_policy.txt
│
├── src/
│   ├── __init__.py
│   ├── config.py
│   ├── document_loader.py
│   ├── chunker.py
│   ├── embeddings.py
│   ├── vector_store.py
│   ├── metadata_filter.py
│   └── search.py
│
├── index/
│   ├── policy.index
│   └── metadata.pkl
│
├── create_index.py
├── app.py
├── requirements.txt
├── .gitignore
└── README.md
~~~

---

# 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Streamlit | Web application interface |
| Sentence Transformers | Generate text embeddings |
| FAISS | Vector similarity search |
| NumPy | Numerical operations |
| Pickle | Store metadata |
| Git | Version control |
| GitHub | Source code hosting |

---

# 🧠 How the System Works

The project works in two main phases.

## 1. Indexing Phase

~~~text
Policy Documents
       ↓
Document Loader
       ↓
Metadata Extraction
       ↓
Chunking
       ↓
Embedding Generation
       ↓
FAISS Vector Index
       ↓
Save Index
~~~

## 2. Retrieval Phase

~~~text
User Query
       ↓
Query Embedding
       ↓
FAISS Similarity Search
       ↓
Metadata Filtering
       ↓
Top-K Relevant Chunks
       ↓
Display Results
~~~

---

# 📦 Installation

## Step 1: Clone the Repository

~~~bash
git clone https://github.com/YOUR_USERNAME/policy-semantic-search.git
~~~

Go inside the project directory:

~~~bash
cd policy-semantic-search
~~~

---

# 🐍 Step 2: Create Virtual Environment

For Windows:

~~~bash
python -m venv .venv
~~~

Activate the virtual environment:

~~~bash
.venv\Scripts\activate
~~~

If PowerShell gives an execution-policy error, use:

~~~bash
.venv\Scripts\python.exe -m pip install -r requirements.txt
~~~

---

# 📚 Step 3: Install Dependencies

~~~bash
pip install -r requirements.txt
~~~

Main dependencies:

~~~text
sentence-transformers
faiss-cpu
numpy
streamlit
~~~

---

# 📄 Sample Policy Documents

The project contains sample company policy documents.

## HR Leave Policy

~~~text
Department: HR
Document Type: Leave Policy
Date: 2026-01-15
Access Level: Employee
~~~

## IT Security Policy

~~~text
Department: IT
Document Type: Security Policy
Date: 2026-02-10
Access Level: Employee
~~~

## Finance Expense Policy

~~~text
Department: Finance
Document Type: Expense Policy
Date: 2026-03-05
Access Level: Manager
~~~

## Remote Work Policy

~~~text
Department: HR
Document Type: Remote Work Policy
Date: 2026-04-01
Access Level: Employee
~~~

---

# ✂️ Chunking

Large documents are divided into smaller pieces called **chunks**.

This project uses:

~~~text
Fixed-Length Chunking + Overlap
~~~

Example:

~~~text
Chunk 1
────────────────────────────────
Employees are entitled to 24 days
of annual leave every year.
Employees should submit their leave
requests at least three working days...
────────────────────────────────

                 Overlap

                     ↓

Chunk 2
────────────────────────────────
Employees should submit their leave
requests at least three working days...
Emergency leave can be requested...
────────────────────────────────
~~~

The overlap helps preserve context between neighboring chunks.

---

# 🧠 Embeddings

Embeddings represent text as numerical vectors.

This project uses the following Sentence Transformer model:

~~~text
all-MiniLM-L6-v2
~~~

For example:

~~~text
Employees can take annual leave.
~~~

is converted into a numerical vector such as:

~~~text
[0.021, -0.145, 0.083, ...]
~~~

The actual embedding contains many dimensions.

Texts with similar meanings tend to have similar vector representations.

---

# 🔎 Semantic Search

Semantic search searches based on the **meaning** of text rather than only matching exact keywords.

For example:

~~~text
Query:
How many vacation days can I take?
~~~

Document:

~~~text
Employees are entitled to 24 days of annual leave.
~~~

Even though the words are different:

~~~text
vacation ≈ annual leave
~~~

the embedding model can represent their semantic relationship.

---

# 🆚 Keyword Search vs Semantic Search

## Keyword Search

Keyword search focuses on matching exact words.

Example:

~~~text
Query:
vacation days

Document:
annual leave
~~~

There may be no exact keyword match.

---

## Semantic Search

Semantic search considers the meaning:

~~~text
vacation
annual leave
time off
holiday leave
~~~

These concepts can have similar semantic representations.

Therefore, semantic search can retrieve relevant documents even when exact words are different.

---

# 🏷️ Metadata

Metadata is additional information associated with each document or chunk.

This project uses:

~~~text
Department
Document Type
Date
Access Level
Source
~~~

Example:

~~~json
{
    "department": "HR",
    "document_type": "Leave Policy",
    "date": "2026-01-15",
    "access_level": "Employee",
    "source": "hr_leave_policy.txt"
}
~~~

Metadata helps the application filter search results.

---

# 🔐 Metadata Filtering

The application supports filtering based on:

## Department

~~~text
HR
IT
Finance
~~~

## Document Type

~~~text
Leave Policy
Security Policy
Expense Policy
Remote Work Policy
~~~

## Date

Example:

~~~text
2026-01-15
~~~

## Access Level

~~~text
Employee
Manager
~~~

---

# 📊 Similarity Search

FAISS is configured using:

~~~python
faiss.IndexFlatIP(dimension)
~~~

`IP` stands for:

~~~text
Inner Product
~~~

The embeddings are normalized before being stored:

~~~python
normalize_embeddings=True
~~~

Because the embeddings are normalized, inner product can be used as an efficient equivalent to cosine similarity.

---

# 📐 Similarity Metrics

Vector search commonly uses different similarity or distance metrics.

## 1. Cosine Similarity

Cosine similarity measures the angle between two vectors.

~~~text
             A · B
Cosine = ---------------
           |A| × |B|
~~~

Higher similarity generally means the vectors have more similar directions.

---

## 2. Dot Product

Dot product is:

~~~text
A · B
~~~

It is computationally efficient and is used by this project through FAISS Inner Product search.

---

## 3. Euclidean Distance

Euclidean distance measures the straight-line distance between two vectors.

~~~text
Distance = √Σ(Aᵢ - Bᵢ)²
~~~

Smaller distance generally means greater similarity.

---

# 🗄️ FAISS

This project uses **FAISS** for vector similarity search.

FAISS is designed for efficient similarity search over dense vectors.

The project creates an index using:

~~~python
faiss.IndexFlatIP(dimension)
~~~

The index stores document embeddings and allows similarity search.

---

# 🗃️ Other Vector Databases

Popular vector databases and vector search systems include:

| Technology | Common Use |
|---|---|
| FAISS | Local and high-performance vector search |
| Chroma | Learning, prototypes, and RAG |
| Pinecone | Managed production vector database |
| Weaviate | Production vector search |
| Qdrant | Vector search with metadata filtering |
| pgvector | Vector search inside PostgreSQL |

---

# ▶️ Create the Vector Index

Before starting the Streamlit application, create the FAISS index.

Run:

~~~bash
python create_index.py
~~~

Expected output:

~~~text
Loading documents...
Documents loaded: 4

Creating chunks...
Chunks created: ...

Generating embeddings...

Creating FAISS index...

Index created successfully!
~~~

After successful execution, the `index` folder will contain:

~~~text
index/
├── policy.index
└── metadata.pkl
~~~

---

# 🌐 Run the Streamlit Application

Run:

~~~bash
streamlit run app.py
~~~

The application will start locally.

Usually Streamlit provides an address similar to:

~~~text
http://localhost:8501
~~~

Open the address in your browser.

---

# 💬 Example Queries

## Example 1

Query:

~~~text
How many annual leaves can employees take?
~~~

Expected result:

~~~text
Department: HR
Document Type: Leave Policy
Access Level: Employee
~~~

---

## Example 2

Query:

~~~text
What are the password requirements?
~~~

Expected result:

~~~text
Department: IT
Document Type: Security Policy
~~~

---

## Example 3

Query:

~~~text
What expenses can employees claim?
~~~

Apply filters:

~~~text
Department: Finance
Access Level: Manager
~~~

The system retrieves relevant Finance policy chunks.

---

## Example 4

Query:

~~~text
How often should passwords be changed?
~~~

Expected result:

~~~text
Department: IT

Passwords must be changed every 90 days.
~~~

---

# 🧪 Example Search Flow

Suppose the user searches:

~~~text
How many days of annual leave are available?
~~~

The system performs:

~~~text
                     User Query
                          │
                          ▼
                Query Embedding
                          │
                          ▼
                   Query Vector
                          │
                          ▼
                   FAISS Search
                          │
                          ▼
                Similarity Ranking
                          │
                          ▼
                Metadata Filtering
                          │
                          ▼
                  Relevant Chunks
                          │
                          ▼
                  Streamlit Display
~~~

---

# 🧩 Project Components

## `document_loader.py`

Responsible for:

- Reading policy documents
- Extracting text
- Extracting metadata
- Creating document objects

---

## `chunker.py`

Responsible for:

- Splitting documents
- Creating overlapping chunks
- Keeping metadata with chunks

---

## `embeddings.py`

Responsible for:

- Loading the embedding model
- Generating embeddings
- Converting text into vectors

---

## `vector_store.py`

Responsible for:

- Creating FAISS index
- Adding embeddings
- Saving the index
- Loading the index
- Performing similarity search

---

## `metadata_filter.py`

Responsible for:

- Department filtering
- Document type filtering
- Date filtering
- Access-level filtering

---

## `search.py`

Combines:

~~~text
Embedding
     +
Vector Search
     +
Metadata Filtering
~~~

to create the policy search engine.

---

## `create_index.py`

Responsible for the indexing pipeline:

~~~text
Documents
    ↓
Load
    ↓
Chunk
    ↓
Generate Embeddings
    ↓
Create FAISS Index
    ↓
Save Index
~~~

---

## `app.py`

Provides the Streamlit user interface.

It allows users to:

- Enter search queries
- Select metadata filters
- Search policies
- View similarity scores
- View document metadata
- View relevant chunks

---

# ⚠️ Retrieval Quality Problems

Semantic search systems can face several retrieval problems.

## 1. Irrelevant Chunks

Sometimes the system retrieves a chunk that is semantically related but does not actually answer the query.

Possible solutions:

~~~text
Better embedding model
Better chunking
Metadata filtering
Reranking
Similarity threshold
~~~

---

## 2. Duplicate Chunks

Similar or duplicate chunks may appear in search results.

Possible solutions:

~~~text
Deduplication
Hashing
Similarity threshold
Better chunking
~~~

---

## 3. Missing Context

A chunk may contain only part of the required information.

For example:

~~~text
Chunk 1:
Full-time employees...

Chunk 2:
are eligible for 24 days of leave.
~~~

If only Chunk 2 is retrieved, important context may be missing.

Possible solutions:

~~~text
Chunk overlap
Larger chunks
Parent-child retrieval
Context expansion
Document-aware chunking
~~~

---

# 🔄 Indexing Pipeline

The indexing pipeline is:

~~~text
Policy Documents
       ↓
Document Loader
       ↓
Metadata Extraction
       ↓
Chunking
       ↓
Embedding Generation
       ↓
FAISS Index
       ↓
Save Index
~~~

This pipeline runs when:

~~~bash
python create_index.py
~~~

is executed.

---

# 🔎 Retrieval Pipeline

The retrieval pipeline is:

~~~text
User Query
       ↓
Generate Query Embedding
       ↓
FAISS Similarity Search
       ↓
Retrieve Candidate Chunks
       ↓
Apply Metadata Filters
       ↓
Top-K Results
       ↓
Display Results
~~~

---

# 🔀 Hybrid Search

A future version can combine:

~~~text
Keyword Search
       +
Semantic Search
       ↓
Hybrid Search
~~~

Keyword search can be useful for exact terms such as:

~~~text
Policy ID
Employee ID
Contract Number
Product Code
~~~

Semantic search is useful for natural-language questions such as:

~~~text
How much annual leave can I take?
~~~

Combining both approaches can improve retrieval quality.

---

# 🔄 Reranking

A future implementation can retrieve more candidates first:

~~~text
FAISS
  ↓
Top 20 Chunks
  ↓
Reranker
  ↓
Top 5 Chunks
~~~

A reranker can analyze the query and candidate documents more deeply and reorder the results based on relevance.

---

# 🚀 Future Improvements

The following features can be added in future versions:

- [ ] PDF document support
- [ ] DOCX document support
- [ ] Recursive chunking
- [ ] Semantic chunking
- [ ] Document-aware chunking
- [ ] Hybrid search
- [ ] BM25 keyword search
- [ ] Reranking
- [ ] Similarity threshold
- [ ] Duplicate removal
- [ ] Qdrant integration
- [ ] Pinecone integration
- [ ] Chroma integration
- [ ] pgvector integration
- [ ] User authentication
- [ ] Role-based access control
- [ ] LLM-based answer generation
- [ ] Source citations
- [ ] Chat interface
- [ ] Docker deployment

---

# 🤖 Future RAG Architecture

This semantic search system can be extended into a complete RAG application.

~~~text
                  Policy Documents
                         │
                         ▼
                      Chunking
                         │
                         ▼
                    Embeddings
                         │
                         ▼
                  Vector Database
                         │
                         ▼
                     Retrieval
                         │
                         ▼
                     Reranking
                         │
                         ▼
                  Relevant Context
                         │
                         ▼
                        LLM
                         │
                         ▼
                 Generated Answer
                         │
                         ▼
                    User Interface
~~~

---

# 🔒 Access Control

Metadata can also be used to support access-control logic.

For example:

~~~text
Employee
    ↓
Employee-level policies

Manager
    ↓
Employee + Manager policies

Admin
    ↓
All authorized policies
~~~

In a real production system, metadata filtering should not be considered the only security mechanism.

Proper authentication and authorization should also be implemented.

---

# 📈 Learning Objectives

This project demonstrates the following concepts:

### Embeddings

How text can be represented as numerical vectors.

### Semantic Search

Searching based on meaning instead of exact keywords.

### Chunking

Breaking large documents into smaller searchable pieces.

### Metadata

Attaching additional information to documents and chunks.

### Similarity Metrics

Understanding:

~~~text
Cosine Similarity
Dot Product
Euclidean Distance
~~~

### Vector Indexing

Efficiently storing and searching embeddings.

### Retrieval

Finding the most relevant document chunks.

### Filtering

Restricting results using metadata.

### Reranking

Improving the order of retrieved results.

### Hybrid Search

Combining keyword and semantic retrieval.

---

# 🖥️ Application Interface

The Streamlit application provides:

~~~text
┌───────────────────────────────────────────────┐
│           🔎 Policy Semantic Search            │
├───────────────────────────────────────────────┤
│                                               │
│ Ask your question                             │
│                                               │
│ ┌───────────────────────────────────────────┐ │
│ │ How many annual leaves can I take?        │ │
│ └───────────────────────────────────────────┘ │
│                                               │
│                 [ Search ]                    │
│                                               │
├───────────────────┬───────────────────────────┤
│ Metadata Filters  │ Search Results            │
│                   │                           │
│ Department        │ Similarity Score: 0.82   │
│ [HR]              │ Department: HR            │
│                   │ Document: Leave Policy    │
│ Document Type     │                           │
│ [Leave Policy]    │ Employees are entitled   │
│                   │ to 24 days of annual     │
│ Access Level      │ leave every year.        │
│ [Employee]        │                           │
└───────────────────┴───────────────────────────┘
~~~

---

# 📚 Sample Dataset

The sample dataset contains policies related to:

~~~text
HR
├── Leave Policy
└── Remote Work Policy

IT
└── Security Policy

Finance
└── Expense Policy
~~~

The sample documents are provided for educational and demonstration purposes.

---

# 🔧 Configuration

Configuration values are maintained in:

~~~text
src/config.py
~~~

Example:

~~~python
EMBEDDING_MODEL = "all-MiniLM-L6-v2"

CHUNK_SIZE = 300

CHUNK_OVERLAP = 50

TOP_K = 5
~~~

These values can be adjusted according to application requirements.

---

# 📁 Important Files

| File | Purpose |
|---|---|
| `app.py` | Streamlit application |
| `create_index.py` | Creates FAISS vector index |
| `requirements.txt` | Python dependencies |
| `src/config.py` | Configuration |
| `src/document_loader.py` | Loads documents |
| `src/chunker.py` | Creates chunks |
| `src/embeddings.py` | Generates embeddings |
| `src/vector_store.py` | FAISS operations |
| `src/metadata_filter.py` | Metadata filtering |
| `src/search.py` | Search engine |
| `data/policies/` | Policy documents |
| `index/` | Generated FAISS index |

---

# 🧹 `.gitignore`

It is recommended to add a `.gitignore` file.

Example:

~~~gitignore
.venv/
__pycache__/
*.pyc
.env
.DS_Store
~~~

If you do not want to upload generated indexes to GitHub, you can also add:

~~~gitignore
index/
~~~

However, if your application requires the pre-built FAISS index, keep the index files in the repository or generate them during deployment.

---

# 📤 Push Project to GitHub

Initialize Git:

~~~bash
git init
~~~

Add all files:

~~~bash
git add .
~~~

Commit the project:

~~~bash
git commit -m "Initial commit - Policy Semantic Search System"
~~~

Add your GitHub repository:

~~~bash
git remote add origin https://github.com/YOUR_USERNAME/policy-semantic-search.git
~~~

Push the project:

~~~bash
git branch -M main
git push -u origin main
~~~

---

# 🚀 Quick Start

~~~bash
git clone https://github.com/YOUR_USERNAME/policy-semantic-search.git

cd policy-semantic-search

python -m venv .venv

.venv\Scripts\activate

pip install -r requirements.txt

python create_index.py

streamlit run app.py
~~~

---

# 🎯 Module 5 Practical

This project is based on:

~~~text
Module 5: Embeddings and Vector Search
~~~

The practical covers:

- ✓ What embeddings represent
- ✓ Semantic Search
- ✓ Keyword Search
- ✓ Chunking Strategies
- ✓ Metadata Design
- ✓ Metadata Filtering
- ✓ Cosine Similarity
- ✓ Dot Product
- ✓ Euclidean Distance
- ✓ Embedding Model Selection
- ✓ Indexing
- ✓ Retrieval
- ✓ Reranking Concepts
- ✓ Hybrid Search Concepts
- ✓ Vector Databases
- ✓ Retrieval Quality Problems

---

# 📝 Key Concepts Summary

~~~text
Embedding
    ↓
Numerical representation of text

Chunking
    ↓
Breaking documents into smaller pieces

Vector Index
    ↓
Efficient storage and similarity search

Semantic Search
    ↓
Search based on meaning

Metadata
    ↓
Additional information about documents

Filtering
    ↓
Restrict results using metadata

Retrieval
    ↓
Find relevant document chunks

Reranking
    ↓
Improve result ordering

Hybrid Search
    ↓
Combine keyword + semantic search
~~~

---

# 🔮 Project Roadmap

~~~text
Version 1
   │
   ├── Text Documents
   ├── Fixed Chunking
   ├── Sentence Transformers
   ├── FAISS
   └── Metadata Filtering
        │
        ▼
Version 2
   │
   ├── PDF Support
   ├── Recursive Chunking
   ├── Better Embedding Models
   └── Similarity Threshold
        │
        ▼
Version 3
   │
   ├── Hybrid Search
   ├── BM25
   ├── Reranking
   └── Better Retrieval
        │
        ▼
Version 4
   │
   ├── Vector Database
   ├── Qdrant / Pinecone
   ├── Authentication
   └── Access Control
        │
        ▼
Version 5
   │
   ├── RAG
   ├── LLM
   ├── Answer Generation
   └── Source Citations
~~~

---

# 👨‍💻 Author

## Mohd Wasim

**B.Tech – Information Technology**

Areas of Interest:

- Artificial Intelligence
- Generative AI
- Retrieval-Augmented Generation (RAG)
- Large Language Models (LLMs)
- Machine Learning
- Python
- C++
- Data Structures and Algorithms

---

# ⭐ Support

If you found this project useful for learning **Embeddings, Semantic Search, FAISS, and Vector Databases**, consider giving the repository a ⭐ on GitHub.

---

# 📄 License

This project is created for educational and learning purposes.

You are free to use, modify, and extend the project for your own learning and development.

---

# 🙌 Conclusion

The **Policy Semantic Search System** demonstrates how modern AI-powered search systems can retrieve relevant information based on semantic meaning.

The project combines:

~~~text
Python
   +
Sentence Transformers
   +
Embeddings
   +
FAISS
   +
Metadata Filtering
   +
Streamlit
~~~

to create a practical semantic search application over policy documents.

The same architecture can be extended into a production-ready **RAG system** by adding a vector database, reranking, hybrid search, an LLM, authentication, and source citations.
