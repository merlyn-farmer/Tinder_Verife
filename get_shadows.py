import pandas as pd
from info import list_profiles
import re
import string

def get_shadows(port):
    with open("sessions", "w") as f:
        pass
    with open("session_names", "w") as f:
        pass
    for i in range(2):
        data = list_profiles(port)
        df = pd.DataFrame(data)
        if i == 0:
            if port == "34999":
                group = "212e65d0-eba1-43d5-b4a4-2fb444f08bde"
                print(group)
            else:
                group = "91ff0f99-32a9-4c74-a1db-e1a68c25506c"
                print(group)
            locked = df.loc[df['group'] == group]
        else:
            if port == "34999":
                group = "7eace03e-b07b-4aba-a7a7-9e776ea17762"
                print(group)
            else:
                group = "b249628c-3ece-4178-b7cf-bec16589eedd"
                print(group)
            locked = df.loc[df['group'] == group]

        ids = locked["uuid"]
        print(ids)
        names = locked["name"]
        print(names)

        for i in names:
            pattern = r'[' + string.punctuation + ']'
            name = re.sub(pattern, "", i)
            with open("session_names", "a", encoding="UTF-8") as f:
                f.write(name + "\n")
            print(name)

        for i in ids:
            with open("sessions", "a", encoding="UTF-8") as f:
                f.write(str(i) + "\n")
            print(i)
