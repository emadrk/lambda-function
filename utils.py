import boto3
import smtplib
from email.message import EmailMessage

# Stopping ec2instance by providing instance as method arguement
def stopInstance(ins):
    instanceId=[ins.id]
    ec2 = boto3.resource('ec2')
    ec2.instances.filter(InstanceIds = instanceId).stop()

# This method is used for checking if tag is updated or not.
def isTagUpdated(instance) -> bool:
    for tag in instance.tags:

        if "testing_tag" in tag["Key"]:
            testingTag=tag.get("Value","") 

    if not testingTag:
        return False

    return True    

# This method is used to Send Email to user who has created the instance 
def sendEmail(receiverEmail,instanceId,tag1=None,tag2=None):
    msg=EmailMessage()
    
    msg['Subject'] = 'AWS ALERT'
    msg['From'] = 'Emad Khan'
    msg["To"] = receiverEmail

    if not tag2:
        msg.set_content(f"For Instance ID: {instanceId}, The  tag {tag1} is empty. Please configure it otherwise your instance will die")
    elif not tag1:
        msg.set_content(f"For Instance ID: {instanceId}, The tag {tag2} is empty. Please configure it otherwise your instance will die")   
    else:
        msg.set_content(f"For Instance ID: {instanceId}, The Tags {tag1} and {tag2} is empty. Please configure it otherwise your instance will die")     
    
    server = smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.login("emadk3@gmail.com","password")
    server.send_message(msg)
    server.quit()
           