## **Full Stack Automation Final Project**
[Short Video - Demonstration](https://...)
### **_This project created to demonstrate my knowledge and skills in Automation Testing._**
***
### _About_
The project demonstates a smart automation infrastructure. It is built in hierarchy order of modules. The modules contain number of classes with methods.
There are page object moduls, Conftest for initialization, common opperations, actions, extensions, flows and test moduls.
In this way, the tests can be created in very simple way with a minimum lines of code, and it can be easy maintained.
Also the infrastructure allows to work with differend kinds of applications easly.
Test cases running with Pytest.

### _Project Overview_

The project is an example of infrastructure for automation testing of different kinds of applications:
* Web based application
* Mobile application
* Rest API
* Electron application
* Desktop application

### **_Infrastructure project includes using of:_**
* Page Object Design Pattern
* Project Layers(Extensions/Work Flows/Test Cases...)
* Conftest - Initialization Modul
* Pytest - testing framework for Python
* Support of Different Clients/Browsers
* Failure Mechanism
* Common Functionality
* External Files Support
* Reporting System (including screenshots)
* Visual Testing
* DB support
* CI support  

***

### _List of applications were used in this project:_
* [Atid.store](https://atid.store/) webpage - Web based application
* Mortgage calculator - Mobile application
* Grafana API - Web API
* TodoList -Electron application
* Windows calculator - Desktop application

### _Tools & Frameworks used in the project:_
* Pytest - Testing Framework
* Listeners - interface used to generate logs and manage error handling
* MySQL Free Online DB - used for login to Grafana web page
* [Jenkins](https://www.jenkins.io/)- for tests execution
* REST Assured - for API testing
* [Allure](http://allure.qatools.ru/) Reports - as the main reporting system

### Tests Execution:
> Each of the applications has a few tests for demonstration purpose.
These tests can be developed in a very simple way, due to a lot of work with the infrastructure.
[Test_cases](https://github.com/DanArbiv505/test_automation_final_project/tree/master/test_cases)

### _Known Issues:_
Sometimes can be conflicts with some dependencies the applications are using, for example - sharing ports.
Hence, the project is for DEMO purpose only.
