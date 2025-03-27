from time import *
import random as r

def mistake(partest,usertest):
    error = 0
    for i in range(len(partest)):
        try:
            if partest[i] != usertest[i] :
                error +=1
        except:
            error +=1
    return error
def speed_time( time_s,time_e,userinput):
    time_delay = time_e - time_s
    time_r = round(time_delay,2)
    speed = len(userinput) / time_r
    return round(speed)

test = ["""Documentation development may involve document drafting, formatting, submitting, reviewing, approving, distributing, reposting and tracking, etc.,
and are convened by associated standard operating procedure in a regulatory industry. It could also involve creating content from scratch.
Documentation should be easy to read and understand.
If it is too long and too wordy, it may be misunderstood or ignored. Clear, concise words should be used, and sentences should be limited to a maximum of 15 words.
Documentation intended for a general audience should avoid gender-specific terms and cultural biases.
In a series of procedures, steps should be clearly numbered.""","""The purpose of a computer program is to perform a specific task. 
The program is written in a programming language, and compiled into an executable file which can then be run on a computer.""",
"""A common type of software document written in the simulation industry is the SDF.
When developing software for a simulator, which can range from embedded avionics devices to 3D terrain databases by way of full motion control systems,
the engineer keeps a notebook detailing the development "the build" of the project or module. 
The document can be a wiki page, Microsoft Word document or other environment. 
They should contain a requirements section, an interface section to detail the communication interface of the software. 
Often a notes section is used to detail the proof of concept, and then track errors and enhancements. 
Finally, a testing section to document how the software was tested. This documents conformance to the client's requirements. 
The result is a detailed description of how the software is designed, how to build and install the software on the target device, and any known defects and workarounds. 
This build document enables future developers and maintainers to come up to speed on the software in a timely manner, 
and also provides a roadmap to modifying code or searching for bugs.""","""Technical writers and corporate communicators are professionals whose field and work is documentation. 
Ideally, technical writers have a background in both the subject matter and also in writing, managing content, and information architecture. 
Technical writers more commonly collaborate with subject-matter experts, such as engineers, technical experts, medical professionals, etc. 
to define and then create documentation to meet the user's needs. 
Corporate communications includes other types of written documentation, for example:""","""The purpose of a computer program is to perform a specific task. 
The program is written in a programming language, and compiled into an executable file which can then be run on a computer.""",
"""A common type of software document written in the simulation industry is the SDF.
When developing software for a simulator, which can range from embedded avionics devices to 3D terrain databases by way of full motion control systems,
the engineer keeps a notebook detailing the development "the build" of the project or module. 
The document can be a wiki page, Microsoft Word document or other environment. 
They should contain a requirements section, an interface section to detail the communication interface of the software. 
Often a notes section is used to detail the proof of concept, and then track errors and enhancements. 
Finally, a testing section to document how the software was tested. This documents conformance to the client's requirements. 
The result is a detailed description of how the software is designed, how to build and install the software on the target device, and any known defects and workarounds.
""","""Technical writers and corporate communicators are professionals whose field and work is documentation. 
Ideally, technical writers have a background in both the subject matter and also in writing, managing content, and information architecture. 
Technical writers more commonly collaborate with subject-matter experts, such as engineers, technical experts, medical professionals, etc. 
to define and then create documentation to meet the user's needs. 
Corporate communications includes other types of written documentation, for example:""","""Under current policy, 
employers in states that do not have mandatory E-Verify laws must complete an I-9 form for every employee, 
which requires the employer to examine an employee’s work authorization documentation, 
such as a passport, driver’s license, permanent resident card or other forms."""]

test1 = r.choice(test)
print('....Typing speed calculator....')
print(test1)
print()
print()
Time1 = time()
testinput = input('Enter: ')
Time2 = time()
print('speed:',speed_time( Time1,Time2,testinput),' w/s')
print('Error:',mistake(test1,testinput))