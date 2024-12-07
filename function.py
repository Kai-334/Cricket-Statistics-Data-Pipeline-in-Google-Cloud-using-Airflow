from googleapiclient.discovery import build
from google.cloud import bigquery

def trigger_df_job(cloud_event, environment):   
    
    # Initializing the Dataflow API Service
    service = build('dataflow', 'v1b3')

    # Initialize BigQuery client
    bq_client = bigquery.Client()

    # Setting the project ID
    project_id = "cricket-statistics-etl"

    # BigQuery table details
    dataset_id = "cricket_dataset"
    table_id = "icc_odi_bastman_ranking"
    table = f"{project_id}.{dataset_id}.{table_id}"

    # Step 1: Clear the BigQuery table
    delete_query = f"DELETE FROM `{table}` WHERE TRUE"
    bq_client.query(delete_query).result()  # Execute query and wait for it to finish

    # Points to a pre-built Dataflow template provided by Google
    template_path = "gs://dataflow-templates-us-central1/latest/GCS_Text_to_BigQuery"

    template_body = {
        "jobName": "bq-load",  # Provide a unique name for the job
        "parameters": {
        "javascriptTextTransformGcsPath": "gs://bucket-dataflow-required-data/udf.js",
        "JSONPath": "gs://bucket-dataflow-required-data/bq.json",
        "javascriptTextTransformFunctionName": "transform",
        "outputTable": "cricket-statistics-etl:cricket_dataset.icc_odi_bastman_ranking",
        "inputFilePattern": "gs://bucket-cricket-data/batsmen_rankings.csv",
        "bigQueryLoadingTemporaryDirectory": "gs://bucket-dataflow-required-data"
        }
    }

    # Step 2: Launch the Dataflow Job
    request = service.projects().templates().launch(projectId=project_id, gcsPath=template_path, body=template_body)
    response = request.execute()

    print(response)