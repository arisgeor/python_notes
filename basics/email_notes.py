#! python3

#Simple Mail Transfer Protocol
import smtplib 
conn = smtplib.SMTP('smtp.gmail.com', 587) #server, port_number
conn.starttls() #begin the encryption #220 means everything is ok.
conn.ehlo() #connect to smtp server.

conn.login('aoristos13@gmail.com', 'kadcaihaecagsaxmaloargaa')
conn.sendmail('aoristos13@gmail.com', 'aris.georgoulas@hotmail.com','Subject: So long \n\n Dear Aris\n, Its been so long since I last heard from you')
#the structure is:(from, to, body)
conn.quit()

#Gmail --> smtp.gmail.com, 587
#Outlook --> smtp-mail.outlook.com, 587
#Yahoo --> smtp.mail.yahoo.com, 587

#you can also check your inbox, which is kinda complicated. 
#you can always check IMAP documentataion.