import os
import requests
import csv
from google.cloud import storage

# Example sensitive information stored as variables (ideally use environment variables)
rapidapi_key = "your_api_key_here"
bucket_name = "your_bucket_name_here"

url = 'https://cricbuzz-cricket.p.rapidapi.com/stats/v1/rankings/batsmen'
headers = {
    'X-RapidAPI-Key': rapidapi_key,  # Use environment variable for API key
    'X-RapidAPI-Host': 'cricbuzz-cricket.p.rapidapi.com'
}
params = {
    'formatType': 'odi'
}

response = requests.get(url, headers=headers, params=params)

# Fetch the data
if response.status_code == 200:
    data = response.json().get('rank', [])  # Extracting the full rank data

    csv_filename = 'batsmen_rankings.csv'

    if data:
        field_names = ['rank', 'name', 'country']  # Specify required field names

        # Write data to CSV file without headers
        with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=field_names)

            for i, entry in enumerate(data, start=1):  # Ensure rank starts from 1
                entry['rank'] = i  # Set the correct rank number
                writer.writerow({field: entry.get(field) for field in field_names})

        print(f"Data fetched successfully and written to '{csv_filename}'")

        # Upload the CSV file to GCS
        storage_client = storage.Client()
        bucket = storage_client.bucket(bucket_name)
        destination_blob_name = f'{csv_filename}'  # The path to store in GCS

        blob = bucket.blob(destination_blob_name)
        blob.upload_from_filename(csv_filename)

        print(f"File {csv_filename} uploaded to GCS bucket {bucket_name} as {destination_blob_name}")
    else:
        print("No data available from the API.")
else:
    print("Failed to fetch data:", response.status_code)
