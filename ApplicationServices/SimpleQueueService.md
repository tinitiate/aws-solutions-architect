# Amazon Simple Queue Service (SQS)
- Amazon SQS offers a secure, durable, and available hosted queue that lets you integrate and decouple distributed software systems and components.
- Amazon SQS offers common constructs such as dead-letter queues and cost allocation tags. 
- Provides a generic web services API that you can access using any programming language that the AWS SDK supports.
- Amazon SQS supports:
  - Standard  
  - FIFO queues

|              | **Standard Queue**                                           | **FIFO Queue**                                               |
| ------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| Availability | Available in all regions                                     | Available in the US East (N.Virginia), US East (Ohio) US West (Oregon), EU (Ireland), Asia Pacific (Tokyo) regions. |
| Throughput   | **Unlimited Throughput** – Standard queues support a nearly unlimited number of transactions per seconds (TPS) per action. | **High Throughput** – By default, FIFO queues support up to 3,000 messages per second with batching,(Can request a limit increase). FIFO queues support up to 300 messages per second (300 send, receive, or delete operations per second) without batching. |
| Delivery     | **At-Least-Once Delivery** – A message is delivered at least once, but occasionally more than one copy of a message is delivered. | **Exactly-Once Processing** – A message is delivered once and remains available until a consumer processes and deletes it. Duplicates aren’t introduced into the queue. |
| Order        | **Best-Effort Ordering** – Occasionally, messages might be delivered in an order different from which they were sent. | **First-in-First-Out Delivery** – The order in which messages are sent and received is strictly preserved. |
| Use Case     | Send data between applications when the throughput is important. | Send data between applications when the order of events is important. |

- **Message timers** let you specify an initial invisibility period for a message added to a queue. The default (minimum) invisibility period for a message is 0 seconds. 
- The maximum is 15 minutes.
- You can subscribe one or more SQS queues to an Amazon SNS topic from a list of topics available for the selected queue.
- You can configure an existing SQS queue to trigger an AWS Lambda function when new messages arrive in a queue.
  - Queue and Lambda function must be in the same AWS Region.
  - FIFO queues also support Lambda function triggers.
  - You can associate only one queue with one or more Lambda functions.
  - You can’t associate an encrypted queue that uses an AWS managed Customer Master Key for SQS with a Lambda function in a different AWS account.
- You can delete all the messages in your queue by purging them.
- Long polling helps reduce the cost by eliminating the number of empty responses and false empty responses. 
  While the regular short polling returns immediately, even if the message queue being polled is empty, 
  long polling doesn’t return a response until a message arrives in the message queue, or the long poll times out.
- Short polling occurs when the WaitTimeSeconds parameter of a ReceiveMessage request is set to 0.
- SQS sets a visibility timeout, a period of time SQS prevents other consumers from receiving and processing the message. 
  - Default visibility timeout for a message is 30 seconds.
  - Minimun is 0 and Maximum is 12 Hours.
- Delay queues let you postpone the delivery of new messages to a queue for a number of seconds.
- **Dead-Letter Queues**
  - A dead-letter queue lets you set aside and isolate messages that can’t be processed correctly to determine why their processing didn’t succeed.
  - Setting up a dead-letter queue allows you to do the following:
  - Configure an alarm for any messages delivered to a dead-letter queue.
  - Examine logs for exceptions that might have caused messages to be delivered to a dead-letter queue.
  - Analyze the contents of messages delivered to a dead-letter queue to diagnose software or the producer’s or consumer’s hardware issues.
  - Determine whether you have given your consumer sufficient time to process messages.

| Quota                             | **Description**                                              |
| --------------------------------- | ------------------------------------------------------------ |
| Delay queue                       | The default (minimum) delay for a queue is 0 seconds. The maximum is 15 minutes. |
| Messages per queue (in flight)    | For most standard queues , there can be a maximum of approximately 120,000 inflight messages (received from a queue by a consumer, but not yet deleted from the queue). You can request a limit increase.</br>For FIFO queues, there can be a maximum of 20,000 inflight messages (received from a queue by a consumer, but not yet deleted from the queue). |
| Messages per queue (backlog)      | Unlimited                                                    |
| Listed queues                     | 1,000 queues per ListQueues request.                         |
| Queue name</br>Batched message ID | A queue name can have up to 80 characters. The following characters are accepted: alphanumeric characters, hyphens, and underscores. Queue names are case-sensitive.</br>The name of a FIFO queue must end with the .fifo suffix. The suffix counts towards the 80-character queue name limit. |
| Long polling wait time            | The maximum long polling wait time is 20 seconds.            |
| Message attributes                | A message can contain up to 10 metadata attributes.          |
| Message batch                     | A single message batch request can include a maximum of 10 messages. |
| Message content                   | A message can include only XML, JSON, and unformatted text.  |
| Message throughput                | Standard queues support a nearly unlimited number of transactions per second (TPS) per action. </br>By default, FIFO queues support up to 3,000 messages per second with batching. FIFO queues support up to 300 messages per second (300 send, receive, or delete operations per second) without batching. |
| Message retention                 | By default, a message is retained for 4 days. The minimum is 60 seconds . The maximum is 14 days. |
| Message visibility timeout        | The default visibility timeout for a message is 30 seconds. The minimum is 0 seconds. The maximum is 12 hours. |
