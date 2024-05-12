import boto3

# [1] Create bucket [2] Delete bucket

client = boto3.client('s3')

# response = client.create_bucket(
    
#     Bucket='anuj-radhaswamiji-boto3-123',
#     CreateBucketConfiguration={'LocationConstraint': 'ap-south-1'}

    
# )
response = client.delete_bucket(
    Bucket='anuj-radhaswamiji-boto3-123',
    ExpectedBucketOwner='964852290492'
    
)



