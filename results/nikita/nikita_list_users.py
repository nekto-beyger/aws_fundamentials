import boto3

client = boto3.client('iam')

def lambda_handler(event, context):
    
    response = client.list_users()
    res = [user["UserName"] for user in response["Users"]]
    return res
