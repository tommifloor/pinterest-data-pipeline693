# Pinterest Data Pipeline

![Static Badge](https://img.shields.io/badge/made%20with-Python-blue)
![GitHub License](https://img.shields.io/github/license/tommifloor/pinterest-data-pipeline693)
![GitHub last commit](https://img.shields.io/github/last-commit/tommifloor/pinterest-data-pipeline693)
![Static Badge](https://img.shields.io/badge/made_for-AiCore-red) 

# Table of Contents
1. [Overview](#1.-project-overview)
3. [Services & Tools](#3.-services-&-tools)
6. [Batch Processing](#6.-batch-processing)
7. [Stream Processing](#7.-stream-processing)
7. [Folder Structure](#7.-folder-structure)
8. [License](#8.-license)

## 1. Overview
A simulated data pipeline using AWS and Databricks. Made for [the AiCore Data Engineering Bootcamp](https://www.theaicore.com/launch/data-engineering).

## 3. Setup
| text | text |

## 3. Services & Tools
- [Apache Airflow](https://airflow.apache.org/):
> Apache Airflow is a platform created by the community to programmatically author, schedule and monitor workflows. 
- [Apache Kafka](https://kafka.apache.org/):
> Apache Kafka is an open-source distributed event streaming platform used by thousands of companies for high-performance data pipelines, streaming analytics, data integration, and mission-critical applications. 
- [Apache Spark](https://spark.apache.org/):
> Apache Spark is a multi-language engine for executing data engineering, data science, and machine learning on single-node machines or clusters. 
- [Confluent.io Kafka REST Proxy](https://docs.confluent.io/platform/current/kafka-rest/index.html):
> The Confluent REST Proxy provides a RESTful interface to an Apache Kafka® cluster, making it easy to produce and consume messages, view the state of the cluster, and perform administrative actions without using the native Kafka protocol or clients.
- [Databricks](https://www.databricks.com/):
> The Databricks Data Intelligence Platform allows your entire organization to use data and AI. It’s built on a lakehouse to provide an open, unified foundation for all data and governance, and is powered by a Data Intelligence Engine that understands the uniqueness of your data.
>The winners in every industry will be data and AI companies. From ETL to data warehousing to generative AI, Databricks helps you simplify and accelerate your data and AI goals.
- [AWS API Gateway](https://aws.amazon.com/api-gateway/):
> Amazon API Gateway is a fully managed service that makes it easy for developers to create, publish, maintain, monitor, and secure APIs at any scale. APIs act as the "front door" for applications to access data, business logic, or functionality from your backend services. Using API Gateway, you can create RESTful APIs and WebSocket APIs that enable real-time two-way communication applications. API Gateway supports containerized and serverless workloads, as well as web applications.
> API Gateway handles all the tasks involved in accepting and processing up to hundreds of thousands of concurrent API calls, including traffic management, CORS support, authorization and access control, throttling, monitoring, and API version management. API Gateway has no minimum fees or startup costs. You pay for the API calls you receive and the amount of data transferred out and, with the API Gateway tiered pricing model, you can reduce your cost as your API usage scales.
- [AWS EC2](https://aws.amazon.com/ec2/):
> Amazon Elastic Compute Cloud (Amazon EC2) offers the broadest and deepest compute platform, with over 750 instances and choice of the latest processor, storage, networking, operating system, and purchase model to help you best match the needs of your workload. We are the first major cloud provider that supports Intel, AMD, and Arm processors, the only cloud with on-demand EC2 Mac instances, and the only cloud with 400 Gbps Ethernet networking. We offer the best price performance for machine learning training, as well as the lowest cost per inference instances in the cloud. More SAP, high performance computing (HPC), ML, and Windows workloads run on AWS than any other cloud.
- [AWS IAM](https://aws.amazon.com/iam/):
> Use AWS Identity and Access Management (IAM) to manage and scale workload and workforce access securely supporting your agility and innovation in AWS.
- [AWS Kinesis](https://aws.amazon.com/kinesis/):
> Amazon Kinesis cost-effectively processes and analyzes streaming data at any scale as a fully managed service. With Kinesis, you can ingest real-time data, such as video, audio, application logs, website clickstreams, and IoT telemetry data, for machine learning (ML), analytics, and other applications.
- [AWS MSK](https://aws.amazon.com/msk/):
> Amazon Managed Streaming for Apache Kafka
Securely stream data with a fully managed, highly available Apache Kafka service
- [AWS MSK CONNECT](https://aws.amazon.com/msk/features/msk-connect/): 
> With Amazon MSK Connect, a feature of Amazon MSK, you can run fully managed Apache Kafka Connect workloads on AWS. This feature makes it easy to deploy, monitor, and automatically scale connectors that move data between Apache Kafka clusters and external systems such as databases, file systems, and search indices. MSK Connect is fully compatible with Kafka Connect, enabling you to lift and shift your Kafka Connect applications with zero code changes. With MSK Connect, you only pay for connectors you are running, without the need for cluster infrastructure.
- [AWS S3](https://aws.amazon.com/s3/):
> Amazon Simple Storage Service (Amazon S3) is an object storage service offering industry-leading scalability, data availability, security, and performance. Millions of customers of all sizes and industries store, manage, analyze, and protect any amount of data for virtually any use case, such as data lakes, cloud-native applications, and mobile apps. With cost-effective storage classes and easy-to-use management features, you can optimize costs, organize and analyze data, and configure fine-tuned access controls to meet specific business and compliance requirements.

Python Modules:
```
- airflow X
- boto3 X
- datetime
- json
- multiprocessing
- pymysql x
- random
- requests X
- sqlalchemy x
- time
- yaml x
```

### 6. Batch Processing

### 7. Streaming Processing

## 7. Folder Structure
```
├── README.md / documentation
├── COPYING.txt / license
├── env
│   └── env.yaml / conda env
│
├── user_posting_emulation.py / batch processing
├── user_posting_emulation_streaming.py / kinesis streaming
│
├── databricks
│   └── databricks notebooks / data processing
├── airflow
│   └── dag.py / batch scheduling
│
├── credentials
│   └── SSH & API keys / security
└── ignore
    └── misc.py / debugging
```
## 8. License
Licensed under [GPL-3.0](https://github.com/tommifloor/pinterest-data-pipeline693/blob/main/COPYING.txt).

---
[Jump to Top](#pinterest-data-pipeline)