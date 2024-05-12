import boto3

# Delete lifecycle configuration

client = boto3.client('s3')

response = client.delete_bucket_lifecycle(
    Bucket='anuj-radhaswamiji-boto3-123',
   
)