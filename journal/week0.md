# Week 0 — Billing and Architecture

## Video Content
The following is a list of videos watched this week, which relate to thte course:

- [Free AWS Cloud Project Bootcamp - Week 0 - Billing and Architecture](https://www.youtube.com/live/SG8blanhAOg?feature=share)
- [AWS Bootcamp Week 0 - Pricing Basics and Free tier](https://youtu.be/OVw3RrlP-sI)
- [AWS Organizations & AWS IAM Tutorial For Beginners - Cloud BootCamp - Week 0](https://youtu.be/4EMWBYVggQI)

## Core Homework
### Conceptual Diagram
A conceptual diagram was drawn on a physical napkin:

![napkin_diagram](https://user-images.githubusercontent.com/123467130/221172724-bc67db5f-9f8a-4cbd-b11b-3a57327d1733.jpg)

The same diagram was completed in Lucidchart:

![conceptual_diagram](https://user-images.githubusercontent.com/123467130/221167183-aeb585b5-1f05-43ec-abe7-aedec49c1d7e.PNG)

[LucidChart Share link](https://lucid.app/lucidchart/9d2e7257-4c90-4638-8aaf-88cf8d6e62a0/edit?viewport_loc=-181%2C-191%2C1899%2C1068%2C0_0&invitationId=inv_0cd2d628-69be-459c-81b5-291e4fed2536)

### Logical Architectual Diagram
A logical architectural diagram was completed in Lucidchart:

![logical_diagram](https://user-images.githubusercontent.com/123467130/221167618-d8a1615a-e043-44d1-9631-ef4a2189dd97.PNG)

[LucidChart Share link](https://lucid.app/lucidchart/ce886dde-65da-4508-86e5-d5f3a6a92d5a/edit?viewport_loc=-141%2C149%2C1899%2C1068%2C0_0&invitationId=inv_5b8d2177-4cd4-474c-9ab4-43621db971b2)

### IAM Admin User
The admin user aws-bootcamp-admin was created with AWS managed policies AdministratorAccess and IAMUserChangePassword:

![admin_user](/journal/resources/images/week0/admin_account.png)

### AWS CloudShell
CloudShell was briefly used to test out its capabilities:

![cloudshell_use](https://user-images.githubusercontent.com/123467130/221171758-433e3771-4d0c-4fdb-af6a-0e3652b78245.png)

### AWS Credentials
An IAM access key and secret key were created to allow programmatic access to AWS CLI from the admin account:

![cli_credentials](/journal/resources/images/week0/cli_credentials.png)

### AWS CLI
AWS CLI was installed on the Gitpod workspace for this project:

![aws_cli](https://user-images.githubusercontent.com/123467130/221176260-5ee376b2-4920-4ec7-8fcd-d6d7acb9de70.PNG)

### Billing Alarm
A billing alarm was created to alert me once my monthly spend has exceeded 15 USD:

![billing_alarm](/journal/resources/images/week0/billing_alarm.PNG)

### Budget
A budget was created with varying thresholds in order to warm me if my likely spend would exceed 15 USD for a given month (Exceeded here due to my one-off 13 USD spend on domain):

![aws_budget](/journal/resources/images/week0/aws_budget.PNG)

## Homework Challenges
### Destroy your root account credentials, Set MFA, IAM role
A random password was created using LastPass, which was set for the root account and then not recorded anywhere (Password generated below is only an example):

![random_password](https://user-images.githubusercontent.com/123467130/221187387-fd255f4f-c37e-4d9e-86fa-6b3f55d1e7a8.PNG)

[Password Generator Link](https://www.lastpass.com/features/password-generator#generatorTool)

The Google Authenticator app was used to add MFA to the admin account (root account previously had MFA):

![admin_mfa](/journal/resources/images/week0/admin_mfa.PNG)

An IAM role allowing an EC2 instance to assume full access to S3 buckets was then created:

![iam_role](https://user-images.githubusercontent.com/123467130/221188461-ab5da4a0-8848-4095-b488-d35cd1886b3e.PNG)

### Use EventBridge to hook up Health Dashboard to SNS
An EventBridge rule was created to sent an alert to my personal email address whenever there was an event occuring in AWS Health Dashboard:

![eventbridge_alert](/journal/resources/images/week0/eventbridge_alert.PNG)

### Review all the questions of each pillars in the Well Architected Tool
All questions in the AWS Well-Architected Framework tool were reviewed:

![well_architected_questions](/journal/resources/images/week0/well_architected_questions.PNG)
