import os
import subprocess as sp
#Could be done easily with gzip but condition for project was not to use external modules to make compression and use logic by my own



#Making a global ASCII list to use it during functions
ASCII=['\x00','\x01','\x02','\x03','\x04','\x05','\x06','\x07','\x08','\x09']

#Making a function for word counter so that can be updated with acii characters for 3-4 most occurring letters to decrease size
def word_counter(path):
    
    
    
    #accessing file to read
    file_word=open(path,'r')


    
    
    #accessing all lines one by one and doing changes accordingly
    text=file_word.read()
    
    
    
    #removing letters which will cause splitting problem
    special_char=['-','.',',',' ','\\n']
    for char in special_char:
        text=text.replace(char,' ')
    words=text.split()
    
    
    #list where we can write words with their occurrences
    words_count=[]
    for i in set(words):
        words_count.append([i,words.count(i)])

    
    
    #doing appropriate changes to access list in main class without much changes    
    words_count.sort(key=lambda x: x[1],reverse=True)
    return words_count
        



class compression_decompression():

    #Taking default things for compression/decompression
    def __init__(self,path,form,zip_loc):
        try:
            self.file_compression=path[0]
            self.file_decompression=path[1]
            self.zip_loc=zip_loc
            self.form=form
        except IndexError:
            print("You din't write path")
    def compression(self):
        try:
            #Opening file to access data
            file=open(f'{self.file_compression}','r')


            #print(file.readlines()) checking
            #file.seek(0)
            content=file.readlines()



            #accessing list one by one to get ASCII instead of multiple spaces
            for i in range(len(content)):
                #changing multiple space to ASCII so it wont match with any char of file
                content[i]=content[i].replace(2*' ','\x1f')

                #Even if single space remains changing it to any ASCII char wont change its size



            #Checking the size for debugging
            #size=os.path.getsize(f'{self.file_compression}')
            #print(size)

            if self.form.lower()=='yes':
                
                #Changing some words with most occurrences with ASCII code which cannot be written normally
                wocou=word_counter(self.file_compression)
                
                #making a list with words ordered with ascii code list we made at beginning
                code=[]


                #Doing changes 1 by 1
                for i in range(10):

                    #Changing line by line
                    for j in range(len(content)):
                        content[j]=content[j].replace(wocou[i][0],ASCII[i])
                    

                    #Also appending the words
                    code.append(wocou[i][0])
                
                #Doing appropriate changes
                content.append(f'\n{str(code)}')

            '''para=''
            for j in range(len(y)):
                para+=y[j].replace('\n',',')
                isnt useful when the character i replace it to is present in the txt file
                and cant get reduced if i put something big'''


            #Closing so that no bug would occur
            file.close()

            #Recognising extension
            extension=self.file_compression.split('.')


            #Writing the changes made back into file
            self.result_path=self.file_compression.replace(f'.{extension[-1]}',f'_compressed.{extension[-1]}')
            file_write=open(f'{self.result_path}', 'w')

            file_write.writelines(content)

            file_write.close()


            #Reading contents for debugging
            #file_update_read=open('file_1.txt','r')
            #print(file_update_read.read())
            #print(os.path.getsize('file_1.txt'))
            #file_update_read.close()

        #Error handling to know bug in code
        except Exception as e:
            print(f"{e} has occurred")
    
    
    def decompression(self):
        #most of the code is copied from compression cuz we need to do simple change    
        
        try:
            
            #Opening file to access data
            file=open(f'{self.file_decompression}','r')



            #print(file.readlines()) checking
            #file.seek(0)
            content=file.readlines()



            #accessing list one by one to get multiple spaces back from ASCII
            for i in range(len(content)):
                #changing ASCII char back to space
                content[i]=content[i].replace('\x1f',2*' ')

                #Even if single space remains changing it to any ASCII char wont change its size



            #Checking the size for debugging
            #size=os.path.getsize(f'{self.file_decompression}')
            #print(size)


            #Doing changes as per word optimization being chosen or not
            if self.form.lower()=='yes':
                

                #Taking codes written inside file to do changes with did earlier
                code=content[-1].strip()


                #Removing extra chars which entered during list being put into file else we could use pickle to put proper list
                remove_char=["'",']','[',' ']
                for char in remove_char:
                    code=code.replace(char, '')

                
                #Getting the actual list
                code_1=code.split(',')
                #print(code_1)
                
                
                #Doing the changes back to get the words back from ASCII codes
                for i in range(10):
                    for j in range(len(content)-1):
                        content[j]=content[j].replace(ASCII[i], code_1[i])


                #Removing codes
                content.pop(-1)



            #At last we are left \n at the end so not reading it to not get extra line at end
            content[-1]=content[-1][:-1]

            #Closing so that no bug would occur
            file.close()

            #Recognising extension for name changes
            extension=self.file_decompression.split('.')
            
            
            #Writing the changes made back into file
            self.result_path=self.file_decompression.replace(f'.{extension[-1]}',f'_decompressed.{extension[-1]}')
            file_write=open(f'{self.result_path}', 'w')

            file_write.writelines(content)

            file_write.close()
        except Exception as e:
            print(f"{e} has occurred")

    #Looked through Documentation of subprocess to do this
    def compression_using7ziporWinrar(self):
        
        
        try:
            #Recognising extension
            extension=self.file_compression.split('.')


            #creating path for compressed back in same location
            self.result_path=self.file_compression.replace(f'.{extension[-1]}','_compressed.')




            try:
                #Using subprocess to create compressed file without actually opening it
                sp.run([r'C:\Program Files\7-Zip\7z.exe','a',self.result_path,self.file_compression])
            
            except:
                sp.run([self.zip_loc,'a',self.result_path,self.file_compression])


        except:
            print("7zip not found")
    
    
    
    
    
    def decompression_using7ziporWinrar(self):
        
        
        try:

            #Recognising extension
            extension=self.file_decompression.split('.')


            #creating path for compressed back in same location
            self.result_path=self.file_decompression.replace(f'.{extension[-1]}','_decompressed\\')


            try:

                sp.run([r'C:\Program Files\7-Zip\7z.exe','x',self.file_decompression,f'-o{self.result_path}'])


            except:
                sp.run([self.zip_loc,'x',self.file_decompression,self.result_path])
        
        except:
            print("7zip not found")






