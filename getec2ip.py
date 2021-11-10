
import boto3
import paramiko

def func_do_ssh_Stuff(address, usr, pwd, command):
        try:
            print("ssh " + usr + "@" + address + ", running : " +
                         command)
            client = paramiko.SSHClient()
            client.load_system_host_keys() # this loads any local ssh keys
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

            client.connect(address, username=usr, password=pwd)
            _, ss_stdout, ss_stderr = client.exec_command(command)
            r_out, r_err = ss_stdout.readlines(), ss_stderr.read()
            print(r_err)
            if len(r_err) > 5:
                print(r_err)
            else:
                print(r_out)
            client.close()
        except IOError:
            print(".. host " + address + " is not up")
            return "host not up", "host not up"


ec2 = boto3.resource('ec2',region_name='us-east-1')

def lambda_handler():
    # create filter for instances in running state
    filters = [
        {
            'Name':'tag:Name',
            'Values':['my-ec2-instance']
        },
        {
            'Name': 'instance-state-name',
            'Values': ['running']
        }
    ]

    # filter the instances based on filters() above
    instances = ec2.instances.filter(Filters=filters)
    #import pdb; pdb.set_trace()
    # instantiate empty array
    RunningInstances = []

    for instance in instances:
        print(instance.__dict__)
        # for each instance, append to array and print instance id
        RunningInstances.append(instance.id)
        print (instance.id,instance.public_ip_address,instance.private_ip_address,instance.tags)

lambda_handler()

print("this is python ec2")
