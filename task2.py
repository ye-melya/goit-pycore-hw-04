def get_cats_info(path):
    cats = []

    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                if line.strip() == "":
                    continue

                cat_id, name, age = line.strip().split(",")

                cat = {
                    "id": cat_id,
                    "name": name,
                    "age": age
                }

                cats.append(cat)

        return cats

    except FileNotFoundError:
        print("Файл не знайдено.")
        return None

    except (ValueError, UnicodeError):
        print("Некоректні дані у файлі.")
        return None

    except OSError:
        print("Не вдалося прочитати файл.")
        return None


cats_info = get_cats_info("cats_file.txt")

if cats_info is not None:
    print(cats_info)