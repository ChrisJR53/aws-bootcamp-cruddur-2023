# Week 3 — Decentralized Authentication
## Required Homework
### Weekly Videos
All videos in todo list watched.

### Setup Cognito User Pool
Firstly I created a User Pool on AWS Cognito:

![Cognito User Pool](/journal/resources/images/week3/01_cognito_userpool.PNG)

I then added the aws-amplify dependency to ```package.json```:

![Amplify Package](/journal/resources/images/week3/02_cognito_npm_i_package.PNG)

I then added the required lines of code to configure aws-amplify to the ```App.js``` file:

![Amplify Config](/journal/resources/images/week3/03_cognito_import.PNG)

I then added the relevent env-vars to ```docker-compose.yml```:

![Env Vars](/journal/resources/images/week3/04_cognito_docker_update.PNG)

In ```HomeFeedPage.js``` I imported "Auth" from the "aws-amplify" library:

![Amplify Import](/journal/resources/images/week3/05_amplify_import.PNG)

Then I added the code lines to check authentication to the same ```HomeFeedPage.js``` file:

![Amplify Authentication](/journal/resources/images/week3/06_amplify_auth.PNG)

In ```ProfileInfo.js``` I added the code for handling sign out:

![Amplify ProfileInfo](/journal/resources/images/week3/07_amplify_profileinfo.PNG)

In ```SigninPage.js``` I added the code to handle the creation of authentication tokens:

![Amplify Signin](/journal/resources/images/week3/08_amplify_signin.PNG)

I then followed the modification of the provided code as per instructed in the weekly video:

![Amplify Signup Modify](/journal/resources/images/week3/09_amplify_signup_modify.PNG)

The error handling for wrong username or password was successful:

![App Error Proof](/journal/resources/images/week3/10_app_error_proof.PNG)

The Cruddur app threw the error below, which was later determined to be the lack of "name" and "preferred_username" being set as required attributes in my Cognito User Pool:

![App Signin Attempt](/journal/resources/images/week3/11_app_signin_attempt.PNG)

### Implement Custom Signup Page
Firstly I went back and recreated my Cognito User Pool to include the name and preferred_username fields as a requirement on user creation:

![User_Requirements](/journal/resources/images/week3/12_signup_remake_user_pool.PNG)

I replaced the old User Pool ID and Client ID details in ```docker-compose.yml```:

![Docker Compose Details](/journal/resources/images/week3/13_signup_pool_details.PNG)

I added the required lines of code to my ```SignupPage.js``` file:

![SignupPage Code](/journal/resources/images/week3/14_signup_page_code.PNG)

### Implement Custom Confirmation Page
Right after adding the SignupPage code, I added the required lines of code for my ```ConfirmationPage.js``` file:

![ConfirmationPage Code](/journal/resources/images/week3/15_confirmation_page_code.PNG)

I successfully added a new user through the Cruddur webpage, which sent me an email confirmation code, and then took me to the confirmation page:

![New User](/journal/resources/images/week3/16_resend_email_test.png)

After activating the user with my email activation code, the user was displayed as verified on Cognito:

![Cognito Verified](/journal/resources/images/week3/18_user_in_pool.PNG)

Finally, I got into the Cruddur homepage successfully logged in as my Cognito user with my full name and handle visible:

![Login Proof](/journal/resources/images/week3/19_login_success.PNG)

### Implement Custom Recovery Page
I added the required lines of code to my ```RecoveryPage.js``` file:

![RecoveryPage Code](/journal/resources/images/week3/20_recovery_page_code.PNG)

I tested the "I Forgot my Password" option on the Cruddur app and confirmed it sent me a new verification code, and I was able to reset my password:

![Recovery Code](/journal/resources/images/week3/21_reset_password_code.png)

I confirmed the recovery feature to reset my password was working correctly on the app:

![Recovery Success](/journal/resources/images/week3/22_password_recovery_success.PNG)

## Homework Challenges
### Test "Resend Activation Code" button
As a **bouns** objective I tested out the "Resend Activation Code" button on the email confirmation page, this worked but only after adding my email into the "Email" input box:

![Resend Code](/journal/resources/images/week3/16_resend_email_test.png)

I confirmed I was indeed emailed a second verification code:

![Email Code](/journal/resources/images/week3/17_confirmation_codes.png)



- Make the password reset success text look better
