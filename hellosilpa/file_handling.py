file1=open("demo.txt","w")
file1.write("""Sense of vision is a complex function 
of the two eyes and their central connections.
The physiological functions involved are :
maintenance of clear ocular media, maintenance 
of normal pressure ,........etc
  """)
file1.close()
file1=open("demo.txt","r")
content=file1.read()
print(content)
file1.close()
file1=open("demo.txt","a")
file1.write("""
Conjunctiva is a translucent mucous membrane 
divided into 3 parts
marginal
bulbar
tarsal
""")
file1.close()





