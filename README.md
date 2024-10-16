# Cricket Statistics Data Pipeline using Google Cloud Services

## Project Overview

This project demonstrates the use of Google Cloud tools to build an automated data pipeline for cricket statistics from the Cricbuzz API. The aim is to showcase proficiency with cloud-based tools and workflows essential for modern data engineering roles.

## Tech Stack & Architecture

![Tech Stack & Architecture](https://github.com/Kai-334/Cricket-Statistics-Data-Pipeline-in-Google-Cloud-using-Airflow/blob/d9ee329ab1f4af5b02bb3bdd3e43edab2e83b296/Project%20Architecture.png)

#### **1. Data Automation with Apache Airflow**
The process starts with Apache Airflow, which is set up to run a Python script at daily intervals. This script fetches cricket statistics from the Cricbuzz API, stores the data in CSV format, and uploads it to a Google Cloud Storage (GCS) bucket.

#### **2. Storing Data in Google Cloud Storage (GCS)**
Google Cloud Storage serves as a scalable and secure repository for the collected cricket statistics in CSV format. This storage acts as the source for further data processing.

#### **3. Cloud Function Trigger**
A Cloud Function is triggered automatically when a new CSV file is uploaded to the GCS bucket. This event-driven approach enables the pipeline to move data forward as soon as it is available.

#### **4. Dataflow Job for BigQuery**
Upon triggering the Cloud Function, a Dataflow job is initiated. In this case, Dataflow simply loads the data from GCS into BigQuery, where it is ready for querying and analysis.

#### **5. Looker Studio for Data Visualization**
BigQuery acts as the data source for Looker Studio. A dynamic dashboard is created in Looker Studio to visualize the cricket statistics, offering a clear and interactive view of the data loaded into BigQuery.

---

## Key Learning Outcome:
This project demonstrates proficiency in using Google Cloud tools, including Airflow for automation, Cloud Storage for data storage, Cloud Functions for event-driven processing, Dataflow for loading data into BigQuery, and Looker Studio for data visualization. It highlights my ability to work with these tools in building a cloud-based data pipeline, which is valuable for potential employers in the data engineering field.

## Automated Data Retrieval and Upload with Apache Airflow (Cloud Composer)

![1](https://github.com/Kai-334/Cricket-Statistics-Data-Pipeline-using-Google-Cloud-Services/blob/f48ead5f6a5f864296df4d3843a290ce3fd5aa9a/Airflow.png)

## Google Cloud Storage for Cricket Statistics Data

![2](https://github.com/Kai-334/Cricket-Statistics-Data-Pipeline-using-Google-Cloud-Services/blob/f48ead5f6a5f864296df4d3843a290ce3fd5aa9a/Google%20Cloud%20Storage.png)

## Cloud Function to Trigger Dataflow Job 

![3](https://github.com/Kai-334/Cricket-Statistics-Data-Pipeline-using-Google-Cloud-Services/blob/f48ead5f6a5f864296df4d3843a290ce3fd5aa9a/Cloud%20Function.png)

## Dataflow Job to Load Data into BigQuery

![4](https://github.com/Kai-334/Cricket-Statistics-Data-Pipeline-using-Google-Cloud-Services/blob/f48ead5f6a5f864296df4d3843a290ce3fd5aa9a/dataflow.png)

## Data on BigQuery

![5](https://github.com/Kai-334/Cricket-Statistics-Data-Pipeline-using-Google-Cloud-Services/blob/f48ead5f6a5f864296df4d3843a290ce3fd5aa9a/bigQuery.png)

## Looker Studio for Data Visualisation

![6](https://github.com/Kai-334/Cricket-Statistics-Data-Pipeline-using-Google-Cloud-Services/blob/f48ead5f6a5f864296df4d3843a290ce3fd5aa9a/Looker.png)


