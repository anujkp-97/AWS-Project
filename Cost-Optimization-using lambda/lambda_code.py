import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')
    
    #Get all EBS snapshot
    response = ec2.describe_snapshots(OwnerIds=['self'])
    
    #Get all active ec2 instance ids
    instances_response = ec2.describe_instances(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
    active_instance_ids = set()
   
    for reservation in instances_response['Reservations']:
       for instance in reservation['Instances']:
           active_instance_ids.add(instance['InstanceId'])
           
    #Iterate
    for snapshot in response['Snapshots']:
        snapshot_id = snapshot['SnapshotId']
        volume_id = snapshot.get('VolumeId')
        
        if not volume_id:
            #delete the snapshot
            ec2.delete_snapshot(SnapshotId = snapshot_id)
            print(f"Delete EBS snapshot {snapshot_id} as it was not attached to any Volume.")
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
