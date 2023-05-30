file = open("student_records.txt", mode = 'w')
file.write("001 joy 88\n")
file.write("002 james 97\n")
file.close()

file = open("student_records.txt", mode = 'a')
file.write("003 jude 84\n")
file.write("04 jennifer 69\n")

file.close()
