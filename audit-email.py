import smtplib, ssl
port = 587  # For starttls
smtp_server = "smtp.gmail.com"
sender_email = "kamel.jlassi@gomycode.co"
password = "type password here"
receiver_email = input("Instructor email :")
print(receiver_email)

with open('signature.html', 'r') as signature_file:
    signature_html = signature_file.read()

valid_hackerspaces = [
    'tunisia',
    'beja',
    'manzah',
    'gabes',
    'gafsa',
    'nabeul',
    'sfax',
    'sousse',
    'cv',
    'lac',
    'morocco',
    'ivory',
    'abidjan',
    'senegal',
    'dakar',
    'egypt',
    'cairo',
    'dokki',
    'casa',
    'nigeria',
    'lagos',
]

def get_country_abbreviation(country):
    abbreviations = {
        'tunisia': 'TN',
        'beja' : 'TN',
        'menzah' : 'TN',
        'gabes' : 'TN',
        'gafsa' : 'TN',
        'nabeul' : 'TN',
        'sfax' : 'TN',
        'sousse' : 'TN',
        'downtown' : 'TN',
        'lac' :'TN',
        'tataouine' : 'TN',
        'boumhel' : 'TN',
        'mourouj' : 'TN',
        'bardo' : 'TN',
        'ghazela' : 'TN',
        'morocco': 'MA',
        'casa' : 'MA',
        'marrakech' : 'MA',
        'sidi maarouf' : 'MA',
        'tanger' : 'MA',
        'rabat' : 'MA',
        'ivory': 'IC',
        'abidjan' : 'IC',
        'zone4' : 'IC',
        'senegal': 'SN',
        'dakar' : 'SN',
        'yoff' : 'SN',
        'egypt': 'EG',
        'cairo' : 'EG',
        'dokki' : 'EG',
        'october' : 'EG',
        'helio' : 'EG',
        'nigeria' : 'NG',
        'lagos' : 'NG',
        'lekki' : 'NG',
        'ikeja' : 'NG',
        'fastac' : 'NG',
        'abuja' : 'NG',
    }
    return abbreviations.get(country, 'misspelled something maybe')
default_cc = ['<amine@gomycode.co>' , '<yahya@gomycode.co>' , '<oussama.ourahou@gomycode.co>', '<support@gomycode.co>', '<farah.agrebi@gomycode.co>','<lengliz@gomycode.co>']
def get_email_cc_list_physical(region): 
    cc_list = {

    }
    return cc_list.get(region, 'something not right')

def get_email_cc_list_online(region):
    cc_list = {
        'tunisia': default_cc+ ['<khalil.boukadi@gomycode.co>'],
        'beja' : default_cc+ ['<ekamel.jlassi@gmail.com>'],
        'manzah' : default_cc+ ['<ekamel.jlassi@gmail.com>'],
        'gabes' : default_cc+ ['<ekamel.jlassi@gmail.com>'],
        'gafsa' : default_cc+ ['<ekamel.jlassi@gmail.com>'],
        'nabeul' : default_cc+ ['<ekamel.jlassi@gmail.com>'],
        'sfax' : default_cc+ ['<ekamel.jlassi@gmail.com>'],
        'sousse' : default_cc+ ['<ekamel.jlassi@gmail.com>'],
        'downtown' : default_cc+ ['<ekamel.jlassi@gmail.com>'],
        'lac' : default_cc+ ['<ekamel.jlassi@gmail.com>'],
        'tataouine' :  default_cc+ ['<ekamel.jlassi@gmail.com>'],
        'boumhel' :  default_cc+ ['<ekamel.jlassi@gmail.com>'],
        'mourouj' :  default_cc+ ['<ekamel.jlassi@gmail.com>'],
        'bardo' :  default_cc+ ['<ekamel.jlassi@gmail.com>'],
        'ghazela' :  default_cc+ ['<ekamel.jlassi@gmail.com>'],
        'ivory': default_cc+ ['<ekamel.jlassi@gmail.com>'],
        'abidjan' : default_cc+ ['<ekamel.jlassi@gmail.com>'],
        'zone4' : default_cc+ ['<ekamel.jlassi@gmail.com>'],
        'egypt': default_cc+ ['<ekamel.jlassi@gmail.com>'],   
        'dokki' : default_cc+ ['<ekamel.jlassi@gmail.com>'],
        'cairo' : default_cc+ ['<ekamel.jlassi@gmail.com>'],
        'october' : default_cc+ ['<ekamel.jlassi@gmail.com>'],
        'helio' : default_cc+ ['<ekamel.jlassi@gmail.com>'],
        'senegal' : default_cc+ ['<ekamel.jlassi@gmail.com>'],
        'dakar' : default_cc+ ['<ekamel.jlassi@gmail.com>'],
        'yoff' : default_cc+ ['<ekamel.jlassi@gmail.com>'],
        'morocco': default_cc+ ['<ekamel.jlassi@gmail.com>'],
        'casa' : default_cc+ ['<ekamel.jlassi@gmail.com>'],
        'marrakech': default_cc+ ['<ekamel.jlassi@gmail.com>'],
        'sidi maarouf': default_cc+ ['<ekamel.jlassi@gmail.com>'],
        'tanger': default_cc+ ['<ekamel.jlassi@gmail.com>'],
        'rabat': default_cc+ ['<ekamel.jlassi@gmail.com>'],
        'nigeria' : default_cc+ ['<ekamel.jlassi@gmail.com>'],
        'lagos' : default_cc+ ['<ekamel.jlassi@gmail.com>'],
        'lekki' : default_cc+ ['<ekamel.jlassi@gmail.com>'],
        'ikeja' : default_cc+ ['<ekamel.jlassi@gmail.com>'],
        'fastac' : default_cc+ ['<ekamel.jlassi@gmail.com>'],
        'abuja' : default_cc+ ['<ekamel.jlassi@gmail.com>'],
        }
    return cc_list.get(region, ['something not right'])

