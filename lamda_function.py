import boto3
import time
from . import utils

   
ec2 = boto3.resource('ec2')


def lambda_handler(event, context):    
    # Get information for all running instances
    running_instances = ec2.instances.filter(Filters=[{
        'Name': 'instance-state-name',
        'Values': ['running']}])

    storedInstances =[]

    for instance in running_instances:

        if isTagEmpty(instance):
            storedInstances.append(instance)
            
    # After 6 hours we will checking if Tag is updated by that user or not.        
    time.sleep(6*3600) 

    for ins in storedInstances:
        if utils.isTagUpdated(ins):
            continue
        utils.stopInstance(ins)



# This method checks if tags are empty or not. If tags are empty it calls sendEmail method to send email to user
def isTagEmpty(instance) -> bool:
    name, email, env = "", "", ""

    for tag in instance.tags:

        if 'Name' in tag['Key']:
            name = tag.get("Value","")
            
        if "created_by" in tag["Key"]:
            email = tag.get("Value","")
            
        if "environment" in tag["Key"]:
            env = tag.get("Value","")    

    if env+name == "":
        utils.sendEmail(email,instance.id,"environment","name")
        return True

    elif not name: 
        utils.sendEmail(email,instance.id,"","name")
        return True

    elif not env:
        utils.sendEmail(email,instance.id,"enviroment","")
        return True
    
    return False  