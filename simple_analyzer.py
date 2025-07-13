import csv
import os


# --- Configuration ---
CSV_FILE_NAME = 'evaluation_template.csv'


def analyze_rag_evaluations(file_path):
    """
    Reads the RAG evaluation CSV, calculates average scores, and prints a report.
    """
    # Check if the file exists
    if not os.path.exists(file_path):
        print(f"❌ Error: The file '{file_path}' was not found.")
        print("Please make sure the CSV file is in the same directory as the script.")
        return


    evaluations = []
    try:
        with open(file_path, mode='r', encoding='utf-8') as infile:
            reader = csv.DictReader(infile)
            for row in reader:
                # Only process rows that have been scored
                if row.get('score_context_relevance') and row['score_context_relevance'].strip():
                    try:
                        # Convert scores to integers for calculation
                        processed_row = {
                            'query_id': row['query_id'],
                            'context_relevance': int(row['score_context_relevance']),
                            'faithfulness': int(row['score_faithfulness']),
                            'answer_relevance': int(row['score_answer_relevance'])
                        }
                        evaluations.append(processed_row)
                    except (ValueError, KeyError) as e:
                        print(f"⚠️ Warning: Skipping row {row.get('query_id', 'N/A')} due to invalid or missing score data. Error: {e}")
    except Exception as e:
        print(f"❌ Error: Failed to read or process the CSV file. {e}")
        return


    if not evaluations:
        print("📊 No scored evaluations found in the file to analyze.")
        return


    # --- Calculations ---
    total_evals = len(evaluations)
    avg_context_relevance = sum(e['context_relevance'] for e in evaluations) / total_evals
    avg_faithfulness = sum(e['faithfulness'] for e in evaluations) / total_evals
    avg_answer_relevance = sum(e['answer_relevance'] for e in evaluations) / total_evals
    
    # Identify potential problem areas (score < 4 is a flag)
    low_faithfulness_queries = [e['query_id'] for e in evaluations if e['faithfulness'] < 4]


    # --- Reporting ---
    print("=" * 40)
    print("📊 RAG Pipeline Evaluation Report 📊")
    print("=" * 40)
    print(f"Total Queries Evaluated: {total_evals}\n")


    print("--- Average Performance Scores (out of 5) ---")
    print(f"  - Context Relevance: {avg_context_relevance:.2f}")
    print(f"  - Answer Faithfulness: {avg_faithfulness:.2f}  <-- Key anti-hallucination metric")
    print(f"  - Answer Relevance: {avg_answer_relevance:.2f}\n")


    print("--- Actionable Insights ---")
    if low_faithfulness_queries:
        print(f"  🔴 Low Faithfulness Alert! Review queries: {', '.join(low_faithfulness_queries)}")
        print("     These answers may be hallucinating or misrepresenting the context.\n")
    else:
        print("  ✅ Great job! No queries with low faithfulness scores were detected.\n")
        
    print("="*40)
    print("This report shows how a simple script can highlight where the RAG pipeline is failing.")




# --- Run the analysis ---
if __nase__ == "__main__":
    analyze_rag_evaluations(CSV_FILE_NAME)