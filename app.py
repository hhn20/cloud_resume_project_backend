import json
import boto3



def lambda_handler(event, context):
    # Increment the count
    try:
        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table('VISIT_COUNT')
        response = table.update_item(
            Key={'id': 1},
            UpdateExpression='ADD visitors :incr',
            ExpressionAttributeValues={':incr': 1},
            ReturnValues='UPDATED_NEW'
        )
        
        # Get the updated counts
        print("hii")
        new_count = response['Attributes']
        
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': new_count
        }
    except Exception as e:
         return {
            'statusCode': 500,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': str(e)
        }
