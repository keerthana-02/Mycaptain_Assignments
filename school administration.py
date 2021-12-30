#PROJECT--- SCHOOL ADMINISTRATION

import csv

#creating a function to store split up list
def write_into_csv(info_list):
    with open("Student_info.csv",'a') as csv_file:
        writer=csv.writer(csv_file)
        
        if(csv_file.tell()==0):
            writer.writerow(["Name", "Age", "Contact number", "E-mail ID"])

        writer.writerow(info_list)


if __name__=='__main__':
    stu_no=1
    condition=True
    while(condition==True):
        print("**************************************************")
        Student_details=input("\nEnter student #{} details(Name age contact number Email ID):".format(stu_no))
        print("Entered info:",Student_details)

        #Splitting the info

        Stu_list=Student_details.split(' ')
        print("After splitting:",str(Stu_list))

        print("\nThe entered info is-\n Student no:{} \n Name:{} \n Age:{} \n Contact number:{} \n E-Mail ID:{}".format(stu_no,Stu_list[0],Stu_list[1],Stu_list[2],Stu_list[3]))

        check=input("\nIs the info correct?:")
        if(check=='yes'):
            check=True
            #Function call
            write_into_csv(Stu_list)
            
            condition=input("\nContinue?:")
            if(condition=='yes'):
                print("**************************************************")
                condition=True
                stu_no+=1
            else:
                condition=False

        else:
            print("\nPlease re-enter the values")