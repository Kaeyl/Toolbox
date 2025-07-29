This Python script automates the creation of a PostgreSQL Docker container using user input — perfect for developers who (like me) forget Docker commands every few weeks and just want to spin up a working container quickly.

What It Does
Prompts you to enter a username, password, database name, container name, and port.

Creates a PostgreSQL container with your settings using Docker.

Prints the list of current containers (running and stopped).

How to Use

Clone the repo or copy the script.

Ensure you have Docker running.

Create a virtual environment and install dependencies:

python -m venv venv
source venv/bin/activate  
pip install docker

Run the script:

python createNewDockerContainer.py

