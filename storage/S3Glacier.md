# S3 Glacier

- **Long-term archival** solution optimized for infrequently used data, or “cold data.”
- Glacier is a REST-based web service.
- You can store an unlimited number of archives and an unlimited amount of data.
- You cannot specify Glacier as the storage class at the time you create an object.
- It is designed to provide an average annual durability of 99.999999999% for an archive. Glacier synchronously stores your data across multiple AZs before confirming a successful upload.
- To prevent corruption of data packets over the wire, Glacier uploads the checksum of the data during data upload. It compares the received checksum with the checksum of the received data and validates data authenticity with checksums during data retrieval.
- Glacier works together with **Amazon S3 lifecycle rules** to help you automate archiving of S3 data and reduce your overall storage costs. Requested archival data is copied to S3 One Zone-IA

## **Data Model**

- **Vault**
  - A container for storing archives.
  - Each vault resource has a unique address with form:  
    https://*region-specific endpoint*/*account-id*/vaults/*vaultname*
  - You can store an unlimited number of archives in a vault.
  - Vault operations are Region specific.
- **Archive**
  - Can be any data such as a photo, video, or document and is a base unit of storage in Glacier.
  - Each archive has a unique address with form:  
    https://*region-specific-endpoint*/*account-id*/vaults/*vault-name*/archives/*archive-id*
- **Job**
  - You can perform a select query on an archive, retrieve an archive, or get an inventory of a vault. Glacier Select runs the query in place and writes the output results to Amazon S3.
  - Select, archive retrieval, and vault inventory jobs are associated with a vault. A vault can have multiple jobs in progress at any point in time.
- **Notification Configuration**
  - Because jobs take time to complete, Glacier supports a notification mechanism to notify you when a job is complete.

## **Glacier Operations**

- Retrieving an archive (asynchronous operation)
- Retrieving a vault inventory (list of archives) (asynchronous operation)
- Create and delete vaults
- Get the vault description for a specific vault or for all vaults in a region
- Set, retrieve, and delete a notification configuration on the vault
- Upload and delete archives. You cannot update an existing archive.
- Glacier jobs — select, archive-retrieval, inventory-retrieval

## **Vaults**

- Vault operations are region specific.
- Vault names must be unique within an account and the region in which the vault is being created.
- You can delete a vault only if there are no archives in the vault as of the last inventory that Glacier computed and there have been no writes to the vault since the last inventory.
- You can retrieve vault information such as the vault creation date, number of archives in the vault, and the total size of all the archives in the vault.
- Glacier maintains an inventory of all archives in each of your vaults for disaster recovery or occasional reconciliation. A **vault inventory** refers to the list of archives in a vault. Glacier updates the vault inventory approximately once a day. Downloading a vault inventory is an asynchronous operation.
- You can assign your own metadata to Glacier vaults in the form of **tags**. A tag is a key-value pair that you define for a vault.
- **Glacier Vault Lock** allows you to easily deploy and enforce compliance controls for individual Glacier vaults with a vault lock policy. You can specify controls such as “**write once read many**” (WORM) in a vault lock policy and lock the policy from future edits. Once locked, the policy can no longer be changed.

## **Archives**

- Glacier supports the following basic archive operations: upload, download, and delete. Downloading an archive is an asynchronous operation.
- You can upload an archive in a single operation or upload it in parts.
- Using the multipart upload API, you can upload large archives, up to about 10,000 x 4 GB.
- You cannot upload archives to Glacier by using the management console. Use the AWS CLI or write code to make requests, by using either the REST API directly or by using the AWS SDKs.
- You cannot delete an archive using the Amazon S3 Glacier (Glacier) management console. Glacier provides an API call that you can use to delete one archive at a time.
- After you upload an archive, you cannot update its content or its description. The only way you can update the archive content or its description is by deleting the archive and uploading another archive.
- Glacier does not support any additional metadata for the archives.

## **Glacier Select**

- You can perform filtering operations using simple SQL statements directly on your data in Glacier.
- You can run queries and custom analytics on your data that is stored in Glacier, without having to restore your data to a hotter tier like S3.
- When you perform select queries, Glacier provides three data access tiers:
  - **Expedited** – data accessed is typically made available within 1–5 minutes.
  - **Standard** – data accessed is typically made available within  3–5 hours.
  - **Bulk** – data accessed is typically made available within 5–12 hours.

## **Glacier Data Retrieval Policies**

- Set data retrieval limits and manage the data retrieval activities across your AWS account in each region.
- Three types of policies:
  - Free Tier Only – you can keep your retrievals within your daily free tier allowance and not incur any data retrieval cost.
  - Max Retrieval Rate – ensures that the peak retrieval rate from all retrieval jobs across your account in a region does not exceed the bytes-per-hour limit you set.
  - No Retrieval Limit

### **Security**

- Glacier encrypts your data at rest by default and supports secure data transit with SSL.
- Data stored in Amazon Glacier is immutable, meaning that after an archive is created it cannot be updated.
- Access to Glacier requires credentials that AWS can use to authenticate your requests. Those credentials must have permissions to access Glacier vaults or S3 buckets.
- Glacier requires all requests to be signed for authentication protection. To sign a request, you calculate a digital signature using a cryptographic hash function that returns a hash value that you include in the request as your signature.
- Glacier supports policies only at the vault level.
- You can attach identity-based policies to IAM identities.
- A Glacier vault is the primary resource and resource-based policies are referred to as *vault policies*.
- When activity occurs in Glacier, that activity is recorded in a CloudTrail event along with other AWS service events in *Event History*.
