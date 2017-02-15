__author__ = 'project_11'

#class formats to be supported by IO group
#please follow this as we need to implement as meta data and store into the file

class user:
    def __init__(self,username='',password='',email=''):
        self.userid=username
        self.password=password
        self.email=email

class category:
    def __init__(self,categoryname='',forums=[],next_category=''):
        self.category_name=categoryname
        self.forums=forums
        self.next_category=next_category

class forum:
    def __init__(self):
        self.category=None
        self.forum_name=None
        self.createdby=None
        self.timestamp=None
class questions:
    def __init__(self,ques_name='',answers=[],timestamp='',like=0,dislike=0,created_by='',next_ques=''):
        self.ques_name=ques_name
        self.answers=answers
        self.timestamp=timestamp
        self.like=like
        self.dislike=dislike
        self.created_by=created_by
        self.next_ques=next_ques

class answers:
    def __init__(self,answers=[],created_by=[],timestamp=[],like=0,dislike=0,next_ans=''):
        self.answers=answers
        self.created_by=created_by
        self.timestamp=timestamp
        self.like=like
        self.dislike=dislike
        self.next_ans=next_ans