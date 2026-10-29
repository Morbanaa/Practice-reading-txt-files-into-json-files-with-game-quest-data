import json

def main(): 
    try:
        quest_log = []
        summary = {"Total":0}
        active_log = []
        with open("text.txt","r") as file:
            content = file.readlines()

            quest = {}
            for line in content:
                clean_line = line.strip()
                if clean_line == "":
                    continue
                elif not clean_line.count("|") == 4:
                    continue
                else:
                    val = clean_line.split("|")

                    quest["Quest ID"] = val[0].strip().title()
                    quest["Quest Name"] = val[1].strip().title()
                    quest["Quest Location"] = val[2].strip().title()
                    try:
                        quest["Quest Reward"] = int(val[3])
                    except ValueError:
                        print("Quest Reward must contain a whole number")
                    
                    quest["Quest Progress"] = val[4].strip().title()
                    if quest["Quest Progress"] == "Completed":
                        try:
                            summary["Total"] += quest["Quest Reward"]
                        except KeyError:
                            pass

                    if quest["Quest Progress"] == "In Progress":
                        active_log.append(quest)

                    quest_log.append(quest)
                    quest = {}

        # Passes data in json files
        with open("data.json","w") as file:
            json.dump(quest_log,file,indent=4)
        with open("summary.json","w") as file:
            json.dump(summary,file,indent=4)
        with open("active_quests.json","w") as file:
            json.dump(active_log,file,indent=4)

    except FileNotFoundError:
        print("File Not Found, Check File Path")
        return

    print()
    while True:
        choice = input("Enter a location to filter by: ").title()
        print()

        found = False
        for quest in quest_log:
            if choice == quest["Quest Location"]:
                found = True
                for key,value in quest.items():
                    print(f"{key}: {value}")
                print()

        if found == False:
            print("Search returned empty")
        else:
            break

           
if __name__ == "__main__":
    main()
