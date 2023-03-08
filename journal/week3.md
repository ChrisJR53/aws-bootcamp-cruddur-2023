# Week 3 — Decentralized Authentication
## Required Homework
### Setup Cognito User Pool
Firstly I created a User Pool on AWS Cognito:

![Cognito User Pool]()

I then added the aws-amplify dependency to ```package.json```:

![Amplify Package]()

I then added the required lines of code to configure aws-amplify to the ```App.js``` file:

![Amplify Config]()

I then added the relevent env-vars to ```docker-compose.yml```:

![Env Vars]()

In ```HomeFeedPage.js``` I imported "Auth" from the "aws-amplify" library:

![Amplify Import]()

Then I added the code lines to check authentication to the same ```HomeFeedPage.js``` file:

![Amplify Authentication]()

In ```ProfileInfo.js``` I added the code for handling sign out:

![Amplify ProfileInfo]()

In ```SigninPage.js``` I added the code to handle the creation of authentication tokens:

![Amplify Signin]()

I then followed the modification of the provided code as per instructed in the weekly video:

![Amplify Signup Modify]()

The error handling for wrong username or password was successful:

![App Error Proof]()

The Cruddur app threw the error below, which was later determined to be the lack of "name" and "preferred_username" being set as required attributes in my Cognito User Pool:

![App Signin Attempt]()

### Implement Custom Signup Page
Firstly I went back and recreated my Cognito User Pool to include the name and preferred_username fields as a requirement on user creation:

![User_Requirements]()

I replaced the old User Pool ID and Client ID details in ```docker-compose.yml```:

![Docker Compose Details]()

I added the required lines of code to my ```SigninPage.js``` file:

![SigninPage Code]()

### Implement Custom Confirmation Page
Right after adding the SigninPage code, I added the required lines of code for my ```ConfirmationPage.js``` file:

![ConfirmationPage Code]()

I added a new user through the Cruddur webpage:

![New User]()

As a **bouns** objective I tested out the "Resend Activation Code" button on the email confirmation page:

![Resend Code]()

Before activating the user on Cruddur, I checked that the user had been created in Cognito and was yet to be verified:

![Cognito_Unverified]()

After activating the user with my email activation code, the user was displayed as verified on Cognito:

![Cognito Verified]()

Finally, I got into the Cruddur homepage successfully logged in as my Cognito user:

![Login Proof]()

### Implement Custom Recovery Page
I added the required lines of code to my ```RecoveryPage.js``` file:

![RecoveryPage Code]()

I confirmed the recovery feature to reset my password was working correctly:

![Recovery Success]()

## Homework Challenges
- Test "Resend Activation Code" button
- Make the password reset success text look better
