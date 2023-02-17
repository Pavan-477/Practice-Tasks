import json
import numpy as np
from json import JSONDecodeError


Question_bank={
1:
{
"Who developed Python Programming Language?a) Wick van Rossumb) Rasmus Lerdorfc) Guido van Rossumd) Niene Stom":"c"
},

2: 
{
"Which type of Programming does Python support?a) object-oriented programmingb) structured programmingc) functional programmingd) all of the mentioned":"d"
},

3:
{ 
"Is Python case sensitive when dealing with identifiers?a) nob) yesc) machine dependentd) none of the mentioned":"b"
},

4: 
{
"Which of the following is the correct extension of the Python file?a) .pythonb) .plc) .pyd) .p":"c"
},

5:
{
"Is Python code compiled or interpreted?a) Python code is both compiled and interpretedb) Python code is neither compiled nor interpretedc) Python code is only compiledd) Python code is only interpreted":"d"
},

6:
{
"All keywords in Python are in _________?a) Capitalizedb) lower casec) UPPER CASEd) None of the mentioned":"d"
},

7:
{
"Which of the following is used to define a block of code in Python language?a) Indentationb) Keyc) Bracketsd) All of the mentioned":"a"
},

8:
{
"Which keyword is used for function in Python language?a) Functionb) defc) Fund) Define":"b"
},

9:
{
"Which of the following character is used to give single-line comments in Python?a) //b) #c) !d) /*":"b"
},

10:
{
"Python supports the creation of anonymous functions at runtime, using a construct called __________?a) pib) anonymousc) lambdad) none of the mentioned":"c"
},

11:
{
"What is the order of precedence in python?a) Exponential, Parentheses, Multiplication, Division, Addition, Subtractionb) Exponential, Parentheses, Division, Multiplication, Addition, Subtractionc) Parentheses, Exponential, Multiplication, Division, Subtraction, Additiond) Parentheses, Exponential, Multiplication, Division, Addition, Subtraction":"d"
},

12:
{
"What does pip stand for python?a) Pip Installs Pythonb) Pip Installs Packagesc) Preferred Installer Programd) All of the mentioned" :"c"
},

13:
{
"Which of the following is true for variable names in Python?a) underscore and ampersand are the only two special characters allowedb) unlimited lengthc) all private members must have leading and trailing underscoresd) none of the mentioned":"b"
},

14:
{
"Which of the following is the truncation division operator in Python?a) |b) //c) /d) %":"c"
},

15: 
{
"What will be the output of the following Python code?l=[1, 0, 2, 0, 'hello', '', []]   list(filter(bool, l))a) [1, 0, 2, ‘hello’, ”, []]b) Errorc) [1, 2, ‘hello’]d) [1, 0, 2, 0, ‘hello’, ”, []]":"c"
},

16: 
{
"Which of the following functions is a built-in function in python?a) factorial()b) print()c) seed()d) sqrt()":"b"
},

17:
{
"Which of the following is the use of id() function in python?a) Every object doesn’t have a unique idb) Id returns the identity of the objectc) All of the mentionedd) None of the mentioned":"b"
},

18:
{ 
"Which of the following is not a core data type in Python programming?a) Tuplesb) Listsc) Classd) Dictionary":"c"
},

19:
{
"Which of these is the definition for packages in Python?a) A set of main modulesb) A folder of python modulesc) A number of files containing Python definitions and statementsd) A set of programs making use of Python modules":"b"
},

20:
{
"What will be the output of the following Python function  len(['hello',2, 4, 6])?a) Errorb) 6c) 4d) 3" : "c"
}

}

with open('Questions_file.json','w') as f:
    
    json.dump(Question_bank,f)
print('Writing finished')

with open('Questions_file.json','r') as f :
    
    all_questions=json.load(f)

class Quiz_maker:

    def __init__(self):
        pass


    def questions_picker(self,all_questions):
        no_of_questions=list(all_questions.keys())
        random_questions = np.random.choice(no_of_questions,10,replace=False)
        self.final_questions=[]
        for i in random_questions:
            self.final_questions.append(all_questions[i])
        return self.final_questions

    def quiz_display(self,final_questions):
        self.score=0
        for i in range(len(final_questions)):
            q=str(list(final_questions[i].keys()))
            Question_str=q[2:q.find('a)')]
            print(i+1,Question_str)

            opt1_str= q[q.find('a)'):q.find('b)')]
            print(opt1_str)
            opt2_str= q[q.find('b)'):q.find('c)')]
            print(opt2_str)
            opt3_str= q[q.find('c)'):q.find('d)')]
            print(opt3_str)
            opt4_str= q[q.find('d)'):-2]
            print(opt4_str)

            response=input('Enter your response : ')
            if response.lower()==list(final_questions[i].values())[0]:
                print('Yay Correct!!!')
                self.score+=1
            else:
                print('Oops Incorrect ')
            print()
        return self.score

    def evaluator(self,score):
        print('Your score is : ',self.score , 'out of 10')
        print('Your accuracy is : ',(self.score/10)*100,'%')
        return None


student=Quiz_maker()
questions=all_questions
final_questions=student.questions_picker(questions)
score=student.quiz_display(final_questions)
performance=student.evaluator(score)