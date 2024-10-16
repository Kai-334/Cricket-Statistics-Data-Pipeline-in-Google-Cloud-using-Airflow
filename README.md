# Cricket-Statistics-Data-Pipeline-in-Google-Cloud-using-Airflow

## Tech Stack & Architecture

![Tech Stack & Architecture](https://github.com/Kai-334/Cricket-Statistics-Data-Pipeline-in-Google-Cloud-using-Airflow/blob/6eee9fd7bbed1d8b1232d8cbed8db19f9216f735/Project%20Architecture.png)

This project leverages an **end-to-end data pipeline** built with the following technologies. The diagram above illustrates how the data flows across these components:

- **Python**: Used for generating synthetic employee data with the Faker library, which is then uploaded to Google Cloud Storage.
- **Google Cloud Storage**: Acts as the raw data repository for employee information.
- **Google Cloud Data Fusion**: Handles data transformation processes, including masking and encrypting sensitive employee details, ensuring compliance with data privacy standards.
- **Google BigQuery**: Stores the transformed and cleaned data, enabling efficient querying and analysis.
- **Looker**: Provides intuitive data visualisation and reporting, helping stakeholders gain insights from the employee data.
- **Cloud Composer (Apache Airflow)**: Orchestrates and automates the entire end-to-end data pipeline, ensuring smooth workflows from data generation to final reporting.
