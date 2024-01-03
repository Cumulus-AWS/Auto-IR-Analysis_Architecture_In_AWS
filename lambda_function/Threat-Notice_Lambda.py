import requests
import json

def lambda_handler(event, context):
    # Discord Webhook URL for sending messages
    url = "your-Webhook-URL"

    # Set default avatar and username for the Discord message
    data = {
        "avatar_url": "your-avatar-URL",
        "username": "Cumulus AWS Guard-Duty",
    }
    
    # Extract the FindingID from the AWS CloudWatch event
    FindingID = event["detail"]["id"]

    # Create Discord message payload with embedded content
    data["embeds"] = [
        {
            "title": "**high-level severity has been detected.**",
            "description": (
                "\n\n"
                # Displaying details of the AWS GuardDuty finding
                "* Type : " + event["detail"]["type"] + "\n\n"
                "* Title : " + event["detail"]["title"] + "\n\n"
                "* Severity : " + str(event["detail"]["severity"]) + "\n\n"
                "* Description : " + event["detail"]["description"] + "\n\n"
                # Include a link to the AWS GuardDuty console for more details
                f"* Link : [AWS GuardDuty](https://ap-northeast-2.console.aws.amazon.com/guardduty/home?region=ap-northeast-2#/findings?macros=current&fId={FindingID})"
            )
        }
    ]

    # Send the Discord message using the Webhook URL
    result = requests.post(url, json=data)
    
    try:
        result.raise_for_status()
    except requests.exceptions.HTTPError as err:
        # Handle HTTP error if the message delivery fails
        return {
            'statusCode': 400,
        }
    else:
        # Return a success response if the message is delivered successfully
        return {
            'statusCode': 200,
            'body': json.dumps("Payload delivered successfully, code {}.".format(result.status_code))
        }
