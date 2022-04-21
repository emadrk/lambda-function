# AWS Lambda Function in Python

### Libraries Used
1. boto3-Library of Python for AWS
2. smtplib for sending email
3. time-built in library of python

### What is the flow?
1. We have created ec2 instances in AWS.

2. We have added two tags for every ec2 instances: created_by and environment.

### Understanding methods used in this project
1. In lambda_handler method, we used iterated over all running instances of ec2.

2. For each running instance, we are checking tags of the instance by calling isTagEmpty method which takes instance as arguement.

3. If tags are empty then we are storing such instance in a variable called storedInstances, Also we are sending email to the person who has created the instance to configure tags.

4. Now after iterating over all ec2 instances, we got the list of instance which had empty tags, either environment or name or both.

5. After sleep of 6 hours. We will then check if the tags are updated or not, by calling a method isTagUpdated which is in utils.py file.

6. If any instance's tag are not updated then we will stop that instance by calling a method stopInstance which is in utils.py file.

7. stopInstance method also takes instance as arguement.