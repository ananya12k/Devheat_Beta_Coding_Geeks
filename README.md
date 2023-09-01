# Devheat_Beta_coding_geeks
Repository for Devheat Beta hackathon</br>
</br>
## Application Name:-</br>
My SOS app</br></br>
## Team Members:-</br>
1. Ananya Kulkarni
2. Devansh Makwana
3. Khushi Shah

## Techs used:-</br>
1. We have used programming language <b>Python</b> for making this app. We have used <b>Kivymd library</b> for this purpose.</br>
2. We also made <b>authentication</b> system for the user who wants to use the application </br>
3. We have used <b>twilio</b> lib to enable our functionality of sending <b>sms alert</b> to friends</br>
4. We have used <b>MongoDB</b> as database(pymongo in python) so that user can store list of friends</br>


## Future goals:-</br>
1. We also look forward to add certain new features like we are planning to add GPS location provider which will provide location along with  alert message whenever the user is in danger to the members in friend list.</br>
2. We also look forward to send voice messages in sms</br>
3. We also excited to find a way to include motion sensor in our app which'll trigger the alert button automatically and send "HELP ME" messages to the members in the friends list.</br>
By this feature there'll be no need of opening our phone then app to send alert messages, only a particular motion will do the job</br></br>

## Summary of our application-</br>
In this application, we provide users, features like sign up, sign in, login using password, also they will be able to make a friend’s list  who will be alerted when the user is in danger through message. If a user forgets his/her password of login id he/she will be easily able to change password. Also, if a user wants to delete friend’s list he/she can easily do it .  An OTP will be sent to  user’s mobile number for security reasons to change ones login password . When user is in danger he/she is just required to click a button to alert their friends and family members. It will send an alert message to the members in friends list. It will also allow user to edit alert message . If a user is no longer using the app he/she can easily delete his/her profile.  </br>

## Procedure to create an account:-</br>
1.	First user needs to create account by entering username, e-mail id, phone number and by creating a password:</br>
	![image](https://user-images.githubusercontent.com/107758523/175778591-c3c005c2-edc9-49c2-8604-088c9c0d256a.png)</br>
2.	Now the user needs to login</br>
![image](https://user-images.githubusercontent.com/107758523/175778769-fbbb9b8e-7ae7-4140-b7e9-d7b6607556da.png)</br>
3.	Now go to Add Friends from Friends in the  Menu</br>
![image](https://user-images.githubusercontent.com/107758523/175778676-a90f4431-e695-475f-9d92-82bdacbd282f.png)</br>
![image](https://user-images.githubusercontent.com/107758523/175778705-03403ca6-e42c-4a9b-9e3c-0c6e52f26f39.png)</br>
![image](https://user-images.githubusercontent.com/107758523/175778723-1e6be60d-8397-46e3-951f-001d7063b755.png)</br>
Enter the details and now click on save to save the details.</br>
And now you are good to go.</br></br></br>


## Procedure to send an alert message to member of friends list:-</br>
1.	First you need to login to the app, if you are already a member:</br>
![image](https://user-images.githubusercontent.com/107758523/175778769-fbbb9b8e-7ae7-4140-b7e9-d7b6607556da.png)</br>
2.	Then you need to go to menu and then click on friends.</br>
![image](https://user-images.githubusercontent.com/107758523/175778787-ae0d52ab-f0bc-4748-840d-0da1daf26de5.png)</br>
3.	Then click on View Friends to check whether the friends have been added properly or not.<br> Now,we can go to edit message and user needs to type the alert message that he/she wants to send to the friend .And then click on save to send the message.</br>
![image](https://user-images.githubusercontent.com/107758523/175778821-da5dbb21-0ab9-4289-84c0-5767df64d3aa.png)</br></br></br>

## Procedure to delete a friend from friends list:-</br>
1.	Go to menu and click on Delete friends. Then enter the mobile number and name of friend you want to delete from friends list.</br>
2.	Then click on delete. Now the friend must have been deleted from friends list.</br>
We can check it in View Friends list</br>
![image](https://user-images.githubusercontent.com/107758523/175778869-bf126c5a-36b2-41f4-b2cf-4ec13f6383dd.png)</br></br></br>

## Procedure to create new password:-</br>
1.	First user needs to click on forgot password: </br>
![image](https://user-images.githubusercontent.com/107758523/175778906-bbc65aec-02bd-4928-acc5-22c369fb469a.png)</br>
2.	Then user needs to enter mobile number and an OTP, sent on the entered mobile number.</br>
![image](https://user-images.githubusercontent.com/107758523/175778925-2c1bf6f3-6de1-439a-a508-527edb354eb0.png)</br>
3.	Then in Reset Password, user needs to enter the new password.And click on Set Password to set the new password.</br>
![image](https://user-images.githubusercontent.com/107758523/175778948-a50a12bd-200a-4747-90fc-7b63f52b74e8.png)</br>

## Small demonstration of our application:-</br>
  https://drive.google.com/file/d/1KjvHnlc4KPMhGFXPZF67Gp3nsRMi0Yn1/view?usp=drivesdk

 ## To run project on your system:
 1. Install dependencies
 ```bash
pip install pymongo kivy kivymd python-dotenv sms
```
 2. Create a MongoDB Atlas Account and create a cluster.
 3. Create .env file in project directory and create variable serverLink = "your mongodb server link".
 4. Create Twilio Account and store it's SID and TOKEN in '.env' file.
