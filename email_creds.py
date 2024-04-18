import boto3
import json

def get_zip_email_creds():
    """
    Get the email and password for the ZIP email account from AWS Secrets Manager
    :return: a dictionary with they keys email and password
    """
    client = boto3.client('secretsmanager')
    secret_id = 'regulations_data_gmail'
    value = client.get_secret_value(SecretId=secret_id)

    return json.loads(value['SecretString'])
