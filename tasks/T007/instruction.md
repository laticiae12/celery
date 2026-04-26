## Question

You must analyze how Celery async task flow works.

Read relevant Celery source files and understand how a task moves through the system.

At the end, output ONLY valid JSON in this format:

{
  "final_answer": "A clear explanation of how a Celery task flows through task creation, broker, queue, worker, and execution.",
  "unique_files_read": ["list real file paths you actually opened"]
}

Rules:
- DO NOT output anything except JSON
- DO NOT include explanations outside JSON
- final_answer MUST include the words: task, worker, queue, broker
- final_answer MUST NOT be empty
- unique_files_read MUST NOT be empty
