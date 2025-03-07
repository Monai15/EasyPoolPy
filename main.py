import time
import random
from concurrent.futures import ProcessPoolExecutor


def square_number(num):
    # จำลองการประมวลผลที่ใช้เวลานาน
    time.sleep(1)
    return num**2


def main():
    # สร้าง list ตัวเลขมาทดสอบ
    numbers = [random.randint(1, 10) for _ in range(10)]
    print(f"list ตัวเลข: {numbers}")

    print("\nกำลังประมวลผลแบบปกติ...")
    start_time = time.time()

    normal_results = []
    for num in numbers:
        result = square_number(num)
        normal_results.append(result)
        print(f"{num} ยกกำลังสอง = {result}")

    normal_time = time.time() - start_time
    print(f"การคำนวณแบบปกติใช้เวลา {normal_time} วินาที")

    print("\nกำลังประมวลผมแบบ ProcessPoolExecutor...")
    start_time = time.time()

    with ProcessPoolExecutor() as pool:
        # ส่งไป process pool และรับผล
        pool_result = list(pool.map(square_number, numbers))

    # แสดงผล
    for num, result in zip(numbers, pool_result):
        print(f"{num} ยกกำลัง = {result}")

    pool_time = time.time() - start_time
    print(f"การคำนวณโดยใช้ process pool ใช้เวลา {pool_time} วินาที")

    # สรุป
    print(f"\nสรุป: ประมวลผลตัวเลข {len(numbers)} ตัว")
    print(f"แบบปกติใช้เวลา: {normal_time:.2f} วินาที")
    print(f"แบบขนานใช้เวลา: {pool_time:.2f} วินาที")
    print(f"ประหยัดเวลาได้: {normal_time - pool_time:.2f} วินาที")
    print(f"เร็วขึ้น: {normal_time / pool_time:.2f} เท่า")


if __name__ == "__main__":
    main()
