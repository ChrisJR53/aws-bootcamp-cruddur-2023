# Week 3 — Decentralized Authentication
## Required Homework
### Implement Custom Signup Page
Firstly I went back and recreated my Cognito User Pool to include the name and preferred_username fields as a requirement on user creation:

![User_requirements]()

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
