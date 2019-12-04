import os
import json
MAIL_TO_ME=True
DEBUGGING_MODE=False

name='Your Name'
email="your.mail@eydean.com"
ZOHO_KEY=os.getenv('MY_ZOHO_KEY')

mail_to_final='person.to.send@eydean.com' 
cc_to_final=None
mail_to_debug='your.debugging.mail@gmail.com'

mail_to=mail_to_debug if MAIL_TO_ME else mail_to_final
cc_final= None if MAIL_TO_ME else cc_to_final


json_path="worklog.json"
if not os.path.isfile(json_path):
    name=[{'name':name}]
    with open(json_path) as r:
        json.dump(name,r)
