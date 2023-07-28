prompt_evaluate="""
I will give you a conversation between the manager and the customer in text format. Evaluate the work of the manager by clearly analyzing the text give an answer by writing about mistakes, correct decisions. Before writing about a mistake, first make sure that it is in the text.
here are the rules for how a manager should behave:  
greet the client and introduce himself,
show friendliness and respect,
contact the customer by name and if the manager addressed the customer at least once by name then this rule is considered fulfilled,
support the client emotionally,
get the customer interested in listening,
tell the customer the approximate time of service and what he will spend it on,
ask questions to the customer to identify the underlying need,
train the client based on their needs,
Make sure that the customer does not have any questions about the trained service,
get feedback from the customer,
inspire confidence that everything will work out,
wish a good day and say goodbye to the customer,
make it clear to the customer that we are always glad to see him.
Note that you should know:
before the start of the conversation, the manager does not know the name of the customer.
Your response should be in json format like this:
{
    "opinion": "(your general opinion)",
    "corrections": [
      {
        "mistake": "(first mistake)",
        "fix": "(how to fix)"
      },
      {
        "mistake": "(second mistake)",
        "fix": "(how to fix)"
      }
      and so on....
    ]
}  
"""

prompt_question="""
I'll give you a conversation between a customer and a manager in text format. You must use this text to give me the questions that the customer asked about Kaspi.                                                                   
Your response must be json format like this:                                                                                                    
{
   "question": [
       {
         "question": (customer question)
       }
       and so on.....
   ]  
}                                                                                                                                                                                                                                                                                                                                                                                                                              }                                                                                                                                                                           text:    
"""

prompt_technical_analysis="""
I will give you the correct answers to these questions. You have to compare them with the answers given by the manager and make an technical analysis of incorrect question 
your response must be in json format like this:
{
   "response": [
        {
          "mistake": "(incorrect answers of manager)",
          "fix": "(technical analysis of manager answers)"
        }
        and so on...
   ]
}
correct answers:
"""

prompt_markship = """
I'll give you a conversation between a customer and a manager in text format. Determine which speaker is a manager and which speaker is a client and give an answer
Your response should be in json format like this:
{
manager: (speaker  1)
customer: (speaker 2)
}                                                                                                                                                                                                                                                                                                                                                                                                                                                          
text: 
"""