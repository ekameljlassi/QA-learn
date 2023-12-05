import smtplib, ssl
port = 587  # For starttls
smtp_server = "smtp.gmail.com"
sender_email = "email here"
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
    'downtown',
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
    'helio',
    'bardo',
    'lekki',
    'october',
    'ikeja',
    'abuja',
    'tataouine',
    'rabat',
    'festac',
    'mourouj',
    'boumhel',
    'marrakech',
    'sidi maarouf'
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
        'festac' : 'NG',
        'abuja' : 'NG',
    }
    return abbreviations.get(country, ' ')
default_cc = ['<amine@gomycode.co>' , '<yahya@gomycode.co>' , '<oussama.ourahou@gomycode.co>', '<support@gomycode.co>', '<farah.agrebi@gomycode.co>','<lengliz@gomycode.co>']
def get_email_cc_list_physical(region): 
    cc_list = {

    }
    return cc_list.get(region, 'something not right')

def get_email_cc_list_online(region):
    cc_list = {
        'tunisia': default_cc+ ['<khalil.boukadi@gomycode.co>'],
        'beja' : default_cc+ ['<rym.taboubi@gomycode.co>'],
        'manzah' : default_cc+ ['<imed.fourati@gomycode.co>'],
        'gabes' : default_cc+ ['<oumayma.gomycode@gmail.co>'],
        'gafsa' : default_cc+ ['<hamza.farhat@gomycode.co>'],
        'nabeul' : default_cc+ ['<mohamed.rejeb@gomycode.co>'],
        'sfax' : default_cc+ ['<yesmine.guermazi@gomycode.co>'],
        'sousse' : default_cc+ ['<safa.kasmi@gomycode.co>'],
        'downtown' : default_cc+ ['<walaa.hendaoui@gomycode.co>'],
        'lac' : default_cc+ ['<saifeddine@gomycode.co>'],
        'tataouine' :  default_cc+ ['<marwa.bguir@gomycode.co>'],
        'boumhel' :  default_cc+ ['<aymen.benhadj@gomycode.co>'],
        'mourouj' :  default_cc+ ['<amira.chihi@gomycode.co>'],
        'bardo' :  default_cc+ ['<oussema.elmetoui@gomycode.co>'],
        'ghazela' :  default_cc+ ['<hamza.farhat@gomycode.co>'],
        'ivory': default_cc+ ['<assohounhonorejeanmichel.soumayin@gomycode.co>'],
        'abidjan' : default_cc+ ['<motibieandrea.bah@gomycode.co>'],
        'zone4' : default_cc+ ['<assohounhonorejeanmichel.soumayin@gomycode.co>'],
        'egypt': default_cc+ ['<abddelrahman.elsayed@gomycode.co>'],   
        'dokki' : default_cc+ ['<abddelrahman.elsayed@gomycode.co>'],
        'cairo' : default_cc+ ['<asma.ahmed@gomycode.co>'],
        'october' : default_cc+ ['<haneen.gasser@gomycode.co>'],
        'helio' : default_cc+ ['<nourhan.ali@gomycode.co>'],
        'senegal' : default_cc+ ['<alainnandy.coly@gomycode.co>'],
        'dakar' : default_cc+ ['<mariekhane.bob@gomycode.co>'],
        'yoff' : default_cc+ ['<papaahmet.diop@gomycode.co>'],
        'morocco': default_cc+ ['<ghita.elidrissi@gomycode.co>'],
        'casa' : default_cc+ ['<ayoub.chakir@gomycode.co>'],
        'marrakech': default_cc+ ['<nassima.idbihi@gomycode.co>'],
        'sidi maarouf': default_cc+ ['<yousra.nadi@gomycode.co>'],
        'tanger': default_cc+ ['<yasmine.zerhouni@gomycode.co>'],
        'rabat': default_cc+ ['<abdellatif.tijani@gomycode.co>'],
        'nigeria' : default_cc+ ['<sobowale.funmilayo.deborah@gomycode.co>'],
        'lagos' : default_cc+ ['<temitayo.akinwale@gomycode.co>'],
        'lekki' : default_cc+ ['<clive.akporube@gomycode.co>'],
        'ikeja' : default_cc+ ['<dele.fayemi@gomycode.co>'],
        'festac' : default_cc+ ['<spencer.nweke@gomycode.co>'],
        'abuja' : default_cc+ ['<victory.ndueso@gomycode.co>'],
        }
    return cc_list.get(region, ['something not right'])

# get input from user
answers_str = input('Audit result :')
answers = [answer.strip() for answer in answers_str.split('\t') if answer.strip()]
print('answers are',answers)
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

# ask if hackerspace is online or physical
hackerspace_type = input("Is the hackerspace online or physical? ")

# check if the hackerspace is online
if hackerspace_type.lower() == 'online':
    # add the camera question
    if answers[0] == 'Yes, Camera was on but not during the whole session':
        message += '<li>Your camera was on but not during the whole session.</li>'
    elif answers[0] == 'No, Camera was not on':
        message += '<li>Your camera was not on during the session.</li>'
    # shift the index of the answers for the remaining questions
    answers = answers[1:]

