
from email_creds import get_zip_email_creds
import boto3
from moto import mock_aws
import json

# This decorator will replace any call to boto3 with an equivalent call to moto's mock API
@mock_aws
def test_get_zip_email_creds():
    # The moto "account" is empty, so we have to put the secret in it
    client = boto3.client('secretsmanager')
    # secrets are stored as JSON strings, so we need to convert our dictionary to a string
    secret_string = json.dumps({'email': 'test@gmail.com', 'password': 'password'})
    client.create_secret(Name='regulations_data_gmail', SecretString=secret_string)

    # the mocked out secretsmanager is now ready.  We can call the function we
    # want to test.
    creds = get_zip_email_creds()

    # Since the function accesses the regulations_data_gmail secret, we expect to get
    # the email and password we saved earlier
    assert creds['email'] == 'test@gmail.com'
    assert creds['password'] == 'password'
