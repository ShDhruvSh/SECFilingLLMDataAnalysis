## User Insights

This application focuses on analyzing Item 5 (Company Stock Performance) within SEC-Edgar 10-K filings, a critical section for potential investors. By examining 29 years of 10-K filings, users gain a comprehensive understanding of a company's financial performance over an extensive period. Key metrics such as revenue trends provide insights into the company's growth trajectory and financial stability.

Additionally, sentiment analysis on the data enables investors to assess market perception and sentiment surrounding the company, aiding in understanding its prospects. Detailed observations extracted from these filings can reveal significant events, trends, or patterns that may influence the company's future performance. This allows potential investors to make informed decisions and effectively manage risks within their investment portfolios.

## Tech Stack

I developed this application using a Python Flask backend and a React.js frontend. The Python backend was chosen for its compatibility with the SEC download library and Gemini LLM API, facilitating easy access to essential data. On the frontend, React.js was selected to create a visually appealing and efficient user interface that seamlessly integrates with the backend logic.

For deployment, I leveraged various AWS tools. The frontend was deployed using CloudFront and S3, while the backend was deployed on Elastic Beanstalk. Docker was employed to enable deployment of the Flask backend on Elastic Beanstalk, with potential for future Kubernetes integration.

## Demo Video

https://github.com/ShDhruvSh/SECFilingLLMDataAnalysis/assets/67289288/eee0ab2d-c025-4fdd-ab76-c8475eb9571b

## Running the App Locally

Follow these steps to run the application on your local machine:

1. **Clone the Repository**:  
   Clone the repository from GitHub using the following command:
   ```
   git clone https://github.com/ShDhruvSh/SECFilingLLMDataAnalysis
   ```

2. **Set up Environment Variables**:  
   - Create an `.env` file in the frontend directory and add the following line:
     ```
     REACT_APP_API_URL="http://localhost:5000/"
     ```
   - Create an `.env` file in the backend directory and add your Gemini API key and email in the following format:
     ```
     GEMINI_API_KEY=<your_gemini_api_key>
     USER_EMAIL=<your_email>
     ```

3. **Install Dependencies**:  
   Navigate to the root directory of the project and run the following command to install backend dependencies:
   ```
   pip install -r requirements.txt
   ```

4. **Run Flask Server**:  
   Start the Flask server by running the following command in the backend directory:
   ```
   python backend.py
   ```
   or
   ```
   flask run --debug
   ```

6. **Install and Run React Server**:  
   Navigate to the frontend directory and install frontend dependencies:
   ```
   npm install
   ```
   Once dependencies are installed, start the React server with the following command:
   ```
   npm start
   ```

7. **Access the Application**:  
   Once both servers are running, access the application by opening your web browser and navigating to `http://localhost:3000/`.

8. **Interact with the App**:  
   You can now interact with the application locally, explore its features, and analyze the insights it provides.
