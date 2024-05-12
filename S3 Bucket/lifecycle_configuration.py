import boto3

def create_bucket_lifecycle_configuration(bucket_name, region):
    # Create an S3 client
    s3 = boto3.client('s3', region_name=region)

    # Define the lifecycle configuration rules
    lifecycle_configuration = {
        'Rules': [
            {
                'ID': 'expire-rule',
                'Filter': {
                    'Prefix': 'radhaswamiji-lifecycle-configuartion'
                },
                'Status': 'Enabled',
                'Transitions': [
                    {
                        'Days': 90,
                        'StorageClass': 'GLACIER'
                    },
                ],
                'Expiration': {
                    'Days': 180
                }
                
            }
            # Add more rules if needed
        ]
    }

    # Set the lifecycle configuration for the bucket
    s3.put_bucket_lifecycle_configuration(
        Bucket=bucket_name,
        LifecycleConfiguration=lifecycle_configuration
    )

    print(f"Lifecycle configuration set for bucket '{bucket_name}'.")


bucket_name = 'anuj-radhaswamiji-boto3-123'

region = 'ap-south-1'

# Call the function 
create_bucket_lifecycle_configuration(bucket_name, region)
