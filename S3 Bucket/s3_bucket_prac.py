import boto3

# [1] Get bucket encryption [2] Get bucket location i.e. Region name

client = boto3.client('s3')
# response = client.get_bucket_encryption(
#     Bucket='anuj-radhaswamiji-boto3-123',
#     ExpectedBucketOwner='964852290492'
# )

# # print(response)
# print(response['ResponseMetadata']['RequestId'])
# print(response['ResponseMetadata']['HostId'])
# print(response['ResponseMetadata']['HTTPHeaders']['date'])

response = client.get_bucket_location(
    Bucket='anuj-radhaswamiji-boto3-123',
   
)
# print(response)
bucket_location =response['LocationConstraint']
# print("Bucket Location - ", bucket_location)

# upload the file on bucket
