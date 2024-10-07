<div align="center">
  <img src="img/logo.jpeg" alt="Logo of Your Project" width="200">
  <h1>Chat boot KEA PoC</h1>

  <p>
    A brief description of what this project does and why it is useful
  </p>

  <!-- Badges -->
  <img src="https://img.shields.io/badge/version-1.0.0-blue.svg?cacheSeconds=2592000" />
  

</div>

---

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Installation

```bash
# Clone the repository
git clone https://javi-reyes@bitbucket.org/ioconnectservices/chat-bot-kea-poc.git
# Navigate to the folder
cd chat-bot-kea-poc
# Install dependencies
pip install -r requirements.txt
# Start the project
streamlit run app.py

```

## Usage
Make sure to change to the KB ID in line 44
```bash
# Amazon Bedrock - KnowledgeBase Retriever 
retriever = AmazonKnowledgeBasesRetriever(
    knowledge_base_id="KB-ID", #Make sure to change to the KB ID
    retrieval_config={"vectorSearchConfiguration": {"numberOfResults": 4}},
)

```

http://localhost:8501/
![alt text](image.png)