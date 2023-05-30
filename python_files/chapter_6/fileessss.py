file1 = open("student_records.txt", mode='r')

file2 = open("record.txt", mode='w')

with file1, file2:
    for record in file1:
        sn, name, score = record.split()
        if sn != "002":
            file2.write(record)
        else:
            new_record = ' '.join([sn, "scholarstica", score])
            file2.write(new_record + "\n")