# บันทึกการแก้โจทย์

ไฟล์นี้เป็นตัวอย่าง ห้ามคัดลอกเนื้อหานี้ไปใช้เป็น submission ของตนเอง

ใช้ไฟล์นี้เพื่อดูระดับรายละเอียดที่คาดหวังเท่านั้น

ตัวอย่างนี้แสดงโจทย์ง่าย ๆ ที่ไม่ได้ใช้ AI

ตัวอย่างนี้ยังแสดงวิธีเปิดเผยความช่วยเหลือเล็กน้อยจากคนด้วย เนื่องจากไม่ได้ใช้ AI นักศึกษาไม่ต้องทำ `ai_reflection.md`

---

## 1. ข้อมูล OJ

หมายเลข/ชื่อโจทย์ OJ:

```text
OJ3537 [LEARNING LOGS] Impostor
```

OJ submission ID ถ้ามีการส่งแล้ว:

```text
691147
```

สถานะ OJ:

```text
Pass
```

เวลาที่ใช้คิดและทำโจทย์ด้วยตนเอง:

```text
30-60 minutes
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

วิธีนับเวลา:

- นับเฉพาะเวลาที่ตั้งใจทำโจทย์นี้ด้วยตนเองจริง ๆ
- เริ่มนับตั้งแต่ตอนที่อ่านโจทย์ครั้งแรก
- ไม่นับเวลาพัก กินข้าว เรียน นอน เวลาที่ทำโจทย์อื่น หรือเวลาที่ไม่ได้ทำโจทย์นี้
- ถ้าใช้ AI ให้นับเฉพาะเวลาที่ทำด้วยตนเองก่อน prompt แรกที่ถาม AI
- ถ้าถามเพื่อน TA หรือผู้สอน ให้นับเฉพาะเวลาที่ทำด้วยตนเองก่อนขอความช่วยเหลือครั้งแรก
- ถ้าใช้ทั้ง AI และความช่วยเหลือจากคน ให้นับเฉพาะเวลาที่ทำด้วยตนเองก่อนขอความช่วยเหลือจากภายนอกครั้งแรก ไม่ว่าจะเป็น AI หรือคน
- ถ้าไม่ได้ใช้ AI และไม่ได้ขอความช่วยเหลือจากคน ให้นับเวลาถึงก่อนเขียน `submission.md`
- ประมาณเวลาได้ แต่ต้องซื่อสัตย์

---

## 2. ความเข้าใจโจทย์ของฉัน

เขียนโจทย์ด้วยคำพูดของตนเอง

ให้อธิบาย input, output และ constraints สำคัญด้วย

ถ้ายังไม่เข้าใจโจทย์ทั้งหมด ให้เขียนสิ่งที่เข้าใจในตอนนี้ ความเข้าใจอาจยังไม่ครบหรืออาจผิดได้ แต่ต้องพยายามอธิบายอย่างจริงใจ

```text
โจทย์ให้รับชื่อสมาชิกและบทบาทของแต่ละคน ซึ่งมีบทบาทเป็น Crewmate หรือ Impostor จนกว่าจะเจอคำว่า Start หลังจากนั้นรับชื่อสมาชิกที่ถูกโหวตให้ออกจากยานจนกว่าจะเจอคำว่า End

โปรแกรมต้องแยกสมาชิกที่ยังอยู่ในยานออกจากสมาชิกที่ถูกขับไล่ โดยแสดงชื่อเรียงตามตัวอักษร พร้อมบทบาทของแต่ละคน และนับจำนวน Impostor ที่ยังเหลืออยู่

Input:

รับข้อมูลชื่อและบทบาทในรูปแบบ JSON จนกว่าจะเจอ Start
รับชื่อสมาชิกที่ถูกขับไล่จนกว่าจะเจอ End

Output:

บรรทัดแรกแสดงจำนวน Impostor ที่ยังเหลืออยู่ ตามด้วย Impostor Remains
แสดงหัวข้อ ***Alive*** และรายชื่อสมาชิกที่ยังอยู่ในยาน เรียงตามตัวอักษร
แสดงหัวข้อ ***Dead*** และรายชื่อสมาชิกที่ถูกขับไล่ เรียงตามตัวอักษร

Constraints:

