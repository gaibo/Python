list_file = open("/workshop/contact_list.txt", "r")
output_file = open("/workshop/email_list.txt", "w")
for line in list_file:
    words = line.split()
    for word in words:
        if word.find("@") != -1:
            output_file.write(word + "\n")
list_file.close()
output_file.close()