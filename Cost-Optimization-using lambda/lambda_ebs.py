import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')
     
    # Get all EBS snapshots
    response_snapshots = ec2.describe_snapshots(OwnerIds=['self'])
    snapshots = response_snapshots['Snapshots']
    
    # Get all active EC2 instance IDs
    response_instances = ec2.describe_instances(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
    active_instance_ids = [instance['InstanceId'] for reservation in response_instances['Reservations'] for instance in reservation['Instances']]
    
    # Iterate over snapshots
    for snapshot in snapshots:
        snapshot_id = snapshot['SnapshotId']
        volume_id = snapshot.get('VolumeId')
        
        # Check if snapshot is not attached to any volume or associated EC2 instance is terminated
        if not volume_id or volume_id.split('-')[1] not in active_instance_ids:
            # Delete the snapshot
            ec2.delete_snapshot(SnapshotId=snapshot_id)
            print(f"Deleted EBS snapshot {snapshot_id} as it was not attached to any Volume or associated EC2 instance is terminated.")
        else:
            #check if volume still exists
            try: 
                volume_response = ec2.describe_volumes(VolumneIds= [volume_id])
                if not volume_response['Volumes'][0]['Attachements']:
                    ec2.delete_snapshot(SnapshotId=snapshot_id)
                    print(f"Deleted EBS Snapshot {snapshot_id} as it was taken from the volume not attached")
            except ec2.exceptions.ClientError as e:
                if e.response['Error']['Code'] == 'InvalidVolume.NotFound':
                # The volume associated with it is not found, it might have been deleted
                    ec2.delete_snapshot(SnapshotId=snapshot_id)
                    print(f"Deleted EBS snapshot {snapshot_id} as its associated volume was not found.")
