import smtplib, ssl
port = 587  # For starttls
smtp_server = "smtp.gmail.com"
sender_email = "kamel.jlassi@gomycode.co"
password = "MHrecordsofcnotJS.."
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
        'manzah' : 'TN',
        'gabes' : 'TN',
        'gafsa' : 'TN',
        'nabeul' : 'TN',
        'sfax' : 'TN',
        'sousse' : 'TN',
        'cv' : 'TN',
        'lac' :'TN',
        'morocco': 'MA',
        'ivory': 'IC',
        'abidjan' : 'IC',
        'senegal': 'SN',
        'dakar' : 'SN',
        'egypt': 'EG',
        'cairo' : 'EG',
        'dokki' : 'EG',
        'casa' : 'MA',
        'nigeria' : 'NG',
        'lagos' : 'NG',
    }
    return abbreviations.get(country, 'misspelled something maybe')
default_cc = '<kamel.jlassi@gomycode.co>'
def get_email_cc_list_physical(region): 
    cc_list = {

    }
    return cc_list.get(region, 'something not right')

def get_email_cc_list_online(region):
    cc_list = {
        'tunisia': [default_cc, '<kameljs2@gmail.com>'],
        'beja' : f'{default_cc} \n <rym.taboubi@gomycode.co> ',
        'manzah' : f'{default_cc}\n <imed.fourati@gomycode.com>',
        'gabes' : f'{default_cc}\n <imen.issaoui@gomycode.com>',
        'gafsa' : f'{default_cc}\n <hamza.farhat@gomycode.com>',
        'nabeul' : f'{default_cc}\n <Firas.sassi@gomycode.co>',
        'sfax' : f'{default_cc}\n <wafa.trigui@gomycode.co>',
        'cv' : f'{default_cc}\n <walaa.hendaoui@gomycode.com>',
        'lac' : f'{default_cc}\n <safa.gaja@gomycode.co>',
        'abidjan' : f'{default_cc}\n <Ivan.brovou@gomycode.co>',
        'cairo' : f'{default_cc}\n <ibrahem.Desouky@gomycode.co>',
        'dakar' : f'{default_cc}\n <mariekhane.bob@gomycode.co>',
        'dokki' : f'{default_cc}\n <ibrahem.Desouky@gomycode.co>',
        'casa' : f'{default_cc}\n <anasnasrou@gmail.com> \n <imane.houmaid@gomycode.co>',
        'lagos' : f'{default_cc}\n <Temitayogomycode@gmail.com>',
        'sousse' : f'{default_cc} \n <safa.kasmi@gomycode.co>',
        'nigeria' : f'{default_cc} \n <Temitayogomycode@gmail.com> \n <funmigomycode@gmail.com>',
        'morocco': f'{default_cc} \n  <nasrou.anas@gomycode.co> \n <imane.houmaid@gomycode.co>',
        'ivory': f'{default_cc}\n <Ivan.brovou@gomycode.co>',
        'egypt': f'{default_cc} \n  <reham.abdel-sayed@gomycode.co> ',        
        'senegal' : f'{default_cc}\n <nicolas.borrel@gomycode.co> \n  <mariekhane.bob@gomycode.co>',
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
elif 50 <= int(score) < 75:
    subject = object.encode('utf-8').decode('utf-8')
    body = f"""\
{simple3}
{signature_html}"""
elif int(score) <= 50:
    subject = object.encode('utf-8').decode('utf-8')
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