print("Note:  \n- Please enter all inputs as text strings, not integers.  \n- If 7-Zip is not installeperd in its default location, type 'yes' when asked.  \n- Decompression is supported only for files compressed by this program.\n\n")

#taking operation to perform
operation=input("What operation do you want to perform?  \nType 'Compression' or 'Decompression':\n")

bulk=input("\n\nDo you want to compress/decompress multiple files at once? (yes or no):\n")



#Checking if bulk compression/decompression is selected depending on which we will do compression that many times
if bulk.lower()=='yes':

    numoffil=int(input("\n\nEnter the number of file you want to commpress/decompress (Integer value):\n"))

else:
    numoffil=1



#Checking Winrar_7Zip in system for better compression only if installed
winrar_zip=input("\n\nDo you want to use 7-Zip for compression/decompression? (yes or no):\n")


#Taking location of 7zip only if user wants to use it
if winrar_zip.lower()=='yes':
    zip_loc=input("\n\nPlease enter the path to your 7-Zip executable (leave blank if installed in default location):\n")

    #Since we are not using word optimization
    form=None

else:
    #taking none if we dont need winrar_zip
    zip_loc=None

    #taking input from user to know where the file is formal do to changes of word to ASCII
    form=input("\n\nDo you want to enable Word Optimization?  \n(This is recommended for files with many repeating words and may reduce file size; sometimes it may increase size.)  \nType 'yes' or 'no':\n")


#Using for loop for bulk compression/decompression
for i in range(numoffil):




    #Taking path of files
    path=input("\n\nEnter path of your file:\n")


    #Checking either file exists or not so that program could end before running further to catch user's mistake
    if os.path.exists(path)!=True:
        print("\nSuch file doesn't exist")


    else:


        #Arranning path with operation to pass valid arguement to main class to perform operations
        if operation.lower()=='compression':
            ipath=[path,None]

        else:
            ipath=[None,path]



        func=compression_decompression(ipath,form,zip_loc)

        print('\n\n')


        #Nested else if for appropriate output as per input
        if winrar_zip.lower()=='yes':


            if operation.lower()=='compression':
                func.compression_using7ziporWinrar()


            elif operation.lower()=='decompression':
                func.decompression_using7ziporWinrar()


            #Trying error handling without try except because this could do it easily
            else:
                print("\nTell appropriately what operation you want to do")



        elif winrar_zip.lower()=='no':


            if operation.lower()=='compression':
                func.compression()


            elif operation.lower()=='decompression':
                func.decompression()


            #Error handling without try-except
            else:
                print("\nTell appropirately what operation you want to do")



        else:
            print("\nWrite the answer appropriately for 7zip compression and decompression")

        #Printing file size before operation
        print(f'\n\nBefore Compression/Decompression size: {os.path.getsize(path)} bytes')


        #Tried to find solution to find file size after decompression using 7zip but dint understand quite
        try:
            print(f'\nAfter Compression/Decompression size: {os.path.getsize(func.result_path)}')

        #Handling error with telling user that this feature isnt avaible for 1 specific need
        except:
            print("File size after decompression from 7zip is not available right now")