#-------------------------------------------------------------------------------
# Name:        ImageDbAssesment
# Purpose:      to collect data of an image file and insert it into a csv file so it can be imported into into a database
#
# Author:      Flora Edwards
#
# Created:     22/07/2015
# Copyright:   (c) Flora Edwards 2015
#-------------------------------------------------------------------------------
#!/usr/bin/env python

from tkinter import *

import tkinter.messagebox

class Files:
    def __init__(self, image_id, file_name, file_type, image_title, owner, licence):
        self.image_id= image_id
        self.file_name= file_name
        self.file_type= file_type
        self.image_title = image_title
        self.owner= owner
        self.licence= licence

    def get_image_id(self):
        return self.image_id
    def get_file_name(self):
        return self.file_name
    def get_file_type(self):
        return self.file_type
    def get_image_title(self):
        return self.image_title
    def get_owner(self):
        return self.owner
    def get_licence(self):
        return self.licence

class GUI:
    def __init__(self):
        window = Tk()
        window.title("Images database")
        window.minsize(width=400, height=350)
        self.ready_to_write = False
        self.recordlist = []
        self.licence = StringVar(window)

        #labels, entry fields and buttons
        image_id_label = Label(window, text='Enter Image ID:')
        image_id_label.grid(row = 1, column=1, sticky = 'w', pady = 10, padx = 10)
        self.image_id_field = Entry(window)
        self.image_id_field.grid(row = 1, column=2, sticky = 'w', pady = 10, padx = 10)

        file_name_label = Label(window, text='Enter File Name:')
        file_name_label.grid(row = 2, column=1, sticky = 'w', pady = 10, padx = 10)
        self.file_name_field = Entry(window)
        self.file_name_field.grid(row = 2, column=2, sticky = 'w', pady = 10, padx = 10)

        file_type_label = Label(window, text='Enter File type:')
        file_type_label.grid(row = 3, column=1, sticky = 'w', pady = 10, padx = 10)
        self.file_type_field = Entry(window)
        self.file_type_field.grid(row = 3, column=2, sticky = 'w', pady = 10, padx = 10)

        image_title_label = Label(window, text='Enter Image Title:')
        image_title_label.grid(row = 4, column=1, sticky = 'w', pady = 10, padx = 10)
        self.image_title_field = Entry(window)
        self.image_title_field.grid(row = 4, column=2, sticky = 'w', pady = 10, padx = 10)

        owner_label = Label(window, text='Enter Image Owner:')
        owner_label.grid(row = 5, column=1, sticky = 'w', pady = 10, padx = 10)
        self.owner_field = Entry(window)
        self.owner_field.grid(row = 5, column=2, sticky = 'w', pady = 10, padx = 10)

        licenceEntry1 = Label(window, text='What licence does this image have?')
        licenceEntry1.grid(row = 6, column=1, sticky = 'w', pady = 10, padx = 10)
        #drop down menu because there are only 6 options and this stops user from putting any random thing in
        self.licenceEntry=OptionMenu(window, self.licence, "Attribution", "Attribution-ShareAlike", "Attribution-NoDerivs", "Attribution-NonCommercial", "Attribution-NonCommercial-ShareAlike", "Attribution-NonCommercial-NoDerivs")
        self.licenceEntry.grid(row = 6, column=2, sticky = 's', pady = 10, padx = 10)

        button_label = Label(window, text='Press to validate:')
        button = Button(window, text='Submit', command=self.doSubmit)
        button_label.grid(row = 7, column = 1, sticky = 'w', pady = 5, padx = 10)
        button.grid(row = 7, column = 2, sticky = 's', pady = 5, padx = 10)

        button_label1 = Label(window, text='Convert Record to csv')
        button1 = Button(window, text='write to csv', command=self.writetocsv)
        button_label1.grid(row = 8, column = 1, sticky = 'w', pady = 5, padx = 10)
        button1.grid(row = 8, column = 2, sticky = 's', pady = 5, padx = 10)

        window.mainloop()

    def doSubmit(self):
        #checking that field entries are not too long but still existant, this helps when putting the created csv file into a databse which will have limits for each collumn
        if len(self.image_id_field.get()) <1 or len(self.file_name_field.get()) <1 or len(self.file_type_field.get()) <1 or len(self.image_title_field.get()) <1 or len(self.owner_field.get()) <1 or len(self.licence.get()) <1:
            tkinter.messagebox.showwarning('Warning!','Please enter a value for all fields.')
        elif len(self.image_id_field.get()) >10 or len(self.file_name_field.get()) >20 or len(self.file_type_field.get()) >5 or len(self.image_title_field.get()) >30 or len(self.owner_field.get()) >30:
            tkinter.messagebox.showwarning('Warning!','one or more of your entries are too long. ID needs to be less than 10 digits, file name needs to be less than 20 characters, image title and owner need to be less than 30 characters each')
        else:
            try:
                validated_image_id = int(self.image_id_field.get())
                self.recordlist.append(Files(self.image_id_field.get(), self.file_name_field.get(), self.file_type_field.get(), self.image_title_field.get(), self.owner_field.get(), self.licence.get()))
                self.ready_to_write= True
                tkinter.messagebox.showinfo('Notice','Submission Sucessful')

                self.image_id_field.delete(0, END) #clears fields so the user doesnt have to backspace all of them to input next data
                self.file_name_field.delete(0, END)
                self.file_type_field.delete(0, END)
                self.image_title_field.delete(0, END)
                self.owner_field.delete(0, END)
            except:
                tkinter.messagebox.showwarning('Warning!','Please check your entries are correct, Image Id needs to be in digits.')
                print('Please check your entries are correct')

    def writetocsv(self):
        import csv
        file_name = 'images.csv'

        if self.ready_to_write: #cheacks data has been previously validated
            ofile = open(file_name, 'a') #appending the file so the user can input new data without getting rid of all the old data
            writer = csv.writer(ofile, delimiter=',', lineterminator='\n') #
            #goes through all data submitted in the gui and writes it into the csv file
            for record in self.recordlist:
                writer.writerow([record.get_image_id(),record.get_file_name(), record.get_file_type(), record.get_image_title(), record.get_owner(), record.get_licence()])
                print(record.get_file_name())
            ofile.close()
            tkinter.messagebox.showinfo('Notice',file_name+' File Generated Successfully')
            self.ready_to_write= False
        else:
            tkinter.messagebox.showwarning('Error!', 'You need to Validate your data')

GUI()
