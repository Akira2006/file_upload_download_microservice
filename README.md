# File Upload Download Microservice

A simple Python Flask microservice that allows applications to upload files and download them later using a unique file ID.  
This project demonstrates a basic microservice architecture where services communicate through HTTP requests.

---

## Overview

This microservice allows a client application to:

• Upload files to the server  
• Generate a unique file ID for every uploaded file  
• Store the file locally on the server  
• Download the file later using the file ID  

The service exposes simple REST endpoints that other applications can interact with.

---

## Tech Stack

Python  
Flask  
UUID for unique file identification  

---

## Project Structure

file_upload_download_microservice
│
├── server.py
├── requirements.txt
├── README.md
└── uploads/


---

## Installation

### 1. Clone the repository


git clone https://github.com/Akira2006/file_upload_download_microservice.git

cd file_upload_download_microservice


### 2. Install dependencies


pip install -r requirements.txt


### 3. Run the microservice


python server.py


The server will start on:


http://127.0.0.1:5001


---

## API Endpoints

### Upload File

Uploads a file to the server.

**Endpoint**


POST /upload


**Example**


curl -F "file=@test.txt" http://127.0.0.1:5001/upload


**Response**


{
"file_id": "generated-id",
"message": "File uploaded"
}


---

### Download File

Downloads a file using the generated file ID.

**Endpoint**


GET /download/<file_id>


**Example**


http://127.0.0.1:5001/download/
<file_id>


---

## Example Workflow

1. Upload a file using the `/upload` endpoint  
2. The server generates a unique `file_id`  
3. The file is stored in the `uploads` directory  
4. Use `/download/<file_id>` to retrieve the file later

---

## Purpose

This project was built as part of a microservices assignment to demonstrate how independent services can handle specific responsibilities such as file storage and retrieval.

The service communicates through HTTP requests instead of direct function calls, following the microservice architecture pattern.


---
