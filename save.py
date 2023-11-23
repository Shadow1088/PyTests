hp = 1000
wood = 5000
iron = 250
kills = 200000

stats_dict = {
    "hp =": hp,
    "wood =": wood,
    "iron =": iron,
    "kills =": kills
    }

def save():
    save_file_name = "save_file.txt"
    new_content = []

       
    with open(save_file_name) as save_file:
        lines = save_file.readlines()

    for line in lines:
            updated_line = ""

            for key, value in stats_dict.items():
                if key in line:
                    updated_line = f"{key} {value}\n"

            if updated_line:
                new_content.append(updated_line)
            else:
                new_content.append(line)


    with open(save_file_name, "w") as save_file:
        save_file.writelines(new_content)

save()
