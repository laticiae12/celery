## Question

You are required to analyze how Celery async task flow works.

You MUST:
1. Read relevant Celery source files
2. Understand how tasks move through:
   - task creation
   - broker/queue
   - worker execution

FINAL OUTPUT REQUIREMENT (CRITICAL):

You MUST return ONLY valid JSON in this exact format:

{
  "final_answer": "A clear explanation of how Celery async tasks flow from task → broker → queue → worker → execution",
  "unique_files_read": ["file1", "file2"]
}

Rules:
- DO NOT print anything before or after the JSON
- final_answer MUST include these words:
  "task", "worker", "queue", "broker"
- unique_files_read must include actual file paths you opened
- final_answer must NOT be empty
- If you fail to output JSON, the task is incorrect
