def SearchRequest():
    ### This Will Hold our Input Data
    SearchData = [[],[],[],[]]

    ### This Will Run The Question Prompts We Want Filled
    def promptQuestions():

        # Get User First Name
        def userFirst():
            return SearchData[0].append(str(input('Enter First Name Here: ')))

        # Get User Last Name
        def userLast():
            return SearchData[1].append(str(input('Enter Last Name Here: ')))
        # Get User Student ID
        def userStudent():
            return SearchData[2].append(int(input('Enter Student ID Number: ')))

        # Ask If They Want to Add Additional Info; Entering 0 Will Exit The Asking Phase
        # Once Completed We Will Start the UserId Lookup Phase
        def userInfo():
            #Beginning Prompt
            userInfo = input('Enter More Details Or Press 0 to Enter Search Mode')
            #List We'll Be Using To Hold Inputs
            output = []
            #Append First input To our Output List
            output.append(userInfo)

            while userInfo != "0":
                #If 0 Was Not Entered: Ask To Enter More Details
                userInfo=input('Enter More Details: ')
                #Append Details To Our Output List
                output.append(userInfo)
            else:
                print('Entering Search Mode')
                #Append Result List To Our Main Search Data
                SearchData[3].append(output)

        # Ending Of Prompt Questions
        def runQuestions():
            """This will be used to hold the order of execution"""
            userFirst()
            userLast()
            userStudent()
            userInfo()
            return SearchData
        return runQuestions()

        #Create a Search Mode Allowing User To Lookup ID
    def SearchMode():
            #Gets Input ID to LookUP
        def SearchStudentID():
            return int(input('Enter Student ID: '))
        #Returns the matching ID as long as the ID is the same as the index Number
        return SearchData[2][SearchStudentID()-1]

    
    # Final Layer to Our Searching Process
    def runSearchProcess():

        #Begins Main Prompt Phase
        promptQuestions()

        #Once Everything is completed, Return the search Modes Result
        return SearchMode()
    #Ending Of Search Request
    return runSearchProcess()


print(SearchRequest())