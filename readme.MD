# Send Work Logs Module:
This is a python script made to send work logs to someone without having to open the email tab and type every time.

It uses zoho server for emailing right now. To use it with gmail change the smtp server address to that of google. and get app password from google account.

## Steps to setup:

* Install the modules in requirements.txt
* Edit the config.py to include your details, for ZOHO KEY follow the following
    - goto [your zoho account page](accounts.zoho.com) to get your app password It is in `Security` > `App Password` / `Application Specific password`
    - click `Generate New App Password` then type a name and generate.
    - copy that key to replace MY_ZOHO_KEY in config.py
* After everything is finished you can run the send_mail.py
* if you are sending for the first time use `"Work Log: "+name` as subject, otherwise use `"Re: Work Log: "+name` to send mail to the same thread.
## Instruction to Use the module:

* run the send_mail.py
* if you have saved worklog from the same day it'll ask to use that.
* if you answered n(no) to the above or do not have history it'll ask you to enter the tasks.
* Enter each tasks.
    - press enter after entering somthing to enter point.
    - press enter in blank line to exit entering given task.
    - enter 're' and press enter to delete the previous point.
* If it's not loaded from history it'll ask for conformation to send the email. enter [y] or just enter to send.

## Instructions to edit/enhance:

* You can edit the template html to your liking. 
* You can also edit anything else to have the interference better.
* getting your key from environment will provide extra layer of security.

## Instruction for contribution:
* If you have any problem during its execution, make a issue in the github.
* If you have edited the module and want to contribute, fork the repository, edit it and send me the pull request.