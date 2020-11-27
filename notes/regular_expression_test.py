import re, pyperclip

phoneRegex = re.compile(r'''
#415-555-0000, 555-0000, (415) 555-0000, 555-0000 ext 12345, ext. 12345, x12345
(
((\d\d\d)|(\(\d\d\d\)))?      #area code (with or without parenthesis ) and all that optional, so ()?
(\s|-)              #first separator)
\d\d\d              #first three digits
-                   #separator
\d\d\d\d            #last 4 digits
(((ext(\.)?\s)|x)   #extentions word-part (optional)
 (\d{2,5}))?        #extention number-part (optional) and those 2 together are optional so i add ()?
)
''', re.VERBOSE)    #without verbose this would have been impossible
                    #Also keep in mind that because i have groups, "findall()"
                    #is goinf to return a list of tuples for each match and each tuple will have one string
                    #for each group. To solve that i wll add all the regex in a group by adding () at the
                    #beginning and the end of the r.e., and i will extract the group[0] which covers
                    #the entire matched text


emailRegex = re.complile(r'''
#some.+_thing@(\d{2,5}))?.com

[a-zA-Z0-9_.+]+  #name part (i created my own character class) i cannot just use \w.
                 #Remember i dont have to escape _.+ symbols when i am inside [] in my own character class
@                #@ symbol
[a-zA-Z0-9_.+]+  #domain name part. Remember the "+" at the end indicates one or more instances!
                 #the emailRegex has no groups so "findall" is going to return a list of strings!
''', re.VERBOSE)

#get the text off the clipboard
text = pyperclip.paste() # after i copied the data i run the program
extractedPhone = phoneRegex.findall(text) #returns the list of tuples 
extractedEmail = emailRegex.findall(text) #return the list of strings we want!

allPhoneNumbers = []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])

results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)
# i take the list and join it with new lines, thus removing the '' and ,

pyperclip.copy(results)

#so now, all this data has been collected, put in a nicer format and copied to the clipboard
#so i can paste it someplace!

