# Simple Chatbot

This project is a simple chatbot application that utilizes the 8B model of LLaMA3 for natural language processing. The front end is built with React and JavaScript, while the back end is powered by Flask and Python. This README provides an overview of the project, how to set it up, and how to run it.

## Project Structure

- **Frontend**: Built with React and JavaScript
- **Backend**: Built with Flask and Python
- **Model**: LLaMA3 (8B model)

## Features

- Chat with a bot powered by the LLaMA3 model
- User-friendly interface with a text input
- Easy setup and configuration

## Prerequisites

Make sure you have the following installed:

- Node.js (for React)
- Python 3.7+ (for Flask)
- Pip (Python package manager)
- An environment for running LLaMA3 (e.g., a GPU or suitable hardware for large model inference)

## Frontend Setup

1. **Navigate to the frontend directory**:

    ```bash
    cd frontend
    ```

2. **Install dependencies**:

    ```bash
    npm install
    ```

3. **Start the React development server**:

    ```bash
    npm start
    ```

    The application will be accessible at `http://localhost:5000`.

## Backend Setup

1. **Navigate to the backend directory**:

    ```bash
    cd backend
    ```

2. **Create and activate a virtual environment** (optional but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required Python packages**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Start the Flask server**:

    ```bash
    python app.py
    ```

    The Flask server will be accessible at `http://localhost:5000`.

## Configuration

1. **Update Backend Configuration**:
   
   Make sure to configure the path to the LLaMA3 model in the `app.py` file within the `backend` directory. You may need to adjust the code to correctly load and use the LLaMA3 model based on your specific setup.

2. **Frontend to Backend Communication**:

   Ensure that the React app (frontend) is configured to communicate with the Flask API. You may need to update the API URL in the React code to match the Flask server's address.

## Usage

1. **Start both frontend and backend servers** as described in the setup sections.

2. **Open your web browser** and navigate to `http://localhost:5000`.

3. **Interact with the chatbot** by typing messages into the chat input and receiving responses generated by the LLaMA3 model.

## Troubleshooting

- If you encounter issues with model loading, ensure that you have the necessary hardware and dependencies to run the LLaMA3 model.
- Check the browser console and Flask server logs for any errors or issues.
- Ensure that both servers (React and Flask) are running and correctly configured to communicate with each other.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [LLaMA3](https://ollama.com/library/llama3.1:8b) for the powerful language model.
- [React](https://reactjs.org/) and [Flask](https://flask.palletsprojects.com/) for the development frameworks.

