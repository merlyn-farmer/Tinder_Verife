import pandas as pd
from info import list_profiles
import re
import string

def get_sessions(port, group):
    with open("sessions", "w") as f:
        pass
    with open("session_names", "w") as f:
        pass
    data = list_profiles(port)
    df = pd.DataFrame(data)
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
