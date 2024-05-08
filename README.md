## User Insights

This application focuses on analyzing Item 5 (Company Stock Performance) within SEC-Edgar 10-K filings, a critical section for potential investors. By examining 29 years of 10-K filings, users gain a comprehensive understanding of a company's financial performance over an extensive period. Key metrics such as revenue trends provide insights into the company's growth trajectory and financial stability.

Additionally, sentiment analysis on the data enables investors to assess market perception and sentiment surrounding the company, aiding in understanding its prospects. Detailed observations extracted from these filings can reveal significant events, trends, or patterns that may influence the company's future performance. This allows potential investors to make informed decisions and effectively manage risks within their investment portfolios.

## Tech Stack

I developed this application using a Python Flask backend and a React.js frontend. The Python backend was chosen for its compatibility with the SEC download library and Gemini LLM API, facilitating easy access to essential data. On the frontend, React.js was selected to create a visually appealing and efficient user interface that seamlessly integrates with the backend logic.

For deployment, I leveraged various AWS tools. The frontend was deployed using CloudFront and S3, while the backend was deployed on Elastic Beanstalk. Docker was employed to enable deployment of the Flask backend on Elastic Beanstalk, with potential for future Kubernetes integration.

## Demo Video

https://github.com/ShDhruvSh/SECFilingLLMDataAnalysis/assets/67289288/eee0ab2d-c025-4fdd-ab76-c8475eb9571b
