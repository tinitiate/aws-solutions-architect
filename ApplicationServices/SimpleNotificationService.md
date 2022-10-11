# Amazon Simple Notification Service 
- Managed service that provides message delivery from publishers to subscribers (also known as producers and consumers).
- Publishers communicate asynchronously with subscribers by sending messages to a topic.
- Clients can subscribe to the SNS topic and receive published messages using a supported endpoint type.
-  SNS follows the “publish-subscribe” (pub-sub) messaging paradigm, with notifications being delivered to clients using a
   “push” mechanism rather than to periodically check or “poll” for new information and updates.

![sns-delivery-protocols](/ApplicationServices/images/sns-delivery-protocols.png)

## Amazon SNS provides the following features and capabilities:
- Application-to-application messaging
   - Application-to-application messaging supports subscribers such as Amazon Kinesis Data Firehose delivery streams, Lambda functions, 
     Amazon SQS queues, HTTP/S endpoints, and AWS Event Fork Pipelines. 
- Application-to-person notifications
   - Application-to-person notifications provide user notifications to subscribers such as mobile applications, mobile phone numbers, and email addresses.   
- Standard and FIFO topics
   - Use a FIFO topic to ensure strict message ordering, to define message groups, and to prevent message duplication.
   - Only Amazon SQS FIFO queues can subscribe to a FIFO topic. 
- Message durability
   - Amazon SNS uses a number of strategies that work together to provide message durability:
      - Published messages are stored across multiple, geographically separated servers and data centers.
      - If a subscribed endpoint isn't available, Amazon SNS runs a delivery retry policy.
      - To preserve any messages that aren't delivered before the delivery retry policy ends, you can create a dead-letter queue.
- Message archiving and analytics
   - You can subscribe Kinesis Data Firehose delivery streams to SNS topics, which allow you to send notifications to additional 
     archiving and analytics endpoints such as Amazon Simple Storage Service (Amazon S3) buckets, Amazon Redshift tables, and more.  
- Message attributes
  - Message attributes let you provide any arbitrary metadata about the message.they are optional and separate from, but sent along with, the message body.
  - Can use message attributes to help structure the push notification message for mobile endpoints. 
  - You can also use message attributes to make your messages filterable with subscription filter policies. You apply filter policies to topic subscriptions.
  - Message attributes contain a name, type, and value that must not be empty or null. The message body should not be empty or null also.
- Message Filtering
  - A filter policy is a simple JSON object.
  - By default, a subscriber of an SNS topic receives every message published to the topic. The filter policy contains attributes that define which messages the             subscriber receives.

## Raw Message Delivery
- By default, messages are delivered encoded in JSON that provides metadata about the message and topic.
- You can send large payload messages using AWS SDK that supports AWS Signature Version 4 signing.
- You can also enable raw message delivery for messages delivered to either SQS endpoints or HTTP/S endpoints.

## SNS Delivery Retries
- All messages sent to SNS are processed and delivered immediately. 
- If a message cannot be successfully delivered on the first attempt, SNS implements a 4-phase retry policy:
   1) retries with no delay in between attempts
   2) retries with some minimum delay between attempts
   3) retries with some back-off model (linear or exponential)
   4) retries with some maximum delay between attempts
