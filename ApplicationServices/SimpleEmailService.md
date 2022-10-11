# Amazon Simple Email Service (SES)
- Is an email platform that provides an easy, cost-effective way for you to send and receive email using your own email addresses and domains.
- Amazon SES is for applications that need to send communications via email. 
- Amazon SES supports custom email header fields, and many MIME types.

![arch_overview-diagram](/ApplicationServices/images/arch_overview-diagram.png)

## Email sending quotas

### Sending Quotas
- You can request an increase for sending quotas.

| Resource                                                     | Default Quota                                                | Adjustable |
| :----------------------------------------------------------- | :----------------------------------------------------------- | :--------- |
| Number of emails that can be sent per 24-hour period         | If your account is in the sandbox, you can send up to 200 emails per 24-hour period. If your account is out of the sandbox, this number varies based on your specific use case. | Yes        |
| Number of emails that can be sent per second (*sending rate*) | If your account is in the sandbox, you can send 1 email per second. If your account is out of the sandbox, this rate varies based on your specific use case. | Yes        |

### Message quotas

| Resource                                                     | Default Quota                              | Adjustable                                                   |
| :----------------------------------------------------------- | :----------------------------------------- | :----------------------------------------------------------- |
| Using the SES v1 API - Maximum message size (including attachments) | 10 MB per message (after base64 encoding). | No *(For workloads with message sizes in excess of 10MB, consider migrating to the SES v2 API* |
| Using the SES v2 API or SMTP - Maximum message size (including attachments) | 40 MB per message (after base64 encoding). | No                                                           |
### The following table lists the types of credentials you might use with Amazon SES, depending on what you are doing.
| If you want to access the...                                 | Use these credentials                                    | What the credentials consist of                          |
| :----------------------------------------------------------- | :------------------------------------------------------- | :------------------------------------------------------- |
| Amazon SES API(You might access the Amazon SES API directly, or indirectly through an AWS SDK, the AWS Command Line Interface, or the AWS Tools for Windows PowerShell.) | AWS access keys                                          | Access key ID and secret access key                      |
| Amazon SES SMTP interface                                    | SMTP credentials                                         | User name and password                                   |
| Amazon SES console                                           | IAM user name and password OR Email address and password | IAM user name and password OR Email address and password |

## Concepts

### SES SMTP
- You can connect directly to this SMTP interface from your applications, or configure your existing email server to use this interface as an SMTP relay.
- SES allows you to create a private SMTP relay.
- You can access your SES SMTP endpoint from your VPC privately via AWS PrivateLink through a VPC endpoint.
### Email deliverability 
- This is the percentage of your emails that arrive in your recipients inboxes.
### Reputation
- When it comes to email sending, reputation—a measure of confidence that an IP address, email address, or sending domain is not the source of spam—is important.
- Excessive bounces and complaints negatively impact your reputation and can cause SES to reduce the sending quotas for your account, or terminate your SES account.
### Bounce
- If your receiver or email provider fails to deliver your message to the recipient, the receiver bounces the message back to SES.
- SES notifies you of hard bounces and soft bounces that will no longer be retried.
### Complaint
- If the email provider concludes that you are a spammer, and SES has a feedback loop set up with the email provider 
  then the email provider will send the complaint back to SES.
### Global suppression list
- SES global suppression list is a list of recipient email addresses that have recently caused a hard bounce for any Amazon SES customer. 
- If you try to send an email through SES to an address that is on the suppression list, the call to SES succeeds, but the email is treated as a hard bounce instead of   SES attempting to send it.
### Deliveries
- This metric tells us if SES successfully delivered the email to the recipient’s mail server.
### Opens
- This metric tells us if the recipient received the message and opened it in their email client.
### Clicks
- This metric tells us if the recipient clicked one or more links in the email.
### Configuration sets
- Groups of rules that you can apply to the emails you send.
  - Event publishing – SES can track the number of send, delivery, open, click, bounce, and complaint events for each email you send. 
  - You can use event publishing to send information about these events to other AWS services.
  - IP pool management – If you lease dedicated IP addresses, you can create groups of these addresses, called dedicated IP pools. 
  - You can then associate these dedicated IP pools with configuration sets.
### Dedicated IP Pools
- If you lease several dedicated IP addresses, you can use the dedicated IP pools feature to create groups of those IP addresses. 
- You can then associate each pool with a configuration set. 
- When you send emails using a configuration set, those emails are only sent from the IP addresses in the associated pool.
- A common scenario is to create one pool of dedicated IP addresses for sending marketing communications, and another for sending transactional emails. 
- Your sender reputation for transactional emails is then isolated from that of your marketing emails.
### Dedicated IP Addresses vs Amazon SES IP Addresses
| Benefit                                                      | Shared IP addresses | Dedicated IP addresses |
| ------------------------------------------------------------ | ------------------- | ---------------------- |
| Ready to use with no additional setup                        | Yes                 | No                     |
| Reputation managed by AWS                                    | Yes                 | No                     |
| Good for customers with continuous, predictable sending patterns | Yes                 | Yes                    |
| Good for customers with less predictable sending patterns    | Yes                 | No                     |
| Good for high-volume senders                                 | Yes                 | Yes                    |
| Good for low-volume senders                                  | Yes                 | No                     |
| Additional monthly costs                                     | No                  | Yes                    |
| Complete control over sender reputation                      | No                  | Yes                    |
| Isolate reputation by email type, recipient, or other factors | No                  | Yes                    |
| Provides known IP addresses that never change                | No                  | Yes                    |
