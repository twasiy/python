# from PIL import Image

# image = Image.open("/home/wasiy/Pictures/vault/tanha.jpg")
# image.save("/home/wasiy/Pictures/vault/tanha.ppm")
# from tkinter import *

# root = Tk()
# photo = PhotoImage(file="/home/wasiy/Pictures/vault/tanha.ppm")

# label = Label(root, image=photo)
# label.pack()

# root.mainloop()

# from tkinter import *
# from PIL import Image, ImageTk  # Import Pillow

# root = Tk()

# # Load the image using PIL
# image = Image.open("/home/wasiy/Pictures/vault/tanha.jpg")
# photo = ImageTk.PhotoImage(image)

# root.geometry('500x500')

# labelframe = LabelFrame(root,text='Future wife',font=(30))
# labelframe.place(x=100,y=50,height=400,width=300)

# label = Label(root, image=photo,text='Tanha Baby',compound=TOP,font=(30))
# label.place(x=110,y=80)

# bt = Button(root,text='ON',font=('arial',20,'bold'),relief=FLAT,bg='yellow',fg='cyan',cursor='plus')
# bt.place(x=150,y=330)

# root.mainloop()


from tkinter import *


root = Tk()
root.config(bg='#2C2C2C')
root.geometry('500x500')

var = StringVar()

# list1 =[['python','py'],['java','ja'],['c++','c++'],['c#','c#']]

# for i in list1:
#     radio = Radiobutton(root,text= i[0],font=('arial',20,'bold'),variable=var,value=i[1],bg = '#2C2C2C',fg='#1C1C1C')
#     radio.pack()


lis = ['python','java','C++','C#','C','Ruby','Perl','Go','R','swift','kotlin','Assembly','Matlab','Rust',
       'scala','Groovy','Typescript','HTML','CSS','javascript','React','Angular','Vue','Svelte','Jquery',
       'Bootstrap','Tailwind','Materialize','Bulma','Sass','Less','Stylus','Dart','Flutter','React Native',
       'Node','Django','Flask','Spring','Laravel','Codeigniter','Express','Nest','Deno','Ruby on Rails',
       'Sinatra','C++','C#','C','Ruby','Perl','Go','R','swift','kotlin','Assembly','Matlab','Rust',
       'scala','Groovy','Typescript','HTML','CSS','javascript','React','Angular','Vue','Svelte','Jquery',
       'Bootstrap','Tailwind','Materialize','Bulma','Sass','Less','Stylus','Dart','Flutter','React Native',
       'Node','Django','Flask','Spring','Laravel','Codeigniter','Express','Nest','Deno','Ruby on Rails',
       'Sinatra','C++','C#','C','Ruby','Perl','Go','R','swift','kotlin','Assembly','Matlab','Rust',
       'scala','Groovy','Typescript','HTML','CSS','javascript','React','Angular','Vue','Svelte','Jquery',
       'Bootstrap','Tailwind','Materialize','Bulma','Sass','Less','Stylus','Dart','Flutter','React Native',
       'Node','Django','Flask','Spring','Laravel','Codeigniter','Express','Nest','Deno','Ruby on Rails',
       'Sinatra','C++','C#','C','Ruby','Perl','Go','R','swift','kotlin','Assembly','Matlab','Rust',
       'MongoDB','SQL','PostgreSQL','MySQL','MariaDB','SQLite','Oracle','MSSQL','NoSQL']
listbox = Listbox(root,bg='#2C2C2C',fg='yellow',font=('arial',15,'bold'))
for i in lis:
    listbox.insert(END,i)
listbox.place(x=0,y=0)

scroll = Scrollbar(root,bg='#7C7C7C',command=listbox.yview)
scroll.place(x=480,y=0,height=500)

listbox.config(yscrollcommand=scroll.set)

root.mainloop()






