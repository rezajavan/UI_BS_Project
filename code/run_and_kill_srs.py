import os



def run_srs():
    kill_command = "killall pdsch_ue"
    os.system(command=kill_command)

    start_command = "./constlation.sh&"
    os.system(command=start_command)

def kill_srs():
    kill_command = "killall pdsch_ue"
    os.system(command=kill_command)



