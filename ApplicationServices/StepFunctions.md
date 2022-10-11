# AWS Step Functions
- AWS Step Functions is a serverless orchestration service that lets you integrate with AWS Lambda functions and other AWS services to build applications.
- Step Functions is based on state machines and tasks.
- You define state machines using the JSON-based Amazon States Language.
- A state machine is a workflow.
- A task is a state in a workflow that represents a single unit of work that another AWS service performs.
- Each step in a workflow is a state.
- Workflow Types:
  - Standard 
  - Express 
- **Standard Workflow**
  - Standard workflows have exactly-once workflow execution and can run for up to one year.
  - Each step in a Standard workflow will execute exactly-once. 
  - Standard workflows are ideal for long-running, auditable workflows, as they show execution history and visual debugging. 
- **Express Workflow**
  - Express workflows have at-least-once workflow execution and can run for up to five minutes.
  - One or more steps in an Express Workflow can execute more than once,while each step in the workflow executes at-least-once.
  - Express workflows are ideal for high-event-rate workloads, such as streaming data processing and IoT data ingestion.
  
|                                 | Standard Workflows                                           | Express Workflows: Synchronous and Asynchronous              |
| :------------------------------ | :----------------------------------------------------------- | :----------------------------------------------------------- |
| Maximum duration                | 1 year                                                       | 5 minutes                                                    |
| Supported execution start rate  | Over 2,000 per second                                        | Over 100,000 per second                                      |
| Supported state transition rate | Over 4,000 per second per account                            | Nearly unlimited                                             |
| Pricing                         | Priced per state transition. A state transition is counted each time a step in your execution is completed. | Priced by the number of executions you run, their duration, and memory consumption. |
| Execution history               | Executions can be listed and described with Step Functions APIs, and visually debugged through the console. They can also be inspected in CloudWatch Logs by enabling logging on your state machine. | Unlimited execution history, that is, as many execution history entries are maintained as you can generate within a 5-minute period. Further, executions can be inspected in CloudWatch Logs by enabling logging on your state machine. |
| Execution semantics             | Exactly-once workflow execution.                             | *Asynchronous Express Workflows*: At-least-once workflow execution. *Synchronous Express Workflows*: At-most-once workflow execution. |
| Service integrations            | Supports all service integrations and patterns.              | Supports all service integrations. **Note**Express Workflows do not support Job-run (.sync) or Callback (.waitForTaskToken) service integration patterns. |
| Step Functions activities       | Supports Step Functions activities.                          | Does not support Step Functions activities.                  |
- A state is referred to by its name, which can be any string, but which must be unique within the scope of the entire state machine. 
  An instance of a state exists until the end of its execution.
- State Types:
  - Task state – Do some work in your state machine. 
  - Choice state – Make a choice between branches of execution.
  - Fail state – Stops execution and marks it as failure
  - Succeed state – Stops execution and marks it as a success
  - Pass state – Simply pass its input to its output or inject some fixed data.
  - Wait state – Provide a delay for a certain amount of time.
  - Parallel state – Begin parallel branches of execution.
  - Map state – Adds a for-each loop condition
- State machine updates in AWS Step Functions are eventually consistent.
- By default, when a state reports an error, AWS Step Functions causes the execution to fail entirely.
  - Task and Parallel states can have a field named Retry and Catch to retry an execution or to have a fallback state.
- Step Functions has built-in fault tolerance and maintains service capacity across multiple Availability Zones in each region.
- Step Functions automatically scales the operations and underlying compute to run the steps of your application for you in response to changing workloads.
- AWS Step Functions has a 99.9% SLA.
- When creating a state machine, only the States field is required in the JSON document.


