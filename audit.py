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
default_cc = 'Amine Bouhlel <amine@gomycode.co> \n Yahya Bouhlel <yahya@gomycode.co> \n Oussama Ourahou <oussama.ourahou@gomycode.co> \n GOMYCODE SUPPORT <support@gomycode.co> \n Farah Agrebi <farah.agrebi@gomycode.co> \n Sirine lengliz <lengliz@gomycode.co>'
def get_email_cc_list_physical(region): 
    cc_list = {

    }
    return cc_list.get(region, 'something not right')
def get_email_cc_list_online(region):
    cc_list = {
        'tunisia': f'{default_cc}\n <khalil.boukadi@gomycode.co> ',
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
    return cc_list.get(region, 'something not right')

# get input from user
answers_str = input('Audit result :')
answers = answers_str.split('\t')
message = ''
hackerspace = input('hackerspace :')
date = input('date :')
score = input('score :')

instructorName = input('instructor :')
# check each question and add message for "No" answers
if answers[0].lower() == 'no':
    message += 'You did not complete the session. \n'

if answers[1].lower() == 'no':
    message += 'You did not have Standup with students. \n'

if answers[2].lower() == 'no':
    message += 'You were not interactive during the session. \n'

if answers[3].lower() == 'no':
    message += 'You did not have workshop with the students \n'

if answers[4].lower() == 'no':
    message += 'You did not have a Q&A with the students \n'

if answers[5].lower() == 'no':
    message += 'You did not have OTO/Checkpoint with students. \n'

if answers[6].lower() == 'no':
    
    message += 'You did not have Recap + Objective of next session with students. \n'

if answers[7].lower() == 'no':
    
    message += "You camera was not on. \n"

if answers[8].lower() == 'no':
    message += 'You did not have practice box with the students. \n'

# create email
HS = get_country_abbreviation(hackerspace)
email_list = get_email_cc_list_online(hackerspace)
object = f'Online Learning Experience QA - {HS} - {instructorName}'
objectPhysical = f'Online Learning Experience QA - {HS} - {instructorName}'
warningObject = f'WARNING - Online Learning Experience QA - {HS} - {instructorName}'

simple1 = f'Hello {instructorName}\n \nI am sending you this email following the deep-dive done on your session that occurred on {date}. Overall the session went really well and you are applying all the processes and expected session flow. Congratulations on that. Very much appreciated.  \n\n Compliance score :  {score}% \n\n Best Regards,'
simple2 = f'Hello {instructorName}\n \nWe would like to congratulate you for the hard work you have shown during your last training session. Following a deep dive into your session that took place on {date} and it was overall good. You’ll find below the comments or issues we bring your attention to: {message}.  \n\n \n\n Compliance score :  {score}% \n\n We hope to see these changes incorporated in your next sessions. Thank you and keep up the good work ! \n\n Best Regards,'
simple3 = f'Hello {instructorName}\n \nI am sending you this email following the deep-dive done on your session that occurred on {date}. We have noticed as shown in the remarks below that you are not providing an  acceptable experience to our students and that the compliance score is low.\n \n {message} \n\nYour HSM and Country Manager will reach out to you for a full review and remarks on how to run a proper session. \n\n Compliance score :  {score}% \n\n !Best Regards,'
simple4 = f'Hello {instructorName}\n \nI am sending you this email following the deep-dive done on your session that occurred on {date}. We have noticed as shown in the remarks below that you are not providing an  acceptable experience to our students and that the compliance score is low.\n \n {message} \n\n The session overall was not within our criterias and it is not considered as a valid session for the students \n\n Your HSM and Country Manager will reach out to you for a full review and remarks on how to run a proper session. \n\n Compliance score :  {score}% \n\n !Best Regards,'

# write output to file
with open('output.txt', 'w') as file:
    if int(score) == 100 : 
        file.write(email_list)
        file.write('\n\n')
        file.write(object)
        file.write('\n\n')
        file.write(simple1)
    elif 80 <= int(score) < 100 : 
        file.write(email_list)
        file.write('\n\n')
        file.write(object)
        file.write('\n\n')
        file.write(simple2) 
    elif 50 < int(score) <= 75 : 
        file.write(email_list)
        file.write('\n\n')
        file.write(object)
        file.write('\n\n')
        file.write(simple3)
    elif int(score) <= 50 : 
        file.write(email_list)
        file.write('\n\n')
        file.write(warningObject)
        file.write('\n\n')
        file.write(simple4)