```

---

## 3. แผนแรกของฉัน

เขียนแผนแรกก่อนรับความช่วยเหลือจาก AI เพื่อน TA ผู้สอน หรือก่อนสรุป code สุดท้าย

ถ้าใช้ AI ให้เขียนแผนที่มีอยู่ก่อน prompt แรกที่ถาม AI

ถ้าถามเพื่อน TA หรือผู้สอน ให้เขียนแผนที่มีอยู่ก่อนถาม

ถ้าไม่ได้ใช้ AI และไม่ได้ขอความช่วยเหลือจากคน ให้เขียนแผนที่มีอยู่ก่อนหรือระหว่างเริ่มเขียน code

แผนนี้เขียนแบบคร่าว ๆ ได้ อาจยังไม่สมบูรณ์หรืออาจต่างจากวิธีสุดท้าย

สามารถเขียนเป็น pseudocode, flowchart idea หรือขั้นตอนความคิดได้

```text
Step 1: สร้าง dictionary สำหรับเก็บสมาชิกทั้งหมด และอีก dictionary สำหรับเก็บสมาชิกที่ถูกขับไล่
Step 2: รับข้อมูลสมาชิกและบทบาท แล้วใช้ JSON แปลงข้อมูลเป็น dictionary ก่อนนำไปเก็บรวมกัน
Step 3: เมื่อเจอ Start ให้หยุดรับข้อมูลสมาชิก
Step 4: รับชื่อสมาชิกที่ถูกโหวตออกจนกว่าจะเจอ End
Step 5: ตรวจสอบว่าชื่อที่รับเข้ามามีอยู่ใน dictionary สมาชิกหรือไม่ หากมี ให้ย้ายสมาชิกคนนั้นไปยัง dictionary ของผู้ถูกขับไล่
Step 6: นับจำนวน Impostor จากสมาชิกที่ยังอยู่ใน dictionary หลัก
Step 7: แสดงจำนวน Impostor และรายชื่อสมาชิกที่ยังอยู่กับสมาชิกที่ถูกขับไล่ โดยเรียงชื่อตามตัวอักษร

```

---

## 4. วิธีสุดท้ายที่ใช้จริง

อธิบายสั้น ๆ ว่า algorithm หรือวิธีสุดท้ายที่ใช้จริงใน code ที่ส่งคืออะไร

หัวข้อนี้ต่างจาก Section 3:

- Section 3 คือแผนแรกก่อนใช้ AI ก่อนรับความช่วยเหลือจากคน หรือก่อนเขียน code สุดท้าย
- Section 4 คือวิธีสุดท้ายที่ใช้ใน solution จริง
- ถ้าวิธีสุดท้ายเหมือนกับแผนแรก ให้เขียนว่าเหมือนกัน และอธิบายสั้น ๆ ว่าทำไม

ห้ามคัดลอกคำอธิบายจาก AI

ห้ามคัดลอกคำอธิบายจากคนอื่น

```text
เริ่มจากนำเข้า json และสร้าง dictionary สองตัว คือ data สำหรับเก็บสมาชิกที่ยังอยู่ และ dead สำหรับเก็บสมาชิกที่ถูกขับไล่

ใช้ while loop รับข้อมูลสมาชิกทีละบรรทัดจนกว่าจะเจอ Start จากนั้นใช้ json.loads() แปลงข้อมูลและ update() เพื่อเพิ่มสมาชิกลงใน dictionary

หลังจากนั้นรับชื่อสมาชิกที่ถูกโหวตออกจนกว่าจะเจอ End หากชื่ออยู่ใน data จะใช้ pop() นำสมาชิกออกจาก dictionary หลักและนำบทบาทไปเก็บใน dead

