from googleapiclient.discovery import build

def trigger_df_job():   
    
    # Initializing the Dataflow API Service
    service = build('dataflow', 'v1b3')

    # Setting the project ID
    project = "cricket-statistics-etl"

    # Points to a pre-built Dataflow template provided by Google
    template_path = "gs://dataflow-templates-us-central1/latest/GCS_Text_to_BigQuery"

    template_body = {
        "jobName": "bq-load",  # Provide a unique name for the job
        "parameters": {
        "javascriptTextTransformGcsPath": "gs://bucket-dataflow-required-data/udf.js",
        "JSONPath": "gs://bucket-dataflow-required-data/bq.json",
        "javascriptTextTransformFunctionName": "transform",
        "outputTable": "cricket-statistics-etl:cricket_dataset.icc_odi_bastman_ranking",
        "inputFilePattern": "bucket-cricket-data/batsmen_rankings.csv",
        "bigQueryLoadingTemporaryDirectory": "bucket-dataflow-required-data",
        }
    }

    # Launching the Dataflow Job
    request = service.projects().templates().launch(projectId=project, gcsPath=template_path, body=template_body)
    response = request.execute()
    
    print(response)