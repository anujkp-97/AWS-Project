import boto3

# 1. Upload the object , [2]. Delete the object [3] Enablel versioning

s3 = boto3.client('s3')
# [1] Upload a file

# s3.upload_file(r'E:\githubToken.txt', 'anuj-radhaswamiji-boto3-123', 'githubToken')

# [2] Delete the object from s3

# delete the 1 object from S3 bucket
# response = s3.delete_object(
#     Bucket='anuj-radhaswamiji-boto3-123', 
#     Key='images\anuj.jpeg',
    
# )

# [2.A] delete multiple object at one time


# response = s3.delete_objects(
#     Bucket='anuj-radhaswamiji-boto3-123',
#     Delete={
#         'Objects': [
#             {
#                 'Key': 'anuj.jpeg',
                
#             },
#             {
#                 'Key': 'githubToken',
                
#             },
#         ],
      
#     },

   
# )

# [3] Add Bucket versioning
# response = s3.put_bucket_versioning(
#     Bucket='anuj-radhaswamiji-boto3-123',
#     VersioningConfiguration={
#         'MFADelete': 'Disabled',
#         'Status': 'Enabled',
#     },
# )


# [3.A] get bucket versioning
response = s3.get_bucket_versioning(
    Bucket='anuj-radhaswamiji-boto3-123',
)
reqId =(response['ResponseMetadata']['RequestId'])
hostId =print(response['ResponseMetadata']['HostId'])
status = (response['Status'])
mfaDelete =(response['MFADelete'])

print("Request Id: ",reqId)
print("Host Id: ",hostId)
print("Status of versioning: ",status)
print("MFA Delete: ",mfaDelete)