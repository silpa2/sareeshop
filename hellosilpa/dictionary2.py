dic={"soap":30,"shampoo":120,"oil":250,"powder":170}
print("Baby products for you ")
print("""products included:
soap
shampoo
oil
powder""")
v=input("Enter product name to know it's price ").lower()
for item in dic:
    if item==v:
        print("{}: Rs.{}".format(item, dic[item]))
