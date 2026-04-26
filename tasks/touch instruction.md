I’m trying to understand how asynchronous tasks are actually executed in this codebase.

When a task is triggered using the async shortcut, what happens behind the scenes from the moment it is called to when a worker processes it? Specifically, how does the system package the task, send it through the messaging layer, and eventually execute it?

I’m looking for a clear explanation of the flow across the relevant components involved.
