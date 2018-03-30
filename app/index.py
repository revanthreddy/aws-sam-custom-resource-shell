import util.cfnresponse

cfnresponse = util.cfnresponse


def lambda_handler(event, context):
    # TODO implement
    responseValue = 100
    responseData = {}
    responseData['Data'] = responseValue

    if event["RequestType"] == "Delete":
        print("Deleting stack")
        cfnresponse.send(event, context, cfnresponse.SUCCESS, responseData)
    elif event["RequestType"] == "Update":
        print("Updating stack")
        cfnresponse.send(event, context, cfnresponse.SUCCESS, responseData, "CustomResourcePhysicalID")
    if event["RequestType"] == "Create":
        print("Creating stack")
        cfnresponse.send(event, context, cfnresponse.SUCCESS, responseData, "CustomResourcePhysicalID")

    return "Process done"
