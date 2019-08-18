# UI autotests for nps server

### Install 
For correct tests exercution you need to have `python` v. 3.6+. For install requirements run

`pip3 install -r requirements.txt`

### Run
Command to run tests:

`$ py.test -s -v --driver=Chrome --html=report/index.html tests/`

Only Chrome and Firefor browsers are supported.

### Report
Report `index.html` will be in `report` folder.
