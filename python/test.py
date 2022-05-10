import GWSF
import os

def main():
    os.system("clear")
    test_GWSF_FILE = "test.gwsf"
    print(GWSF.getGWSFValue(test_GWSF_FILE, "NAME"))
    print(GWSF.getGWSFValue(test_GWSF_FILE, "VERSION"))
    print(GWSF.getGWSFValue(test_GWSF_FILE, "AGE"))
    print(GWSF.getGWSFValue(test_GWSF_FILE, "LIKES_APPLES"))

    
    age = GWSF.getGWSFValue(test_GWSF_FILE, "AGE"); print(age)

    if age == 14:
        GWSF.changeGWSFValue(test_GWSF_FILE, "AGE", 15)
        pass
    if age == 15:
        GWSF.changeGWSFValue(test_GWSF_FILE, "AGE", 14)
        pass
    pass

if __name__ == '__main__':
    main()