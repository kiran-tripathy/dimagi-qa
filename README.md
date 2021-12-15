## Robot Framework
This is a POC of NY USH App workflow. To start:

##### Install Robot Framework and SeleniumLibrary along with its dependencies using pip package manager. 
```
pip install -r requirements.txt
```
##### Replace the webuser credentials in file /Loccators/user_inputs.robot 
```
${email}    sample
${pass}    sample
```

##### The test cases are located in the Tests directory. They can be executed using the robot command:
```
robot Tests
```
