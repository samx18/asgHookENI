# asgHookENI

A lambda function that gets triggered via a lifecycle hook to attach a secondary elastic network interface to instances that are added to the auto scaling group.


## Setup Steps

* Create lamba funcation - main.py
* Create an SNS topic
* Create a subscription for the topic with the lambda function
* Create a IAM role to allow Auto Scaling access to publish SNS

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Resource": "*",
            "Action": [
                "sqs:SendMessage",
                "sqs:GetQueueUrl",
                "sns:Publish"
            ]
        }
    ]
}

```
* Create a lifecycle hook for the ASG with the following metadata

```
{
  "SubnetId":"subnet-9fb0axxxx",
  "SecurityGroups":"sg-51b8xxxx"
}

```

* Update the lifecycle hook to add the role and the SNS Target and the role

``` 
aws autoscaling put-lifecycle-hook --lifecycle-hook-name eniHook --auto-scaling-group-name demoASG --notification-target-arn arn:aws:sns:us-west-2:123456789123:eni-demo-topic --role-arn arn:aws:iam::123456789123:role/asg-sns

```

