# ProgramPython_TotalScore100
🎓 THIS PROGRAM PYTHON TOTAL SCORE 100 USING LEARNING AND PORTFOLIO 🐍

## PROGRAM PYTHON TOTAL SCORE 100 

```
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
```

### RESULT

#### กรณีที่คะแนนรวมทั้งหมดมากกว่า 75 คะแนน

![Pass](https://github.com/DevChalaam/ProgramPython_CalculateExpenses/assets/124075393/25701711-4a62-474b-bf2f-98e2e99bd16c)

#### กรณีที่คะแนนรวมทั้งหมดน้อยกว่าหรือเท่ากับ 50 คะแนน

![notPass](https://github.com/DevChalaam/ProgramPython_CalculateExpenses/assets/124075393/38a88324-680e-4fbd-a720-1f793fb0eeeb)
