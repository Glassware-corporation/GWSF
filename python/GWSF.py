
_version_ = "0.1.1"

def getGWSFValue(GWSF_file_path, VAR_NAME):
    try:
        GWSF_file = open(GWSF_file_path)
    except:
        raise Exception("GWSF file not found")
    
    for line in GWSF_file:
        if line.startswith(VAR_NAME):
            Value = line.split("-")[1].strip() 
            Value = Value.split("ENDL")[0].strip()
            return Value
    pass

def main():
    print("This is a library\nnot a program\n\n")
    choice = input("What do you want to do?\n1. settings\n2. exit\n")
    if choice == "1":
        print("settings")
        choice2 = input("1. version\n2. exit\n")
        if choice2 == "1":
            print("version")
            print(_version_)
            pass
        elif choice2 == "2":
            print("exit")
            exit(0)
        pass
    elif choice == "2":
        print("exit")
        exit(0)
    else:
        print("Invalid choice")
        main()
    pass

if __name__ == '__main__':
    main()