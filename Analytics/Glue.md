# AWS Glue

- AWS Glue is a serverless data integration service that makes it easy for analytics users to discover, prepare, move, and integrate data from multiple sources.

- AWS Glue consists of:
  - Central metadata repository
  - ETL engine
  - Flexible scheduler

![HowItWorks-overview](C:\Users\sboard\OneDrive\Desktop\HowItWorks-overview.png)

- You define *jobs* in AWS Glue to accomplish the work that's required to extract, transform, and load (ETL) data from a data source to a data target. 
- Typically perform the following actions:
  - For data store sources, you define a *crawler* to populate your AWS Glue Data Catalog with metadata table definitions. You point your crawler at a data store, and the crawler creates table definitions in the Data Catalog. For streaming sources, you manually define Data Catalog tables and specify data stream properties. You can run your job on demand, or you can set it up to start when a specified *trigger* occurs. The trigger can be a time-based schedule or an event.
  - AWS Glue can generate a script to transform your data. Or, you can provide the script in the AWS Glue console or API.
  - You can run your job on demand, or you can set it up to start when a specified *trigger* occurs. The trigger can be a time-based schedule or an event. When your job runs, a script extracts data from your data source, transforms the data, and loads it to your data target. The script runs in an Apache Spark environment in AWS Glue.

## AWS Glue terminology

- AWS Glue relies on the interaction of several components to create and manage your extract, transfer, and load (ETL) workflow.

### AWS Glue Data Catalog

- The persistent metadata store in AWS Glue.
- It contains table definitions, job definitions, and other control information to manage your AWS Glue environment.
- You can only use one data catalog per region.
- AWS Glue Data catalog can be used as the Hive metastore.

### Classifier

- Determines the schema of your data. 
- AWS Glue provides classifiers for common file types, such as CSV, JSON, AVRO, XML, and others.
- AWS Glue also provides classifiers for common relational database management systems using a JDBC connection. 
- We can write your own classifier by using a grok pattern or by specifying a row tag in an XML document.

### Connection

- Data Catalog object that contains the properties that are required to connect to a particular data store.
- To store connection information for a data store, you can add a connection using:
  - JDBC
  - Amazon RDS
  - Amazon Redshift
  - Amazon DocumentDB
  - MongoDB
  - Kafka
  - Network
- We can enable SSL connection for JDBC, Amazon RDS, Amazon Redshift, and MongoDB.

### Crawler

- You can use crawlers to populate the AWS Glue Data Catalog with tables.
- Crawlers can crawl file-based and table-based data stores.
  - Data stores: S3, JDBC, DynamoDB, Amazon DocumentDB, and MongoDB
- It can crawl multiple data stores in a single run.
- How Crawlers work
  - **Determine the format, schema, and associated properties of the raw data by classifying the data** – create a custom classifier to configure the results of the classification.
  - **Group the data into tables or partitions** – you can group the data based on the crawler heuristics.
  - **Writes metadata to the AWS Glue Data Catalog** – set up how the crawler adds, updates, and deletes tables and partitions.
- For incremental datasets with a stable table schema, you can use incremental crawls. It only crawls the folders that were added since the last crawler run.
- You can run a crawler on-demand or based on a schedule.

### Database

- A set of associated Data Catalog table definitions organized into a logical group.
- A container for tables that define data from different data stores.
- A link to a local or shared database is called a *database resource link*.

### Data store, data source, and data target

- A *data store* is a repository for persistently storing your data.
- Data stores: Amazon S3, Amazon RDS, Amazon Redshift, Amazon DynamoDB, JDBC.
- The *data source* is used as input to a process or transform.
- A location where the data store process or transform writes to is called a *data target*.

### Development endpoint

- An environment that allows you to develop and test your ETL scripts.
- To create and test AWS Glue scripts, you can connect the development endpoint using:
  - Apache Zeppelin notebook on your local machine
  - Zeppelin notebook server in Amazon EC2 instance
  - SageMaker notebook
  - Terminal window
  - PyCharm Python IDE
- With SageMaker notebooks, you can share development endpoints among single or multiple users.
  - Single-tenancy Configuration
  - Multi-tenancy Configuration

### Dynamic Frame

- A distributed table that supports nested data.
- A record for self-describing is designed for schema flexibility with semi-structured data.
- Each record consists of data and schema.
- You can use dynamic frames to provide a set of advanced transformations for data cleaning and ETL.

### Job

- The business logic that is required to perform ETL work.
- It is composed of a transformation script, data sources, and data targets.
- Job runs are initiated by triggers that can be scheduled or triggered by events.
- Job types:
  - Spark
  - Streaming ETL
  - Python shell
- Job properties:
  - *Job bookmarks* maintain the state information and prevent the reprocessing of old data.
  - *Job metrics* allows you to enable or disable the creation of CloudWatch metrics when the job runs.
  - *Security configuration* helps you define the encryption options of the ETL job.

### Notebook Sever

- A web-based environment to run PySpark statements.
- You can use a notebook server for interactive development and testing of your ETL scripts on a development endpoint.
  - SageMaker notebooks server
  - Apache Zeppelin notebook server

###  Script

- A script allows you to extract the data from sources, transform it, and load the data into the targets.
- You can generate ETL scripts using Scala or PySpark.
- AWS Glue has a script editor that displays both the script and diagram to help you visualize the flow of your data.

### Table

- The metadata definition that represents your data.

- You can define tables using JSON, CSV, Parquet, Avro, and XML.
- You can use the table as the source or target in a job definition.
- A link to a local or shared table is called a t*able resource link*.
- To add a table definition:
  - Run a crawler.
  - Create a table manually using the AWS Glue console.
  - Use AWS Glue API CreateTable operation.
  - Use AWS CloudFormation templates.
  - Migrate the Apache Hive metastore
- A partitioned table describes an AWS Glue table definition of an Amazon S3 folder.
- Reduce the overall data transfers, processing, and query processing time with *PartitionIndexes*.

### Transform

- The code logic that is used to manipulate your data into a different format.
- Enables you to manipulate your data into different formats.

### Trigger

- Initiates an ETL job. 
- Triggers can be defined based on a scheduled time or an event.

### Worker

- It helps you orchestrate ETL jobs, triggers, and crawlers.
- Workflows can be created using the AWS Management Console or AWS Glue API.
- You can visualize the components and the flow of work with a graph using the AWS Management Console.
- Jobs and crawlers can fire an event trigger within a workflow.
- By defining the default workflow run properties, you can share and manage state throughout a workflow run.
- With AWS Glue API, you can retrieve the static and dynamic view of a running workflow.
- The *static view* shows the design of the workflow. While the *dynamic view* includes the latest run information for the jobs and crawlers. Run information shows the success status and error details.
- You can stop, repair, and resume a workflow run.

 