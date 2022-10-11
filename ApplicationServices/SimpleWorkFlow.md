# Amazon Simple WorkFlow (SWF)
- Amazon SWF makes it easy to build applications that coordinate work across distributed components. 
- Task represents a logical unit of work that is performed by a component of your application.
- Coordinating tasks across the application involves managing intertask dependencies, scheduling, and 
  concurrency in accordance with the logical flow of the application. 
- Amazon SWF gives you full control over implementing tasks and coordinating them.
- Amazon SWF also provides the AWS Flow Framework to help developers use asynchronous programming in the development of their applications.
- Amazon SWF lets you write your application components and coordination logic in any programming language.
- Amazon SWF lets us run the application components and logic in cloud or on-prem.
- Amazon SWF manages workflow execution history and other details of your workflows across availability zones.
- Deciders and activity workers communicate with SWF using long polling.
- SWF provides endpoints in different regions.
- AWS Flow Framework is an SDK for writing distributed, asynchronous programs that can run as workflows on SWF.

## Amazon SWF Concepts
### Workflow 
- A workflow is a set of activities that carry out some objective, together with logic that coordinates the activities.
- Each workflow runs in an AWS resource called a domain, which controls the workflow's scope. 
- AWS account can have multiple domains, each of which can contain multiple workflows, but workflows in different domains can't interact.
- Parallel and sequential workflows can be run asynchronously across multiple computers.
### Activity Worker 
- An activity worker is a program that receives activity tasks, performs them, and provides results back.
### Activity Task
- An activity task tells an activity worker to perform its function.
- SWF stores tasks and assigns them to workers when they are ready.
- Activity tasks—and the activity workers that perform them—can run synchronously or asynchronously.
- Different activity workers can be written in different programming languages and run on different operating systems.
- If you don’t specify a task list when scheduling an activity task, the task is automatically placed on the default task list.
### Decider
- The coordination logic in a workflow is contained in a software program called a decider.
- The decider schedules activity tasks, provides input data to the activity workers, 
  processes events that arrive while the workflow is in progress, and ultimately ends (or closes) the workflow.
- The decider directs the workflow by receiving decision tasks from Amazon SWF and responding back to Amazon SWF with decisions.
### Decision Task
- A Decision task tells a decider that the state of the workflow execution.
- Decision task contains the current workflow history.
- Amazon SWF assigns each decision task to exactly one decider and allows only one decision task at a time to be active in a workflow execution.
- Deciders and activity workers communicate with SWF using long polling.
### Workflow Execution
1. Write activity workers that implement the processing steps in your workflow.
2. Write a decider to implement the coordination logic of your workflow.
3. Register your activities and workflow with Amazon SWF.
4. Start your activity workers and decider.
5. Start one or more executions of your workflow. 
  1. Each execution runs independently and you can provide each with its own set of input data. 
  2. When an execution is started, Amazon SWF schedules the initial decision task. 
  3. In response, your decider begins generating decisions which initiate activity tasks. 
  4. Execution continues until your decider makes a decision to close the execution.
6. Filter and view complete details of executions.
## Quotas for Amazon SWF
- Maximum registered domains – 100
- Maximum workflow and activity types – 10,000 each per domain
- Maximum request size – 1 MB per request
- Maximum open workflow executions – 100,000 per domain
- Maximum workflow execution time – 1 year
- Maximum workflow execution history size – 25,000 events
- Maximum task execution time – 1 year
- Maximum time SWF will keep a task in the queue – 1 year 

