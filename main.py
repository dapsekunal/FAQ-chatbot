
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer


chatbot = ChatBot("chatty", storage_adapter='chatterbot.storage.SQLStorageAdapter',
logic_adapters=[
        #"chatterbot.logic.MathematicalEvaluation",
        #"chatterbot.logic.TimeLogicAdapter",
        "chatterbot.logic.BestMatch"
    ]
           )


conversation = [
    "Hello",
    "Hi there!",

    "hi",
    "Hi!",

    "hii",
    "hello!",

    "Hey",
    "Hi",

    "How are you doing?",
    "I'm doing great.",

    "What is your name?",
    "My name is Chatty.",

    "What is your gender?",
    "I am a machine i don't have any gender",

    "Where is cloud counselage located?",
    "Mumbai, Maharashtra",

    "I m not able to access my Bitrix24 account?",
    "Go to https://cloudcounselage24.bitrix24.com/ On the Login page, In the,"
    " ‘Enter the phone number or email’, type in your email id that you have registered with Cloud Counselage "
    "and Click ‘Forgot Password’. In case the problem persists, please write a mail to hrsupport@cloudcounselage.in",

    "I am not able to access my Bitrix account?",
    "Go to https://cloudcounselage24.bitrix24.com/ On the Login page, In the,"
    " ‘Enter the phone number or email’, type in your email id that you have registered with Cloud Counselage "
    "and Click ‘Forgot Password’. In case the problem persists, please write a mail to hrsupport@cloudcounselage.in",

    "I m unable to access my Bitrix24 account?",
    "Go to https://cloudcounselage24.bitrix24.com/ On the Login page, In the,"
    " ‘Enter the phone number or email’, type in your email id that you have registered with Cloud Counselage "
    "and Click ‘Forgot Password’. In case the problem persists, please write a mail to hrsupport@cloudcounselage.in",

    "I am unable to access my Bitrix account?",
    "Go to https://cloudcounselage24.bitrix24.com/ On the Login page, In the,"
    " ‘Enter the phone number or email’, type in your email id that you have registered with Cloud Counselage "
    "and Click ‘Forgot Password’. In case the problem persists, please write a mail to hrsupport@cloudcounselage.in",

    "I m not able to access my bitrix account",
    "Go to https://cloudcounselage24.bitrix24.com/ On the Login page, In the,"
    " ‘Enter the phone number or email’, type in your email id that you have registered with Cloud Counselage "
    "and Click ‘Forgot Password’. In case the problem persists, please write a mail to hrsupport@cloudcounselage.in",

    "I am not able to access my bitrix24 account",
    "Go to https://cloudcounselage24.bitrix24.com/ On the Login page, In the,"
    " ‘Enter the phone number or email’, type in your email id that you have registered with Cloud Counselage "
    "and Click ‘Forgot Password’. In case the problem persists, please write a mail to hrsupport@cloudcounselage.in",

    " What is the job profile? Will we be able to work only in the tech we have chosen for the internship?",
    " Your job profile is 'Technology - Intern'; if you're in cloud computing "
    "technology to update in your LinkedIn or resume, "
    "you can write as 'Cloud Computing - Intern'. Yes, you'll only work in the technology"
    " you're selected for but you can take the training of other technologies.",

    " What is the job profile?",
    " Your job profile is 'Technology - Intern'"
    "Can we choose different technology ?",
    "You'll only work in the technology"
    " you're selected for but you can take the training of other technologies.",

    " How many workgroups should I be in?",
    " Every intern should be a part of 2 workgroups."

    "1. ""202003-IP"" -- This is a general workgroup. Everyone who is"
    " enrolled in IP should be a part of this workgroup."
    "2. ""202003-IP-Technology""  -- This is a technology-specific workgroup."
    " You'll be added to the technology you had enrolled for."
    " For example ""202003-IP-Python"" for students who enrolled for python.",

    " How many workgroups will an intern be a part of?",
    " Every intern should be a part of 2 workgroups."

    "1. ""202003-IP"" -- This is a general workgroup. Everyone who is"
    " enrolled in IP should be a part of this workgroup."
    "2. ""202003-IP-Technology""  -- This is a technology-specific workgroup."
    " You'll be added to the technology you had enrolled for."
    " For example ""202003-IP-Python"" for students who enrolled for python.",

    " How many workgroups should I be a part of?",
    " Every intern should be a part of 2 workgroups."

    "1. ""202003-IP"" -- This is a general workgroup. Everyone who is"
    " enrolled in IP should be a part of this workgroup."
    "2. ""202003-IP-Technology""  -- This is a technology-specific workgroup."
    " You'll be added to the technology you had enrolled for."
    " For example ""202003-IP-Python"" for students who enrolled for python.",


    " Not able to access the LP1 page with my token ",

    "Please watch the videos shared with the invite and you should not face any problems in accessing the training."
    " Please follow the protocol shown in the videos.",

    "Getting error while accessing the page- ""User Not Found""/Website Redirection Issue/Tokens not working.",
    "Please watch the videos shared with the invite and you should not face any problems in accessing the training."
    " Please follow the protocol shown in the videos.",



    "LP2 Quiz doesn't have next question button?",
    "Take a screenshot of the issue and send an email to hrsupport@cloudcounselage.in ",

    "Login issues with training/ for every module of LP1/ LP2, do we have to register again for access to the content?",
    "Yes, you need to register for every module of training. Some of you are facing login issues, "
    "we have kept the training visible without login. Even then, to post a comment and give a quiz"
    " you'll have to login. In case you face difficulty to do so, please try to perform your quiz "
    "or post a comment by using a different browser or incognito mode.",


    " I am applying my 2nd token that is the LP1 then it shows invalid user but the first token was accepted. "
    "What should I do?/ Tokens not working",
    " 1) For each training of LP1/LP2, there are different tokens. Please read the tasks or watch the videos"
    " again meticulously."
    " Try accessing it in incognito mode."
    "2)Please watch the videos shared with the invite and you should not face any problems in accessing the training."
    " Please follow the protocol shown in the videos.",

    "Tokens not working",
    " 1) For each training of LP1/LP2, there are different tokens. Please read the tasks or watch the videos"
    " again meticulously."
    " Try accessing it in incognito mode."
    "2)Please watch the videos shared with the invite and you should not face any problems in accessing the training."
    " Please follow the protocol shown in the videos.",


    " I did follow the instructions given in the video, but still, I'm not able to log in for the LP1 task",
    "Ensure you're using the right token",

    "I'm not able to log in for the LP1 task",
    "Ensure you're using the right token",



    "Do I need to pass with the certificate in training.",
    " No, but please ensure you complete the training.",


    "I am not able to see my tasks.",
    "Please remove the default ""In Progress"" from your filter of the task section and try.",


    " What do we do in the work report?/what we should write in work report?",
    "As mentioned in the video, please write what you have done this week and request approval"
    " from your supervisor by clicking on ""send to supervisor"".",

    "what we should write in work report?",
    "As mentioned in the video, please write what you have done this week and request approval"
    " from your supervisor by clicking on ""send to supervisor"".",

    " I tried it 3-4 times and have to enter token each time I visit it.",
    " We understand that it sometimes becomes tedious to access the training and we highly appreciate your"
    " support in making the training possible. We only do this for security reasons and we're trying to find a way"
    " to minimise the token use. For now, please note that in LP1 there are 3 types tokens:"
    "1. One for each technology, you're a part of."
    "2. The lp1 home page."
    "3. The 6 tokens (one for each step)",


    " I just joined the group and I am not understanding what to do further. How do I start my internship?",
    "Please go through the mail from which you have accepted the invite and check the task section as well.",

    "How do I start my internship?",
    "Please go through the mail from which you have accepted the invite and check the task section as well.",


    "I am unable to access LP1 despite of following the correct procedure",
    " We understand that it sometimes becomes tedious to access the training and we highly appreciate your"
    " support in making the training possible. We only do this for security reasons and we're trying to find a way"
    " to minimise the token use. For now, please note that in LP1 there are 3 types tokens:"
    "1. One for each technology, you're a part of."
    "2. The lp1 home page."
    "3. The 6 tokens (one for each step)",
    " What do I do after completing the quiz? how to complete the entire lp1",

    "There are tokens for each training in the task, if this learning path is done, please wait "
    "for the next learning path "
    "to begin and then please try to finish it. If you are done with LP3 please wait for Live Projects to begin.",


    "Do I need to register every time I do different tasks of lp1?",
    " There are codes in the LP1 assignment, and each time you have to register also,"
    " please check your task description.",


    " I have complete one training, I didn't find any options to continue my training.",
    "Go back to the technology Page. Enter the respective tokens and then work. follow the same process every time.",


    " I am not getting results of the training.",
    "They are just for your practice and not for our record, so you don't need the results of LP1 and LP2 training.",


    " Unable to access/give the quiz",
    " Please retry after some time in an incognito window",

    " Unable to give the quiz",
    " Please retry after some time in an incognito window",

    "I'm Unable to access/give the quiz",
    " Please retry after some time in an incognito window",

    "What to do after completing LP1/ LP2/ LP3?",
    " Mark your task as finished and wait for the next instructions.",

    " Which Browser I should use?"
    "Google Chrome is recommended."
    
    "Can I use any other browser?",
    "IF you prefer any other browser, it's okay",

    " Do we need to complete all the six steps within 14 hours as you mentioned that we have to complete "
    "all the 6 steps within 2 weeks so it becomes 14 hours?",
    " It's preferred if you complete the LP1 training in 2 weeks but not mandatory. LP1, LP2,"
    " and LP3 are expected to be"
    " completed before the live projects start in July; but that doesn't mean you should give "
    "anything less than 1 hour a day or 7 hours a week towards the learning paths (LP).",


    " I had press finished button of LP1 task but want to resume the task, how to do that?",
    "You can go back to that task and then click on 'More' and then 'resume' to restart that task.",


    "The web pages on mobile are not showing properly.",
    " They are purposefully only configured for Desktops/ Laptops. In an emergency, you can use the ""show as desktop"" mode of your browser.",


    " I have opted for a blockchain internship, can I also learn about AI and do an internship in both? ",
    " You can learn both the technologies using Learning Path 2 (LP2) which will begin after the 2nd week of March, "
    "but your internship will only be continuing with the one you are selected for.",


    " Can I switch my technology now? ",
    "form-filling and got selected for the technology I’m not interested in.",
    " You cannot switch the technology currently. You have to continue with the one you are selected for."
    " In the case of multiple form entries, you just got selected for one of them; the first"
    " one that you entered. You cannot make a switch right now.",



    " how can I get to know about my progress of LP 1",
    " There is no metric to score your progress in any learning paths as it will be"
    " at a different pace for every individual.",

    "Is quiz has marks ?",
    " There is no metric to score your progress in any learning paths as it will be"
    " at a different pace for every individual.",

    "Quiz is important",
    "Yes. It is important",

    " I am not able to view a page",
    " This could be because of some issue in the cookies or extension in your browser."
    " Please try again with a different browser or open the tab with incognito mode. "
    "Also, you don't need to record your results, the quizzes are only for your "
    "knowledge check and not a metric to score you.",

    "I am logged in the training and still the website asks me to login",
    " This could be because of some issue in the cookies or extension in your browser."
    " Please try again with a different browser or open the tab with incognito mode. "
    "Also, you don't need to record your results, the quizzes are only for your "
    "knowledge check and not a metric to score you.",

    " I am having trouble finding the workgroup ( no workgroup is visible)",
    "Please ensure that you have connected to the drive of that workgroup by going to your notification "
    "and connecting to the drive of that workgroup. If that is done, please try to "
    "search for your workgroup in the search bar at the"
    "top of your screen. To search, use the keywords, 202003-IP-TechnologyName. Ex ""202003-IP-DevOps""."
    " In case there is no invitation to you, please message Cloud Counselage HR."
    " You will be added to 2 groups “202003-IP” which is a general workgroup and "
    "the other one is “202003-IP-Technology” which is a technology-specific workgroup.",


    " I am not added into my technology workgroup.",
    "Please follow the instructions given in the videos or the one in the Bitrix24 mail "
    "(these are the same videos share in the task), the tokens are given to you."
    " Ensure that you are putting the right token on the right page.",

    "I entered the tokens but it is showing user not found",
    "Please follow the instructions given in the videos or the one in the Bitrix24 mail "
    "(these are the same videos share in the task), the tokens are given to you."
    " Ensure that you are putting the right token on the right page.",

    " When does the LP1/ LP2/ LP3 begin dates and deadline/ end date?",
    " The dates to begin the learning paths (LP) are: -" 
               "LP1 - 01/03/2020"
    
               "LP2 - 18/03/2020"
    
               "LP3 - 02/04/2020" 
    
               "All learning Paths (LP) are expected to be completed by the interns before the first "
    " week of June as Live Projects will begin in that time frame.",



    " What happens in LP2? What kind of training can we expect?",
    "The main focus of LP2 is to provide you with a basic foundation of the technology you're interested in."
    " The training is also handpicked in such a way that they enable you to work on LP3 assignments"
    " which interim gives you the beginning to start your study for the selected technology and in no terms is "
    "the only/ final training you should look into."
    " Please keep learning after your LP2 is complete, that is the only way to grow in your technology of choice.",


    " What happens in LP3? What kind of training can we expect?",
    "LP3 will be assignment based and its execution and content vary from technology to technology."
    " This assignment will be like a mini-project for all interns in a particular technology which "
    "will be verified by Cloud Counselage Project Managers.",


    "What to do after LP3?",
    "You'll be given preparatory leave (PL) from April to June after that your Live Projects "
    "will be given after the first week of June.",

    "what we have to do after LP3",
    "You'll be given preparatory leave (PL) from April to June after that your Live"
    " Projects will be given after the first week of June.",

    "I see duplicate tasks been created, is it with me or everyone?",
    "You might see 2 tasks created for some of you, please ignore the duplicate one.",

    "I have two same task?/ I have two similar tasks?",
    "You might see 2 tasks created for some of you, please ignore the duplicate one",

    "Can we skip any training if we are already clear with the basics?",
    " No, these pieces of training will cover basics and there is no harm in "
    "brushing up your skills before you start with the assignments later.",


    " Is it ok to clock-out before an hour is completed if the tasks are completed? "
    "Do we need to clock-in and compulsorily complete 7 hours a week even if the tasks are completed?",
    "If the tasks are completed, there is no need to clock-in and clock-out unnecessarily for hours. However, "
    "you should keep a track of all the updates of the internship being posted on the groups.",


    " Resource links not working. What to do? Should we skip?",
    "Please do not skip any piece of training, in case you're not able to access any link please message"
    " to Cloud Counselage HR and drop an email to hrsupport@cloudcounselage.in regarding the same.",


    " What to do when our university exams start?",
    " We have provided our interns with preparatory leave from the exam season, nevertheless, you are free"
    " to work on your LP3 assignment, but we suggest to concentrate on your exams first.",


    "Is it okay to mention this internship as ongoing for college records?",
    " Yes, we'll provide every intern a joining letter as soon as all interns are inducted.",

    " Can we do another internship with IP?",
    " Yes, you can do another internship outside of Cloud Counselage but please"
    " ensure to provide 1 hour a day or 7 hours a week for IP.",

    "what is deadline for LP1/LP2/LP3",
    "All learning Paths (LP) are expected to be completed by the interns before the first  "
    " week of June as Live Projects will begin in that time frame.",

    "what is deadline for LP1",
    "All learning Paths (LP) are expected to be completed by the interns before the first  "
    "week of June as Live Projects will begin in that time frame.",

    "what is deadline for LP2",
    "All learning Paths (LP) are expected to be completed by the interns before the first "
    "week of June as Live Projects will begin in that time frame.",

    "what is deadline for LP3",
    "All learning Paths (LP) are expected to be completed by the interns before the first "
    "week of June as Live Projects will begin in that time frame.",

    "Are we getting an offer letter/Stipend?",
    "Submit your project and once it's reviewed as successful, collect your internship letter."
    " Your internship is complete after this. There is no stipend for live projects. "
    "If your work is sublime and we have a vacancy in the position you're interested in, you may be offered a "
    "chance for interviews and can get an offer letter from Cloud Counselage Pvt. Ltd.",

    "What to do after Live Projects?",
    " Your internship is complete after this. There is no stipend for live projects. ",

    "Thank you.",
    "You're welcome."
    ]

trainer = ListTrainer(chatbot)
trainer.train(conversation)

#trainer = ChatterBotCorpusTrainer(chatbot)
#trainer.train('chatterbot.corpus.english')
#answer = chatbot.get_response("Hello")
#print(answer)



print("Hi! Ask me. ")
while True:

     query = input()

     answer = chatbot.get_response(query)
   # print("You: ",query)
     if answer.confidence >= 0.3:
        print("answer.confidence : ",answer.confidence )
        print("Chatty: ", answer)
     else:
        print("answer.confidence : ", answer.confidence)
        No_given_input = 'No known response to the input was found.'
        print('Chatty:',No_given_input)
