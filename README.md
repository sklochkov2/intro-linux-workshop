# Intro Linux Workshop

## Overview
This small project is designed to help you:
1. Explore filesystem navigation.  
2. Practice basic command-line tasks.  
3. Launch and inspect processes.  
4. Run a simple web service and interact with it.

## Structure
- `server/`: a minimal Flask app exposing two endpoints.  
- `data/message.txt`: static content for viewing.  

## Quick start exercises

1. Clone the repository and enter it:
   ```bash
   git clone <repo-url>
   cd intro-linux-workshop
   ```
2. Install dependencies & run the server.
   ```bash
   sudo apt update
   sudo apt install -y python3 python3-pip
   pip3 install -r requirements.txt --break-system-packages
   ```
3. Query the server.
   ```bash
   sudo apt update
   sudo apt install -y curl
   curl 'http://127.0.0.1:8000/'
   curl 'http://127.0.0.1:8000/message'
   ```
4. How do we make curl display what exactly it did when sending the request? How can we use it to send a POST request instead of GET? The Docs will help us!
   ```bash
   man curl
   ```
