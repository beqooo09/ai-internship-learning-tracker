INTERVIEW_QUESTIONS = {
    "Python": [
        {
            "question": "What is the difference between a list and a tuple in Python?",
            "answer": "A list is mutable, meaning it can be changed after creation. A tuple is immutable, meaning its values cannot be changed after creation.",
            "example": "Use a list for tasks you update. Use a tuple for fixed coordinates like (10, 20)."
        },
        {
            "question": "What is a function in Python?",
            "answer": "A function is a reusable block of code that performs a specific task. It helps reduce repetition and organize code.",
            "example": "def greet(name): return f'Hello, {name}'"
        },
        {
            "question": "What is a dictionary in Python?",
            "answer": "A dictionary stores data as key-value pairs and is useful for fast lookups.",
            "example": "{'name': 'Beqir', 'skill': 'Python'}"
        }
    ],

    "SQL": [
        {
            "question": "What is the difference between INNER JOIN and LEFT JOIN?",
            "answer": "INNER JOIN returns only matching rows from both tables. LEFT JOIN returns all rows from the left table and matching rows from the right table.",
            "example": "Use LEFT JOIN when you want all customers even if some have no orders."
        },
        {
            "question": "What is GROUP BY used for?",
            "answer": "GROUP BY groups rows with the same values and allows aggregate calculations like COUNT, SUM, and AVG.",
            "example": "SELECT department, COUNT(*) FROM employees GROUP BY department;"
        },
        {
            "question": "What is a window function?",
            "answer": "A window function calculates values across related rows without collapsing the result like GROUP BY.",
            "example": "ROW_NUMBER() OVER(PARTITION BY department ORDER BY salary DESC)"
        }
    ],

    "Machine Learning": [
        {
            "question": "What is supervised learning?",
            "answer": "Supervised learning trains a model using labeled data where both inputs and correct outputs are known.",
            "example": "Predicting house prices using historical houses with known prices."
        },
        {
            "question": "What is overfitting?",
            "answer": "Overfitting happens when a model learns training data too closely and performs poorly on new data.",
            "example": "A model gets 99% training accuracy but only 60% test accuracy."
        },
        {
            "question": "What is the difference between classification and regression?",
            "answer": "Classification predicts categories. Regression predicts continuous numeric values.",
            "example": "Spam detection is classification. House price prediction is regression."
        }
    ],

    "Deep Learning": [
        {
            "question": "What is a neural network?",
            "answer": "A neural network is a model made of connected layers that learns patterns from data.",
            "example": "Neural networks can classify images, text, or audio."
        },
        {
            "question": "What is an activation function?",
            "answer": "An activation function helps neural networks learn non-linear patterns.",
            "example": "ReLU is commonly used in hidden layers."
        },
        {
            "question": "What is a CNN?",
            "answer": "A Convolutional Neural Network is commonly used for image data and learns patterns such as edges and shapes.",
            "example": "CNNs are used for image classification and object detection."
        }
    ],

    "Cloud": [
        {
            "question": "What is cloud computing?",
            "answer": "Cloud computing means using remote servers over the internet to store, process, and manage data.",
            "example": "Azure, AWS, and Google Cloud are cloud platforms."
        },
        {
            "question": "What is scalability?",
            "answer": "Scalability means increasing or decreasing computing resources based on demand.",
            "example": "An app can add more servers during high traffic."
        },
        {
            "question": "What is the difference between IaaS, PaaS, and SaaS?",
            "answer": "IaaS provides infrastructure, PaaS provides a development platform, and SaaS provides ready-to-use software.",
            "example": "Azure VMs are IaaS, Azure App Service is PaaS, Gmail is SaaS."
        }
    ],

    "Databricks": [
        {
            "question": "What is Databricks used for?",
            "answer": "Databricks is used for data engineering, analytics, machine learning, and big data processing with Apache Spark.",
            "example": "A company can use Databricks to process large datasets and build ML pipelines."
        },
        {
            "question": "What is Apache Spark?",
            "answer": "Apache Spark is a distributed data processing engine for processing large datasets quickly.",
            "example": "Spark can process large Parquet or Delta tables across multiple machines."
        },
        {
            "question": "What is a Databricks notebook?",
            "answer": "A Databricks notebook is an interactive workspace for code, queries, visualizations, and documentation.",
            "example": "A notebook can contain Python, SQL, and Markdown together."
        }
    ],

    "Computer Vision": [
        {
            "question": "What is salient object detection?",
            "answer": "Salient object detection identifies the most visually important object or region in an image.",
            "example": "In a photo of a person standing in a park, the person may be the salient object."
        },
        {
            "question": "What is image segmentation?",
            "answer": "Image segmentation divides an image into meaningful regions or objects.",
            "example": "Separating a car, road, and sky in a street image."
        }
    ],

    "Data Engineering": [
        {
            "question": "What is an ETL pipeline?",
            "answer": "ETL stands for Extract, Transform, Load. It moves data from sources, cleans or transforms it, and loads it into a destination.",
            "example": "Extract CSV data, clean it with Pandas, and load it into a database."
        },
        {
            "question": "What is data warehousing?",
            "answer": "A data warehouse stores structured data from different sources for reporting and analytics.",
            "example": "A company stores sales, customers, and product data in a warehouse for dashboards."
        }
    ]
}