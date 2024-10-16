from googleapiclient.discovery import build

def trigger_df_job(cloud_event,environment):   
 
    service = build('dataflow', 'v1b3')
    project = "rare-array-438709-t1"

    template_path = "gs://dataflow-templates-us-central1/latest/GCS_Text_to_BigQuery"

    template_body = {
        "jobName": "bq-load",  # Provide a unique name for the job
        "parameters": {
        "javascriptTextTransformGcsPath": "gs://bucket-dataflow-metadata-123/udf.js",
        "JSONPath": "gs://bucket-dataflow-metadata-123/bq.json",
        "javascriptTextTransformFunctionName": "transform",
        "outputTable": "rare-array-438709-t1:cricket_dataset.icc_odi_batsman_ranking",
        "inputFilePattern": "gs://bucket-ranking-data-123/batsmen_rankings.csv",
        "bigQueryLoadingTemporaryDirectory": "gs://bucket-dataflow-metadata-123",
        }
    }

    request = service.projects().templates().launch(projectId=project,gcsPath=template_path, body=template_body)
    response = request.execute()
    print(response)
