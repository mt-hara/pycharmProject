import os

pid_list = []

def main():
    pid_list.append(os.getpid())
    child_id = os.forkpty()

    if child_id == 0:
        pid_list.append(os.getpid())
        print()
        print("C：Chrild process")
        print("C: my pid = {}".format(pid_list))
    else:
        pid_list.append(os.getpid())
        print()
        print("P: parent process")
        print("P: mychild pid = {}".format(child_id))
        print("P I known pid = {}".format(pid_list))

if __name__ == "__main__":
    main()