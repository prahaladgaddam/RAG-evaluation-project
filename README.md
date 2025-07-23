RAG Pipeline Evaluation Experiment
This repository contains a simple, practical guide and code to simulate and evaluate a Retrieval-Augmented Generation (RAG) pipeline. 

It demonstrates a manual evaluation process and provides a Python script to analyze the performance, highlighting key metrics like context relevance, answer faithfulness, and answer relevance.

🚀 Experiment Overview
The experiment simulates a RAG bot acting as an expert on a fictional "Nexus-7 Smart Drone". 

and You, as the evaluator, will manually:

Retrieve relevant information from the knowledge base for given queries.
Generate an answer based on the retrieved information.
Score the performance of the retrieval and generation based on defined metrics.
A Python script then aggregates these scores into a performance report.


📊 Evaluation Metrics
The evaluation focuses on three key metrics, scored from 1 to 5:

Context Relevance: How well the retrieved information matches the query.
Answer Faithfulness: Whether the generated answer only uses information from the retrieved context, indicating an "anti-hallucination metric".
Answer Relevance: How well the final answer addresses the user's problem.


📁 Files in this Repository

evaluation_template.csv: The spreadsheet where you will log and score the RAG bot's performance.
simple_analyzer.py: A Python script to calculate average scores and generate a performance report from the CSV data.
knowledgebase: Fictional Product Info

Images:

Evaluation Template
 ![evaluation template CSV_allQueries](https://github.com/user-attachments/assets/0f6954c4-3ea8-4306-8273-f154e6e18b84)

Knowledge Base
 ![knowledgebase](https://github.com/user-attachments/assets/15411f1e-a873-4ea7-a183-244e4f0eca6b)

Code Sample
 ![Code](https://github.com/user-attachments/assets/76fa2c19-0af6-4a29-8d82-12e091e4221a)



🛠️ How to Run the Experiment
Prerequisites
Python 3.x installed.


Steps
Ensure evaluation_template.csv and simple_analyzer.py are in the same directory.

Initial Run (Pre-filled Data):
Open your terminal or command prompt, navigate to the directory, and run:
![evaluation_template1](https://github.com/user-attachments/assets/a484b88a-cb4f-40a8-99c0-f629b311e8fe)



Bash

python simple_analyzer.py

(You will see a report based on the initial 3 pre-filled queries, noting a "Low Faithfulness Alert" for Query #3).

Manual Evaluation:
Open evaluation_template.csv. For query_id 4 and 5, manually:
![evaluation template CSV_allQueries](https://github.com/user-attachments/assets/9b3125c1-ad3d-4b3f-82de-e031222c1eee)

Read the user_query.

Refer to the "Knowledge Base" (from RAG experiment.txt if available, or the details below) to find retrieved_context.

Write a generated_answer.


Score 

score_context_relevance, score_faithfulness, and score_answer_relevance (1-5).

Nexus-7 Smart Drone Knowledge Base Snippets:

Key Features: 4K HDR camera, 30-minute flight time, 5-mile range, "Obstacle-Avoidance Pro" system.

Limitations: Not waterproof, requires FAA registration in the US, optimal operating temperature is 0°C to 40°C.

Support Policy: 1-year limited warranty covering manufacturing defects only. Does not cover crash damage.



Second Run (After Manual Evaluation):

Save the evaluation_template.csv file. Run the Python script again:

Bash

python simple_analyzer.py

(Observe the updated report reflecting your new data).


📈 Example Results
Report 1 (Initial Run - based on 3 queries)
![Report1](https://github.com/user-attachments/assets/dc883778-6f2b-4dd3-a7f2-9a1bdeffabe5)


========================================
📊 RAG Pipeline Evaluation Report 1 📊
========================================
Total Queries Evaluated: 3

--- Average Performance Scores (out of 5) ---
  - Context Relevance: 4.67
  - Answer Faithfulness: 4.33  <-- Key anti-hallucination metric
  - Answer Relevance: 4.67

--- Actionable Insights ---
  🔴 Low Faithfulness Alert! Review queries: 3
     These answers may be hallucinating or misrepresenting the context.

===============

This report shows how a simple script can highlight where the RAG pipeline is failing.




Report 2 (After completing queries 4 and 5 - example)
![report2](https://github.com/user-attachments/assets/00eecf36-542a-4c95-aea8-42810594f626)

========================================
📊 RAG Pipeline Evaluation Report 2📊
========================================
Total Queries Evaluated: 5

--- Average Performance Scores (out of 5) ---
  - Context Relevance: 4.80
  - Answer Faithfulness: 4.60  <-- Key anti-hallucination metric
  - Answer Relevance: 4.80

--- Actionable Insights ---
  🔴 Low Faithfulness Alert! Review queries: 3
     These answers may be hallucinating or misrepresenting the context.

==============

This report shows how a simple script can highlight where the RAG pipeline is failing.
