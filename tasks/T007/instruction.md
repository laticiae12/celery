## Question

You must analyze how Celery async task flow works.

Steps:
1. Read relevant files from the Celery codebase
2. Understand how tasks move through the system

IMPORTANT:
You MUST output a JSON object with EXACTLY this format:

{
  "final_answer": "Your explanation here",
  "unique_files_read": ["file1", "file2"]
}

Rules:
- final_answer must be a detailed explanation
- It MUST include these words: task, worker, queue, broker
- unique_files_read must list real files you accessed
- Do NOT output anything outside this JSON
