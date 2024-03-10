# ProgramPython02 - โปรแกรมคำนวณคะแนนรวม 100 คะแนน และเกรดนักศึกษา

count = 1
gread1 = "H"
gread2 = "S"
gread3 = "U"
while count <= 5 :
    nameStudent = str(input(f"กรุณากรอกชื่อนักศึกษาคนที่ {count} ชื่อนักศึกษา : "))
    allScore = int(input(f"กรอกคะแนนรวมของนักศึกษา {nameStudent} : "))
    workScore = int(input(f"คะแนนงานของนักศึกษา {nameStudent} : "))
    finalScore = int(input(f"คะแนนสอบของนักศึกษา {nameStudent} : "))
    totalScore = workScore + finalScore
    for i in range(1) :
        if allScore > 75 :
            print(f"คุณ {nameStudent} มีคะแนนรวมเท่ากับ {allScore} คุณได้รับเกรด {gread1}")
        elif allScore >= 50 or allScore == 75 :
            print(f"คุณ {nameStudent} มีคะแนนรวมเท่ากับ {allScore} คุณได้รับเกรด {gread2}")
        elif allScore < 50 :
            print(f"คุณ {nameStudent} มีคะแนนรวมเท่ากับ {allScore} คุณได้รับเกรด {gread3}")
    if totalScore == 65 :
        print(f"นักศึกษา {nameStudent} มีคะแนนรวม {allScore} มีคะแนนงานและคะแนนสอบเท่ากับ {totalScore}")
    else :
        print(f"ข้อมูลของ {nameStudent} ผิดพลาดกรุณากรอกใหม่")
        break
    count += 1