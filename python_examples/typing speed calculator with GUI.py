from tkinter import *
from time import *
import random as r

def normalize_text(text):
    """
    Normalize text by stripping leading/trailing whitespace and
    replacing multiple spaces/newlines with a single space.
    """
    return " ".join(text.split())


def mistake(partest, usertest):
    """
    Compare the normalized source text and user input character by character.
    """
    # Normalize both texts so spacing differences are ignored.
    norm_source = normalize_text(partest)
    norm_user = normalize_text(usertest)

    error = 0
    for i in range(len(norm_source)):
        try:
            if norm_source[i] != norm_user[i]:
                error += 1
        except IndexError:
            # If user input is shorter, count the missing characters as errors.
            error += 1
    return error


def speed_time(time_s, time_e, userinput):
    """
    Calculate the typing speed in characters per second based on the raw user input.
    """
    time_delay = time_e - time_s
    if time_delay == 0:
        time_delay = 1  # Prevent division by zero.
    speed = len(userinput) / time_delay
    return round(speed)

start_time = None
test_text = ""


def start_typing():
    global start_time, test_text

    # If start_time is None, it's the start of a new test.
    if start_time is None:
        # Define the list of sample texts.
        test_list = [("""Documentation development may involve document drafting, formatting, submitting, reviewing, approving, distributing, reposting and tracking, etc.,
and are convened by associated standard operating procedure in a regulatory industry. It could also involve creating content from scratch.
Documentation should be easy to read and understand.
If it is too long and too wordy, it may be misunderstood or ignored. Clear, concise words should be used, and sentences should be limited to a maximum of 15 words.
Documentation intended for a general audience should avoid gender-specific terms and cultural biases.
In a series of procedures, steps should be clearly numbered."""),("""The purpose of a computer program is to perform a specific task. 
The program is written in a programming language, and compiled into an executable file which can then be run on a computer."""),
("""A common type of software document written in the simulation industry is the SDF.
When developing software for a simulator, which can range from embedded avionics devices to 3D terrain databases by way of full motion control systems,
the engineer keeps a notebook detailing the development "the build" of the project or module. 
The document can be a wiki page, Microsoft Word document or other environment. 
They should contain a requirements section, an interface section to detail the communication interface of the software. 
Often a notes section is used to detail the proof of concept, and then track errors and enhancements. 
Finally, a testing section to document how the software was tested. This documents conformance to the client's requirements. 
The result is a detailed description of how the software is designed, how to build and install the software on the target device, and any known defects and workarounds. 
This build document enables future developers and maintainers to come up to speed on the software in a timely manner, 
and also provides a roadmap to modifying code or searching for bugs."""),("""Technical writers and corporate communicators are professionals whose field and work is documentation. 
Ideally, technical writers have a background in both the subject matter and also in writing, managing content, and information architecture. 
Technical writers more commonly collaborate with subject-matter experts, such as engineers, technical experts, medical professionals, etc. 
to define and then create documentation to meet the user's needs. 
Corporate communications includes other types of written documentation, for example:"""),("""The purpose of a computer program is to perform a specific task. 
The program is written in a programming language, and compiled into an executable file which can then be run on a computer."""),
("""A common type of software document written in the simulation industry is the SDF.
When developing software for a simulator, which can range from embedded avionics devices to 3D terrain databases by way of full motion control systems,
the engineer keeps a notebook detailing the development "the build" of the project or module. 
The document can be a wiki page, Microsoft Word document or other environment. 
They should contain a requirements section, an interface section to detail the communication interface of the software. 
Often a notes section is used to detail the proof of concept, and then track errors and enhancements. 
Finally, a testing section to document how the software was tested. This documents conformance to the client's requirements. 
The result is a detailed description of how the software is designed, how to build and install the software on the target device, and any known defects and workarounds.
"""),("""Technical writers and corporate communicators are professionals whose field and work is documentation. 
Ideally, technical writers have a background in both the subject matter and also in writing, managing content, and information architecture. 
Technical writers more commonly collaborate with subject-matter experts, such as engineers, technical experts, medical professionals, etc. 
to define and then create documentation to meet the user's needs. 
Corporate communications includes other types of written documentation, for example:"""),("""Under current policy, 
employers in states that do not have mandatory E-Verify laws must complete an I-9 form for every employee, 
which requires the employer to examine an employee’s work authorization documentation, 
such as a passport, driver’s license, permanent resident card or other forms.""")]
        test_text = r.choice(test_list)

        # Clear any existing text and insert the new source text.
        textbox_source.config(state=NORMAL)
        textbox_source.delete("1.0", END)
        textbox_source.insert(END, test_text)

        # Configure a tag for paragraph alignment.
        textbox_source.tag_configure("para", justify=LEFT, lmargin1=10, lmargin2=10)
        textbox_source.tag_add("para", "1.0", "end")

        # Disable editing so that the source text remains unchanged.
        textbox_source.config(state=DISABLED)

        # Clear the destination text box.
        textbox_des.delete("1.0", END)

        # Record the start time.
        start_time = time()

        # Update the button text.
        main_button.config(text="Done")
    else:
        # If start_time is already set, the user has finished typing.
        end_time = time()
        userinput = textbox_des.get("1.0", END).strip()  # Remove any extra whitespace.

        # Calculate typing speed and errors.
        speed = speed_time(start_time, end_time, userinput)
        errors = mistake(test_text, userinput)

        # Update the labels with the results.
        speedlab_val.config(text=str(speed) + " w/s")
        errorlab_val.config(text=str(errors))

        # Reset the start time for the next test.
        start_time = None

        # Change the button text to allow a restart.
        main_button.config(text="Restart")


