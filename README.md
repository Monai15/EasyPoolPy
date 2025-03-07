# โปรแกรมคำนวณค่ายกกำลังสองทีละตัว

โปรแกรมนี้เป็นการคำนวณค่ายกกำลังสองทีละตัว โดยแต่ละตัวอย่างการหน่วงเวลาที่ 1 วินาที

## อธิบายโค้ด

1.ฟังก์ชันจำลองการประมวลผมที่ใช้เวลานาน

```
  def square_number(num):
    # จำลองการประมวลผลที่ใช้เวลานาน
    time.sleep(1)
    return num**2
```

2.การประมวลผลปกติ

```
  normal_results = []
    for num in numbers:
        result = square_number(num)
        normal_results.append(result)
```

3.การประมวลแบบใช้ ProcessPoolExecute

```
  with ProcessPoolExecutor() as pool:
        # ส่งไป process pool และรับผล
        pool_result = list(pool.map(square_number, numbers))
```

## ผลลัพธ์

โปรแกรมจะแสดงผลดังนี้

- list ตัวเลขที่ใช้ประมวลผล
- ผลลัพธ์และเวลาที่ใช้ในการประมวลผลแบบปกติ
- ผลลัพธ์และเวลาที่ใช้ในการประมวลผลแบบใช้ ProcessPoolExecute
- สรุปและเปรียบเทียบเวลา
