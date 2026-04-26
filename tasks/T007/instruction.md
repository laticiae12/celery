## Question

You must analyze how Celery async task flow works.

Read relevant Celery source files and understand how a task moves through the system.

At the end, you MUST output ONLY this JSON:

{
  "final_answer": "Explain clearly how a task flows through Celery including task creation, broker, queue, worker, and execution.",
  "unique_files_read": ["list of actual files you opened"]
}

STRICT RULES:
- Output ONLY JSON (no explanations, no extra text)
- final_answer must include: task, worker, queue, broker
- final_answer must NOT be empty
- unique_files_read must contain real file paths from your reads
- If you output anything outside JSON, the answer is WRONG