# get input from user
answers_str = input('Audit result :')
answers = answers_str.split('\t')
message = ''
while True:
    hackerspace = input('hackerspace: ')
    # Check if hackerspace is valid in cc_list
    if hackerspace.lower() in valid_hackerspaces:
        break  # Exit the loop if hackerspace is valid
    else:
        print('Invalid hackerspace. Please enter a valid hackerspace.')
date = input('date :')
score = input('score :')

instructorName = input('instructor :')
# check each question and add message for "No" answers
if answers[0].lower() == 'no':
    message += '<li>You did not complete the session.</li>'

if answers[1].lower() == 'no':
    message += '<li>You did not have Standup with students. </li>'

if answers[2].lower() == 'no':
    message += '<li>You were not interactive during the session. </li>'

if answers[3].lower() == 'no':
    message += '<li>You did not have workshop with the students. </li>'

if answers[4].lower() == 'no':
    message += '<li>You did not have a Q&A with the students. </li>'

if answers[5].lower() == 'no':
    message += '<li>You did not have OTO/Checkpoint with students. </li>'

if answers[6].lower() == 'no':
    
    message += '<li>You did not have Recap + Objective of next session with students. </li>'

if answers[7].lower() == 'no':
    
    message += "<li>You camera was not on. </li>"

if answers[8].lower() == 'no':
    message += '<li>You did not have practice box with the students. </li>'

# create email
HS = get_country_abbreviation(hackerspace)
email_list = get_email_cc_list_online(hackerspace)
object = f'Online Learning Experience QA - {HS} - {instructorName}'
objectPhysical = f'Online Learning Experience QA - {HS} - {instructorName}'
warningObject = f'WARNING - Online Learning Experience QA - {HS} - {instructorName}'

simple1 = f"""Hello {instructorName}, <br> <br> I am sending you this email following the deep-dive done on your session that occurred on {date}. Overall the session went really well and you are applying all the processes and expected session flow. Congratulations on that. Very much appreciated. <br> <br> <b style="color:blue"> Compliance score :  {score}% </b> <br> <br> Best Regards,"""
simple2 = f"""Hello {instructorName}, <br> <br> We would like to congratulate you for the hard work you have shown during your last training session. Following a deep dive into your session that took place on {date} and it was overall good. You’ll find below the comments or issues we bring your attention to:<br> <ul>{message}</ul> <br> <b style="color:red;"> Compliance score :  {score}% </b> <br> <br> We hope to see these changes incorporated in your next sessions. Thank you and keep up the good work ! <br> <br> Best Regards,"""
simple3 = f"""Hello {instructorName}, <br> <br> I am sending you this email following the deep-dive done on your session that occurred on {date}. We have noticed as shown in the remarks below that you are not providing an  acceptable experience to our students and that the compliance score is low. <br> <br> <ul>{message}</ul> <br> <b style="color:red;"> Compliance score :  {score}%</b> <br> <br> Your HSM and Country Manager will reach out to you for a full review and remarks on how to run a proper session. <br> <br> Best Regards,"""
simple4 = f"""Hello {instructorName}, <br> <br> I am sending you this email following the deep-dive done on your session that occurred on {date}. We have noticed as shown in the remarks below that you are not providing an  acceptable experience to our students and that the compliance score is low.<br> <br> <ul>{message}</ul> <br> <br> The session overall was not within our criterias and it is not considered as a valid session for the students <br> <br> <b style="color:red;"> Compliance score :  {score}% </b> <br> <br> Your HSM and Country Manager will reach out to you for a full review and remarks on how to run a proper session. <br> <br> Best Regards,"""

# # write output to file
# with open('output.txt', 'w') as file:
#     if int(score) == 100 : 
#         file.write(email_list)
#         file.write('\n\n')
#         file.write(object)
#         file.write('\n\n')
#         file.write(simple1)
#     elif 80 <= int(score) < 100 : 
#         file.write(email_list)
#         file.write('\n\n')
#         file.write(object)
#         file.write('\n\n')
#         file.write(simple2) 
#     elif 50 < int(score) <= 75 : 
#         file.write(email_list)
#         file.write('\n\n')
#         file.write(object)
#         file.write('\n\n')
#         file.write(simple3)
#     elif int(score) <= 50 : 
#         file.write(email_list)
#         file.write('\n\n')
#         file.write(warningObject)
#         file.write('\n\n')
#         file.write(simple4)

if int(score) == 100:
    subject = object.encode('utf-8').decode('utf-8')
    body = f"""\
{simple1}
{signature_html}"""
elif 80 <= int(score) < 100:
    subject = object.encode('utf-8').decode('utf-8')
    body = f"""\
{simple2}
{signature_html}"""
elif 50 <= int(score) <= 75:
    subject = object.encode('utf-8').decode('utf-8')
    body = f"""\
{simple3}
{signature_html}"""
elif int(score) <= 50:
    subject = warningObject.encode('utf-8').decode('utf-8')
    body = f"""\
{simple4}
{signature_html}"""

cc_s = ["kameljs2@gmail.com", "kamel.jlassi@gomycode.co"]


# Construct the final email content
final_email = f"""\
Content-Type: text/html; charset=utf-8
Subject: {subject}
From : {sender_email}
To : {receiver_email}
CC : {", ".join(email_list)}

{body}"""

final_email = final_email.encode('utf-8')

context = ssl.create_default_context()
with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo()
    server.starttls(context=context)
    server.ehlo()
    server.login(sender_email, password)
    server.sendmail(sender_email, [receiver_email] + email_list , final_email)