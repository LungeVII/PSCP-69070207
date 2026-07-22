## 1. ข้อมูล OJ

หมายเลข/ชื่อโจทย์ OJ:

```text
2996 - [LEARNING LOGS] สลับตัวอักษร
```

OJ submission ID ถ้ามีการส่งแล้ว:

```text
541255
```

สถานะ OJ:

```text
Pass
```

เวลาที่ใช้คิดและทำโจทย์ด้วยตนเอง:

```text
0-15 minutes
```

เลือกหนึ่งข้อ:

```text
0-15 minutes
15-30 minutes
30-60 minutes
1-3 hours
3-6 hours
6-24 hours
1-3 days
4-7 days
1-4 weeks
More than 4 weeks
```


---

## 2. ความเข้าใจโจทย์ของฉัน

เขียนโจทย์ด้วยคำพูดของตนเอง

ให้อธิบาย input, output และ constraints สำคัญด้วย

ถ้ายังไม่เข้าใจโจทย์ทั้งหมด ให้เขียนสิ่งที่เข้าใจในตอนนี้ ความเข้าใจอาจยังไม่ครบหรืออาจผิดได้ แต่ต้องพยายามอธิบายอย่างจริงใจ

```text
โจทย์ให้ผมรับข้อความตัวอักษรภาษาอังกฤษยาว 5 ตัวอักษร แล้วให้สลับตัวอักษรนั้นจากหลังไปหน้า

Input:
โปรแกรมรับค่าข้อความ

Output:
โปรแกรมควรแสดงตัวอักษรที่สลับจากหลังไปหน้า และตัวพิมเล็กทั้งหมด

Constraints:
input เป็นจำนวนเต็ม ฉันควรพิจารณา 0 และตัวเลขติดลบด้วย เพราะ modulo ยังใช้ได้ใน Python
```

---

## 3. แผนแรกของฉัน

```text
Step 1: รับค่าตัวอักษร 5 ตัว
Step 2: แสดงตัวอักษรจากหลังไปหน้า โดยใช้ ค่าindex
```

---

## 4. วิธีสุดท้ายที่ใช้จริง

```text
วิธีสุดท้ายของผมเหมือนกับแผนแรก ผมรับข้อความมาและใช้ .lower() เพื่อให้ตัวพิมเล็กทั้งหมด
จากนั้นก็แสดงผมข้อความนั้นแต่แสดงแบบใช้ index ตัวที่ -1 มาถึง ตัวแรก โดยอ่านค่ากลับด้วย -1
```

---

## 5. การทดสอบของฉัน

### Test Case 1

ทำไมเลือก case นี้:

```text
มีตัวอักษรตัวพิมใหญ่
```

Input:

```text
Peter
```

Expected output:

```text
retep
```

Actual output:

```text
retep
```

Result:

```text
Pass
```

### Test Case 2

ทำไมเลือก case นี้:

```text
มีตัวอักษรตัวพิมใหญ่ตรงกลาง
```

Input:

```text
viTer
```

Expected output:

```text
retiv
```

Actual output:

```text
retiv
```

Result:

```text
Pass
```

### Test Case 3

ทำไมเลือก case นี้:

```text
เพื่อ check การสลับตัวอักษร
```

Input:

```text
viper
```

Expected output:

```text
repiv
```

Actual output:

```text
repiv
```

Result:

```text
Pass
```

---

## 6. การใช้ AI

ใช้ AI กับโจทย์นี้หรือไม่

```text
No
```

ถ้าใช้ AI ต้องทำไฟล์นี้ด้วย:

```text
ai_reflection.md
```

ถ้าถามเฉพาะเพื่อน TA หรือผู้สอน และไม่ได้ใช้ AI ไม่ต้องทำ `ai_reflection.md`

---

## 7. ความช่วยเหลือจากคน / การร่วมมือ

ได้ถามเพื่อน TA ผู้สอน หรือบุคคลอื่นเพื่อขอความช่วยเหลือในโจทย์นี้หรือไม่

```text
No
```

ถ้าใช่ ให้อธิบายสั้น ๆ ว่าได้รับความช่วยเหลือแบบใด

ตัวอย่างที่อนุญาต:

- อธิบายความหมายของโจทย์
- อธิบาย concept การเขียนโปรแกรม
- ให้ hint เกี่ยวกับแนวทาง
- คุยเรื่อง debugging
- คุยเรื่อง test cases
- ช่วยอธิบาย error message

สิ่งที่ไม่อนุญาต:

- คัดลอก code ของผู้อื่น
- ส่ง solution ของผู้อื่น
- ขอให้ผู้อื่นเขียน solution ให้
- ใช้ OJ submission ของผู้อื่น
- ขอให้ผู้อื่นส่ง OJ แทน

ใครช่วยคุณ

```text

```

เขาช่วยอะไร

```text

```

คุณยังทำอะไรด้วยตนเอง

```text

```

คุณคัดลอก code จากคนอื่นหรือไม่

```text
No
```

---

## 8. คำรับรองของนักศึกษา

เขียน `Yes` ในแต่ละ statement

| Statement | Yes/No |
|---|---|
| I wrote this submission in my own words. | Yes |
| I understand my final code. | Yes |
| I recorded the real OJ status. | Yes |
| I did not copy AI-generated text directly into this file. | Yes |
| I did not copy code from another person. | Yes |
| If I received human help, I disclosed it in this file. | Yes |
| I submitted the final code to the OJ by myself. | Yes |