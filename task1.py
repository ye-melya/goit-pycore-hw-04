def total_salary(path):
    summe = 0
    count = 0

    try:
        with open(path,"r", encoding="utf-8") as file:
            for line in file:
                if line.strip() == "":
                    continue

                name, salary = line.strip().split(",")
                summe = summe + float(salary)
                count = count + 1

        if count == 0:
            return 0, 0
        
        average = summe / count
        return summe, average

    except FileNotFoundError:
        print("Файл не знайдено.")
        return None

    except (ValueError, UnicodeError):
        print("Некоректні дані у файлі.")
        return None

    except OSError:
        print("Не вдалося прочитати файл.")
        return None


result = total_salary("salary_file.txt")

if result is not None:
    total, average = result
    print("Загальна сума заробітної плати:", total)
    print("Середня заробітна плата:", average)

    