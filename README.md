# AI-Multi-Model-RAG

This project is a Multi-Modal Retrieval-Augmented Generation (RAG) system designed to bridge the gap between static PDF documents and interactive AI. Unlike standard RAG systems that only "read" text, this system "sees" the document by extracting and indexing text, complex tables, and high-resolution diagrams to provide visually-grounded answers.

## Project Overview

The application allows users to upload technical papers (e.g., the "Attention Is All You Need" PDF) and ask complex questions. The AI doesn't just describe the answer; it retrieves the specific figure or table from the document that represents the concept, displaying it alongside a GPT-4o generated explanation.

### Core Features

- Multi-Modal Extraction: Uses PyMuPDF and pdfplumber to distinguish between prose, data tables, and embedded images.

- Vectorized Search: Converts text and image context into 1536-dimensional embeddings using OpenAI’s text-embedding-3-small and stores them in a Pinecone serverless vector database.

- Contextual Image Retrieval: When a user asks about a visual concept (e.g., "Input Projections"), the system performs a similarity search to find the corresponding image crop and serves it via a FastAPI static mount.

- Interactive Frontend: A modern, responsive Tailwind CSS interface that renders AI responses in Markdown and displays retrieved PDF figures in real-time.

### Technical Architecture

    Component       Technology
    
    Backend         FastAPI (Python)
    Vector DB       Pinecone (Serverless)
    LLM-OpenAI      GPT-4o-mini
    Embeddings      OpenAI text-embedding-3-small
    PDF Parsing     PyMuPDF (fitz) & pdfplumber
    Frontend        HTML5, CSS, js

### Workflow

    Ingestion: The user uploads a PDF. The backend splits the document into three streams:
    Text: Cleaned and chunked by page.
    Tables: Converted to Markdown format to preserve structural relationships.
    Images: Extracted as PNGs, with surrounding text saved as metadata for searchability.

### ⚙️ Installation

    # Clone the repository
    git clone https://github.com/Ahmed2797/AI-Multi-Model-RAG.git

    # Create and activate a conda environment
    conda create -n rag python=3.10
    conda activate rag

    # setup api key
    export OPENAI_API_KEY="your_api_key_here"
    export PINECONE_API_KEY="your_api_key_here"

    # store pinecone
    python store_pinecone.py

    #run 
    python app.py