# add the remaining questions
if answers[0] == 'Almost but missed a few points':
    message += '<li>You had Standup with students but missed a few points.</li>'
elif answers[0] == 'No, they did not':
    message += '<li>You did not have Standup with students.</li>'
else:
    print("answer is nto identfied")
if answers[1] == 'He covered most of the SuperSkill':
    message += '<li>You partially covered a SuperSkill.</li>'
elif answers[1] == 'He did not cover any SuperSkill':
    message += '<li>You did not cover any SuperSkill.</li>'
else:
    print("answer for superskill is not indetified")

if answers[2] == 'Approachable and responsive, but not consistently':
    message += '<li>You are approachable and responsive, but not consistently.</li>'
elif answers[2] == 'Not approachable and rarely responds to inquiries':
    message += '<li>You rarely responds to inquiries.</li>'
else:
    print("answer for instructor responsive and approcachable is not identified")

if answers[3] == 'Yes, but briefly':
    message += '<li>You had workshops with the students but briefly.</li>'
elif answers[3] == 'No, there were no workshops':
    message += '<li>You did not have workshops with the students.</li>'
else:
    print('answer for workshop is not indentified')

if answers[4] == 'Explanations are somewhat clear but can be improved':
    message += '<li>Your explanations are somewhat clear but can be improved.</li>'
elif answers[4] == 'Explanations are often unclear and difficult to follow':
    message += '<li>Ypur explanations are often unclear and difficult to follow.</li>'

if answers[5] == 'Classroom time is somewhat well managed, but there are areas for improvement':
    message += '<li>Classroom time is somewhat well managed, but there are areas for improvement.</li>'
elif answers[5] == 'Classroom time is poorly managed with no attention to icebreakers and punctuality':
    message += '<li>Classroom time is poorly managed with no attention to icebreakers and punctuality.</li>'

if answers[6] == 'OTO/Checkpoint sessions partially checked':
    message += '<li>you partially checked OTO/Checkpoint.</li>'
elif answers[6] == 'No OTO/Checkpoint verified':
    message += '<li>You did not check OTO/Checkpoint for the students.</li>'

if answers[7] == 'Briefly had Recaps and Objectives':
    message += '<li>You briefly had Recaps and Objectives for the next session.</li>'
elif answers[7] == 'Didn’t had Recaps and Objectives':
    message += '<li>You didn’t have Recaps and Objectives for the next session.</li>'

if answers[8] == 'Yes, but briefly':
    message += '<li>Real-world examples and practical exercises were included in the session but briefly.</li>'
elif answers[8] == 'No, they did not include anyone':
    message += '<li>No real-world examples and practical exercises were included in the session.</li>'
else:
    print('answer for real world example is indefined')


# create email
HS = get_country_abbreviation(hackerspace)
email_list = get_email_cc_list_online(hackerspace)
object = f'Physical Learning Experience QA - {HS} - {instructorName}'
objectPhysical = f'Physical Learning Experience QA - {HS} - {instructorName}'
warningObject = f'WARNING - Physical Learning Experience QA - {HS} - {instructorName}'

simple1 = f"""Hello {instructorName}, <br> <br> I am sending you this email following the deep-dive done on your session that occurred on {date}. Overall the session went really well and you are applying all the processes and expected session flow. Congratulations on that. Very much appreciated. <br> <br> <b style="color:#38761D"> Compliance score :  {score}% </b> <br> <br> Best Regards,"""
simple2 = f"""Hello {instructorName}, <br> <br> We would like to congratulate you for the hard work you have shown during your last training session. Following a deep dive into your session that took place on {date} and it was overall good. You’ll find below the comments or issues we bring your attention to:<br> <ul>{message}</ul> <br> <b style="color:#38761D;"> Compliance score :  {score}% </b> <br> <br> We hope to see these changes incorporated in your next sessions. Thank you and keep up the good work ! <br> <br> Best Regards,"""
simple3 = f"""Hello {instructorName}, <br> <br> I am sending you this email following the deep-dive done on your session that occurred on {date}. We have noticed as shown in the remarks below that you are not providing an  acceptable experience to our students and that the compliance score is low. <br> <br> <ul>{message}</ul> <br> <b style="color:#E69138;"> Compliance score :  {score}%</b> <br> <br> Your HSM and Country Manager will reach out to you for a full review and remarks on how to run a proper session. <br> <br> Best Regards,"""
simple4 = f"""Hello {instructorName}, <br> <br> I am sending you this email following the deep-dive done on your session that occurred on {date}. We have noticed as shown in the remarks below that you are not providing an  acceptable experience to our students and that the compliance score is low.<br> <br> <ul>{message}</ul> <br> <br> The session overall was not within our criterias and it is not considered as a valid session for the students <br> <br> <b style="color:#CC0000;"> Compliance score :  {score}% </b> <br> <br> Your HSM and Country Manager will reach out to you for a full review and remarks on how to run a proper session. <br> <br> Best Regards,"""

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
elif 55 < int(score) <= 75:
    subject = object.encode('utf-8').decode('utf-8')
    body = f"""\
{simple3}
{signature_html}"""
elif int(score) <= 55:
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