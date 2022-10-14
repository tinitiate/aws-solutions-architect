# Amazon Athena

- Amazon Athena is an interactive query service that makes it easy to analyze data directly in Amazon Simple Storage Service (Amazon S3) using standard SQL.
- Athena is serverless, so there is no infrastructure to set up or manage, and you pay only for the queries you run. 
- Athena scales automatically—running queries in parallel—so results are fast, even with large datasets and complex queries.
- Has a built-in query editor.
- Uses *Presto*, an open source, distributed SQL query engine optimized for low latency, ad hoc analysis of data.
- Athena supports a wide variety of data formats such as CSV, JSON, ORC, Avro, or Parquet.
- Athena automatically executes queries in **parallel**, so that you get query results in seconds, even on large datasets.
- Athena uses Amazon S3 as its underlying data store, making your data highly available and durable.
- Athena integrates with Amazon QuickSight for easy data visualization.
- Athena integrates out-of-the-box with AWS Glue.
- Athena uses a managed **Data Catalog** to store information and schemas about the databases and tables that you create for your data stored in S3.

## **Partitioning**

- By partitioning your data, you can restrict the amount of data scanned by each query, thus improving performance and reducing cost.
- Athena leverages *Hive* for partitioning data.
- You can partition your data by any key.

## **Queries**

- You can query geospatial data.
- You can query different kinds of logs as your datasets.
- Athena stores query results in S3.
- Athena retains query history for 45 days.
- Athena does not support user-defined functions, *INSERT INTO* statements, and stored procedures.
- Athena supports both simple data types such as INTEGER, DOUBLE, VARCHAR and complex data types such as MAPS, ARRAY and STRUCT.
- Athena supports querying data in Amazon S3 Requester Pays buckets.

## **Security**

- Control access to your data by using IAM policies, access control lists, and S3 bucket policies.
- If the files in the target S3 bucket is encrypted, you can perform queries on the encrypted data itself.