def gradingStudents(grades):
    lip = []
    for i in grades:
        if i >= 38:
            rim = i + 2
            kip = i + 1
            if rim % 5 == 0:
                lip.append(rim)
            elif kip % 5 == 0:
                lip.append(kip)
            else:
                lip.append(i)
        else:
            lip.append(i)
