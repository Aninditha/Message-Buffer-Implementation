__author__ = 'Sirna'

import socket
import time
cat_list = ['1.sports','2.general','3.education','4.current affairs','5.human relations','6.technology']

def NewUser(s):
    s.send('8')
    s.send(raw_input("Enter the user name :"))
    s.send(raw_input("Enter the password :"))
    s.send(raw_input("Re Enter the password :"))
    s.send(raw_input("Enter email id :"))
    data=s.recv(2048)
    if data=='True':
        print "Registration Successful\n"
        return
    else:
        print data
        NewUser(s)

def OldUser(s):
    s.send('9')
    name=raw_input("Enter the user name:")
    s.send(name)
    s.send(raw_input("Enter the password:"))
    s.send(raw_input("Enter email id :"))
    data=s.recv(1024)
    if data=="True":
        print "Welcome ",name,"\n"
        return
    else:
        print data
        OldUser(s)

def addForum(s,category):
    s.send('2')
    s.send(category)
    s.send(raw_input("Enter forum name :"))
    print s.recv(1024)

def postQuestion(s,category,forumname):
    s.send('4')
    print category
    s.send(category)
    time.sleep(0.5)
    print category ,",sent"
    print forumname
    s.send(forumname)
    time.sleep(0.5)
    print forumname," sent"
    question=raw_input("Enter your question :")
    print question
    s.send(question)
    print "data sent"
    print s.recv(1024)
    print "waiting"

def postAnswer(s,category,forumname,question):
    s.send('5')
    s.send(category)
    time.sleep(0.5)
    s.send(forumname)
    time.sleep(0.5)
    s.send(question)
    time.sleep(0.5)
    s.send(raw_input("Enter your answer :"))
    print s.recv(1024)

def screen3(s,category,forumname,question):
    while 1:
        ch=raw_input('1.View Answer\n2.Post Answer\n3.Go Back\n')
        if ch=='1':
            print "inside 1"
            s.send('7')
            print category
            s.send(category)
            time.sleep(0.5)
            print category,"sent"
            s.send(forumname)
            time.sleep(0.5)
            print forumname,"sent"
            s.send(question)
            print question ,"sent"
            data=s.recv(1024)
            if data=='None':
                print "No ansers posted....Do you want to post an answer?"
                ch1=raw_input('1.Yes\n2.No\n')
                if ch1=='1':
                    postAnswer(s,category,forumname,question)
                elif ch=='2':
                    return
            else:
                print data
        elif ch=='2':
            postAnswer(s,category,forumname,question)
        elif ch=='3':
            return


def screen2(s,category,forumname):
    while 1:
        ch=raw_input('1.View Question\n2.Post Question\n3.Select Question\n4.Go Back\n')
        if ch=='1':
            s.send('6')
            print " 6 sent"
            s.send(category)
            time.sleep(0.5)
            print category,",sent"
            s.send(forumname)
            time.sleep(0.5)
            print forumname,"sent"
            data=s.recv(1024)
            if data=='None':
                print "No Questions posted....Do u want to post a question?"
                ch1=raw_input('1.Yes\n2.No\n')
                if ch1=='1':
                    postQuestion(s,category,forumname)
                elif ch1=='2':
                    return
            else:
                print data
        elif ch=='2':
            postQuestion(s,category,forumname)
        elif ch=='3':
            question=raw_input('Enter question for which you have to post the answer\n')
            screen3(s,category,forumname,question)
        elif ch=='4':
            return

def screen1(s,category):
    while 1:
        s.send('3')
        s.send(category)
        data=s.recv(1024)
        if data=='None':
            print "No Forums created....Do u want to add a new Forum?"
            ch=raw_input('1.Yes\n2.No\n')
            if ch=='1':
                addForum(s,category)
            else:
                return 2
        else:
            print data
            ch=raw_input('1.Add Forum\n2.View Forum\n3.Go Back\n')
            if ch=='1':
                addForum(s,category)
            elif ch=='2':
                forumname = raw_input("Enter forumname :")
                screen2(s,category,forumname)
            elif ch=='3':
                return

def main(s):
    while 1:
        print cat_list
        choice=raw_input("Select the category :")
        if choice=='7':
            return
        category=cat_list[int(choice)-1][2:]
        screen1(s,category)

def createsocket():
    port=1234
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostname()
    s.connect((host , port))
    print "Welcome to Forum-11"
    choice=raw_input("1.SignIn\n2.SignUp\n")
    if choice=='1':
        OldUser(s)
    else:
        NewUser(s)
    main(s)

if __name__ == "__main__":
    createsocket()
