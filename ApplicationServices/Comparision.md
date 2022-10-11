| AWS Step Functions                                           | Amazon SQS                                                   |
| :----------------------------------------------------------- | :----------------------------------------------------------- |
| When you need to coordinate service components in the development of highly scalable and auditable applications. | When you need a reliable, highly scalable, hosted queue for sending, storing, and receiving messages between services. |
| Step Functions **keeps track** of all tasks and events in an application. | Amazon SQS requires you to **implement your own** application-level tracking, especially if your application uses multiple queues. |
| Step Functions Console and visibility APIs provide an application-centric view that lets you search for executions, drill down into an execution’s details | Amazon SQS requires implementing such additional functionality. |
| Step Functions offers several features that facilitate application development, such as passing data between tasks and flexibility in distributing tasks. | Amazon SQS requires you to implement some application-level functionality. |
| Step functions provide workflows out-of-the-box, alongside other application-level capabilities. | Can use Amazon SQS to build basic workflows to coordinate your distributed application. |

  
| AWS Step Functions                                           | **Amazon SWF**                                               |
| :----------------------------------------------------------- | :----------------------------------------------------------- |
| Consider using AWS Step Functions for all new applications, since it provides a more productive and agile approach to coordinating application components using visual workflows. | When you need **external signals** (deciders) to intervene in your processes, or you would like to launch child processes that return a result to a parent, then you should consider Amazon SWF. |
| With Step Functions, you write state machines in **declarative JSON**. | Amazon SWF, you write a **decider program** to separate activity steps from decision steps.</br>consider using AWS Step Functions for all your new applications, since it provides a more productive and agile approach to coordinating application components using visual workflows.</br>You may write decider programs in the programming language of your choice, or you may use the Flow framework to use programming constructs that structure asynchronous interactions for you. |

  
| AWS **SWF**                                                  | Amazon SQS                                                   |
| :----------------------------------------------------------- | :----------------------------------------------------------- |
| SWF API actions are **task-oriented**.                       | SQS API actions are **message-oriented**.                    |
| SWF **keeps track** of all tasks and events in an application. | Amazon SQS requires you to **implement your own** application-level tracking, especially if your application uses multiple queues. |
| SWF Console and visibility APIs provide an **application-centric view** that lets you search for executions, drill down into an execution’s details, and administer executions. | Amazon SQS requires implementing such additional functionality. |
| SWF offers several **features that facilitate application development**, such as passing data between tasks, signalling, and flexibility in distributing tasks. | Amazon SQS requires you to implement some application-level functionality. |
| In addition to a core SDK that calls service APIs, SWF provides the **Flow Framework** with which you can write distributed applications using programming constructs that structure asynchronous interactions. | Can use Amazon SQS to build basic workflows to coordinate your distributed application. |