ต่อมาใช้ values() วนตรวจสอบบทบาทของสมาชิกที่ยังอยู่ เพื่อนับจำนวน Impostor แล้วใช้ sorted() เรียงชื่อก่อนแสดงผลของทั้งสองกลุ่ม
```

---

## 5. การทดสอบของฉัน

เขียน test cases อย่างน้อย 3 กรณีที่ลองเองหรือออกแบบเอง

พยายามเลือก test cases ที่แตกต่างกัน

แต่ละ test case ให้อธิบายว่าทำไมเลือกกรณีนั้น

ถ้า input หรือ output มีหลายบรรทัด ให้เขียนไว้ใน text blocks

### Test Case 1

ทำไมเลือก case นี้:

```text
ตรวจสอบว่าระบบสามารถย้ายสมาชิกที่ถูกโหวตออกไปยังกลุ่ม Dead และนับ Impostor ที่เหลืออยู่ได้ถูกต้อง
```

Input:

```text
{"Green" : "Crewmate"} 
{"Cyan" : "Crewmate"} 
{"Red" : "Crewmate"} 
{"Pink" : "Crewmate"} 
{"Lime" : "Impostor"} 
{"Blue" : "Impostor"} 
{"White" : "Crewmate"} 
{"Orange" : "Crewmate"} 
Start 
Green 
Cyan 
White 
End
```

Expected output:

```text
2 Impostor Remains
***Alive***
Blue : Impostor
Lime : Impostor
Orange : Crewmate
Pink : Crewmate
Red : Crewmate
***Dead***
Cyan : Crewmate
Green : Crewmate
White : Crewmate
```

Actual output:

```text
2 Impostor Remains
***Alive***
Blue : Impostor
Lime : Impostor
Orange : Crewmate
Pink : Crewmate
Red : Crewmate
***Dead***
Cyan : Crewmate
Green : Crewmate
White : Crewmate
```

Result:

```text
Pass
```

### Test Case 2

ทำไมเลือก case นี้:

```text
ตรวจสอบกรณีที่ Impostor ถูกขับไล่ออกทั้งหมด และมีสมาชิกที่ชื่อเหมือนชื่อบทบาท แต่มีบทบาทแตกต่างกัน
```

Input:

```text
{"Aqua" : "Crewmate"} 
{"Suisei" : "Impostor"} 
{"Fubuki" : "Crewmate"} 
{"Matsuri" : "Impostor"} 
{"Impostor" : "Crewmate"} 
{"Pekora" : "Impostor"} 
{"Korone" : "Crewmate"} 
{"Rushia" : "Crewmate"} 
{"Kusa" : "Crewmate"} 
{"Yagoo" : "Crewmate"} 
{"Marine" : "Crewmate"} 
{"Pinkguy" : "Crewmate"} 
{"Crewmate" : "Impostor"} 
{"Watame" : "Crewmate"} 
Start 
Aqua 
Suisei 
Fubuki 
Matsuri 
Crewmate 
Pekora 
End
```

Expected output:

```text
0 Impostor Remains
***Alive***
Impostor : Crewmate
Korone : Crewmate
Kusa : Crewmate
Marine : Crewmate
Pinkguy : Crewmate
Rushia : Crewmate
Watame : Crewmate
Yagoo : Crewmate
***Dead***
Aqua : Crewmate
Crewmate : Impostor
Fubuki : Crewmate
Matsuri : Impostor
Pekora : Impostor
Suisei : Impostor
```

Actual output:

```text
0 Impostor Remains
***Alive***
Impostor : Crewmate
Korone : Crewmate
Kusa : Crewmate
Marine : Crewmate
Pinkguy : Crewmate
Rushia : Crewmate
Watame : Crewmate
Yagoo : Crewmate
***Dead***
Aqua : Crewmate
Crewmate : Impostor
Fubuki : Crewmate
Matsuri : Impostor
Pekora : Impostor
Suisei : Impostor
```

Result:

```text
Pass
```

### Test Case 3

ทำไมเลือก case นี้:

```text
ตรวจสอบกรณีที่ไม่มีสมาชิกถูกโหวตออก เพื่อดูว่าสมาชิกทั้งหมดจะยังอยู่ในกลุ่ม Alive และกลุ่ม Dead จะไม่มีรายชื่อ
```

Input:

```text
{"Blue" : "Impostor"} 
{"Red" : "Crewmate"} 
Start 
End
```

Expected output:

```text
1 Impostor Remains
***Alive***
Blue : Impostor
Red : Crewmate
***Dead***
```

Actual output:

```text
1 Impostor Remains
***Alive***
Blue : Impostor
Red : Crewmate
***Dead***
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
ไม่มี
```

เขาช่วยอะไร

```text
ไม่มี
```

คุณยังทำอะไรด้วยตนเอง

```text
ฉันเขียน code เอง เลือก test cases สุดท้ายเอง รันโปรแกรมใน VS Code เอง และส่งเข้า OJ ด้วยตนเอง
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
