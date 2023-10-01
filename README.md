# Show-Ticketing

## Local Project Setup

**Prerequisites:**

- **Git**: Ensure you have Git installed. If not, download and install it from [https://git-scm.com/](https://git-scm.com/).

- **Python**: Make sure you have Python 3.x installed. You can download it from [https://www.python.org/downloads/](https://www.python.org/downloads/).

- **Node.js**: You'll need Node.js and npm for the frontend. Download and install them from [https://nodejs.org/](https://nodejs.org/).

- **Redis**: Install and start Redis, which is required for certain backend features. You can get it from [https://redis.io/download](https://redis.io/download).

**Steps:**

1. **Fork the Repository:**
   - Click the "Fork" button on the GitHub repository page to create a copy of the project under your GitHub account.

2. **Clone the Repository:**
   - Open your terminal and run the following command to clone the repository to your local machine:
     ```
     git clone https://github.com/<your-github-username>/Show-Ticketing.git
     ```
     Replace `<your-github-username>` with your actual GitHub username.

3. **Navigate to the Project Folder:**
   - Use the `cd` command to move into the project folder:
     ```
     cd Show-Ticketing
     ```

### Backend Setup:

4. **Edit the .env File:**
   - Inside the project folder, navigate to the `backend` directory, and edit the `.env` file. Configure any necessary environment variables.

5. **Create a Virtual Environment:**
   - In the `backend` folder, create a virtual environment with the following command:
     ```
     python3 -m venv venv
     ```

6. **Activate the Virtual Environment:**
   - Activate the virtual environment based on your operating system:
     - On Linux:
       ```
       source ./venv/bin/activate
       ```
     - On Windows:
       ```
       .\venv\Scripts\activate
       ```

7. **Install Backend Dependencies:**
   - Install the required Python packages using pip:
     ```
     pip install -r requirements.txt
     ```

8. **Start the Backend Server:**
   - Run the backend server using:
     ```
     python main.py
     ```

9. **Install and Start Redis:**
   - If Redis is not already installed, download and install it from [https://redis.io/download](https://redis.io/download), and start the Redis server.

10. **Run Celery Worker (Linux/Windows Subsystem for Linux):**
    - In the backend folder, use the following command to run the Celery worker:
      ```
      celery -A main.celeryservice worker --loglevel=INFO
      ```

11. **Run Celery Beat (Linux/Windows Subsystem for Linux):**
    - To run Celery Beat for task scheduling, use the following command:
      ```
      celery -A main.celeryservice beat --loglevel=INFO
      ```

### Frontend Setup:

12. **Navigate to the Frontend Directory:**
    - In your terminal, navigate to the `frontend` directory within the project folder.

13. **Install Frontend Dependencies:**
    - Install the required Node.js packages by running:
      ```
      npm install
      ```

14. **Run the Application:**
    - Start the frontend application by running:
      ```
      npm run serve
      ```

You're now ready to use the Show-Ticketing application locally. Access it in your web browser at [http://localhost:8080/](http://localhost:8080/).

Enjoy using the application for booking show tickets, and happy coding!
