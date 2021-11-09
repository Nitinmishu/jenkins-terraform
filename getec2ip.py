import boto3

ec2 = boto3.resource('ec2',region_name='us-east-1')

def lambda_handler():
    # create filter for instances in running state
    filters = [
        {
            'Name': 'instance-state-name', 
            'Values': ['running']
        }
    ]
    
    # filter the instances based on filters() above
    instances = ec2.instances.filter(Filters=filters)

    # instantiate empty array
    RunningInstances = []

    for instance in instances:
        print(instance.__dict__)
        # for each instance, append to array and print instance id
        RunningInstances.append(instance.id)
        print (instance.id)
        
lambda_handler()

print("this is python ec2")