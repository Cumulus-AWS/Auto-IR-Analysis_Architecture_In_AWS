import requests
import json

#대상이 Ec2가 아니라 포렌식은 작동하지않지만, 위험도는 충분히 높음
def lambda_handler(event, context):
    url = "https://discord.com/api/webhooks/1181582241265107074/hURSQ-Q-SN27CB-whxYkjS-qDBY0PuF8zWIELtlJMEi1xOwnL8pVqJOM1OcI830O7TVP"

    data = {
    "avatar_url": "https://i.ibb.co/pjyz7qF/angr-Y-cumulus.png",
    "username" : "Cumulus AWS Guard-Duty",
    }
    
    FindingID = event["detail"]["id"]

    data["embeds"] = [
        {
            "title": "**high-level severity has been detected.**",
            "description": (
                "\n\n"
                "* Type : " + event["detail"]["type"] + "\n\n"
                "* Title : " + event["detail"]["title"] + "\n\n"
                "* Severity : " + str(event["detail"]["severity"]) + "\n\n"
                "* Description : " + event["detail"]["description"] + "\n\n"
                f"* Link : [AWS GuardDuty](https://ap-northeast-2.console.aws.amazon.com/guardduty/home?region=ap-northeast-2#/findings?macros=current&fId={FindingID})"
            )
        }
    ]

    result = requests.post(url, json=data)
    
    try:
        result.raise_for_status()
    except requests.exceptions.HTTPError as err:
        return {
        'statusCode': 400,
        }
    else:
        return {
        'statusCode': 200,
        'body': json.dumps("Payload delivered successfully, code {}.".format(result.status_code))
        }

