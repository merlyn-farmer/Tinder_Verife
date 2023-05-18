

def group_id_list(group_id, port):
    match (group_id, port):
#        case ("t_spam", "34999"):
#            g_id = ""
#        case ("t_spam", "35000"):
#            g_id = ""

        case ("merlyn", "34999"):
           g_id = "7506a15d-cca9-4ebd-be36-addf2bd53a52"
        case ("merlyn", "35000"):
           g_id = "584811b7-246c-457a-961a-7344262a90f2"

        case ("david", "34999"):
           g_id = "7506a15d-cca9-4ebd-be36-addf2bd53a52"
        case ("david", "35000"):
           g_id = "584811b7-246c-457a-961a-7344262a90f2"

        case ("FA001", "34999"):
            g_id = "a9c92733-f9a5-45d3-8b9b-494541b236d9"
        case ("FA001", "35000"):
            g_id = "4bc1480b-6b74-464b-83be-082fc71f7bd3"

        case ("FA002", "34999"):
            g_id = "3d4663c9-d23b-484e-8946-b052c436386d"
        case ("FA002", "35000"):
            g_id = "5baf834e-6f78-4f4d-a262-0cb5ee366df2"

        case ("FA003", "34999"):
            g_id = "263503bf-473f-4bd7-aa07-4b30b90b567b"
        case ("FA003", "35000"):
            g_id = "c264d602-8df3-4123-962c-f8fcdbdd06eb"

        case ("FA004", "34999"):
            g_id = "9b0e1cf3-0b73-469a-9ec8-51c2ece19721"
        case ("FA004", "35000"):
            g_id = "8bb79dbf-8b23-426c-bfa2-13394b043095"

        case ("FA005", "34999"):
            g_id = "3e2d5f12-6b00-4203-abde-4d0559d1ec36"
        case ("FA005", "35000"):
            g_id = "0a79e12e-188f-441b-8919-52edc44a097f"

        case ("FA006", "34999"):
            g_id = "4eb3cf01-3baf-4b1d-9597-bf68a4eb44a2"
        case ("FA006", "35000"):
            g_id = "2da42aed-49f7-4125-b572-a5c67fb41a97"


        case (_, "35000"):
            g_id = "00000000-0000-0000-0000-000000000000"


    return g_id
