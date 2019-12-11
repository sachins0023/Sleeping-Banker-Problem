# Sleeping-Banker-Problem
Hiring Problem

Problem Statement.

Your manager wants you to keep an eye on invalid/expired session(s) of a user from the multiple(i.e. concurrent) logins of that user. As a part of this, you will have to inform a user of the invalid session by asking them to log out and log in again. Additionally, the manager wants to have insights on all the sessions of that user, till date, including the current active session.

For this, you are given two fields in a form  to create a user (mobile number, user name). You have to capture all the possible data points such as user-agent, ip address..etc. Whenever a user is created in your database, you need to create a session_key. This submission leads to the next page where you can see all the details of a user(see JSON response below).

When a user tries to login from another(a second) device with the same access details, they are to be shown the same like above, but other windows sessions should be closed saying that "there is already session up and running, please logout and login again"

API method:POST,name:createUser,params:mobile,username


You need to create another API to fetch the details of user base on his mobile number

API method:GET,name:doGetUser,params:mobile

{"mobile_number":9912345678,user_name:"finin",activSession:1C5CHFA_enIN875IN875,sessions:[{session:"bhsolFhytbhGyskj7"},{session:"nJHJKgdsjUgskjfkhdjh78"}]}

Superuser Credentials:
username: admin
password: password