root = Tk()
root.title('.....Typing speed calculator.....')
root.geometry('1200x1000+300+40')
root.config(bg='#1C1C1C')
root.resizable(False,False)
lab_main = Label(root, text='Typing speed calculator',font=('Arial',20,'bold'),bg='#1C1C1C',fg='yellow')
lab_main.place(x= 470,y= 20)

lab_main_line = Label(root, text='...............................................',font=('Arial',20,'bold'),bg='#1C1C1C',fg='yellow')
lab_main_line.place(x= 450,y= 55)

lab_source = Label(root, text='Source text:',font=('Arial',20,'bold'),bg='#1C1C1C',fg='yellow')
lab_source.place(x= 20,y= 100)

textbox_source = Text(root,font=('Arial',10,'bold'),fg='#1C1C1C',bg='white',wrap=WORD)
textbox_source.place(x= 25,y= 150,width= 1150,height= 350)

lab_dest = Label(root, text='Destination text:',font=('Arial',20,'bold'),bg='#1C1C1C',fg='yellow')
lab_dest.place(x= 20,y= 520)

textbox_des = Text(root,font=('Arial',10,'bold'),fg='#1C1C1C',bg='white',wrap=WORD)
textbox_des.place(x= 25,y= 570,width= 1150,height= 200)

speedlab = Label(root, text= 'Speed:',font= ('Arial',20,'bold'),bg='#303030',fg='yellow')
speedlab.place(x= 50,y= 800,height= 70,width= 100)

speedlab_val = Label(root, text= '00',font= ('Arial',20,'bold'),bg='#303030',fg='yellow')
speedlab_val.place(x= 150,y= 800,height= 70,width= 250)

errorlab = Label(root, text= 'Error:',font= ('Arial',20,'bold'),bg='#303030',fg='yellow')
errorlab.place(x= 810,y= 800,height= 70,width= 100)

errorlab_val = Label(root, text= '00',font= ('Arial',30,'bold'),bg='#303030',fg='yellow')
errorlab_val.place(x= 910,y= 800,height= 70,width= 250)

main_button = Button(root, text='LOCATE', font=('Arial',30, 'bold'),bg='#303030',fg='yellow',command=start_typing)
main_button.place(x= 480,y= 900,height= 70,width= 250)

root.mainloop()