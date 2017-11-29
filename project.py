import csv
import matplotlib
import matplotlib.pyplot as plt

def start():
    print("\n\nWhat you wanna know?\n")
    print("1. How often students go out to restaurants?")
    print("2. What is the main reason to go out?")
    print("3. At what time they go out?")
    print("4. What is the main expectation from the restaurants?")
    print("5. How Much time students are willing to wait to get seat?")
    print("6. Per head expenditure?")
    print("7. Which one is the most preferred restaurant?")
    print("8. See the Overall rating of different Restaurants?")
    print("9. See recommendation for customers Tara-ma?")
    get_input()
    
def rate(restaurant_name):
    total_rating=0
    total_students=0
    for data in data_restaurant_list:
        if data[6]==restaurant_name:
            total_students=total_students+1
            total_rating=total_rating+int(data[21])
    print("Overall rating of "+restaurant_name+" - "+str(total_rating/total_students)+"\t(Rated by "+str(total_students)+" students)")
    
def cal(t,p,ty):
    f = open('all.csv')
    read = csv.reader(f)
    data = list(read)
    items=[]
    for i in data:
        if(i[0]==t and i[1]==ty and i[2]==p):
            item_grp=(i[3]).split(";")
            for j in item_grp:
                items.append(j)
    ss = set(items)
    sss=list(ss)
    count=[]
    dish=[]
    dict={}
    for l in ss:
        c=0
        for i in range (0,len(items),1):
            if (items[i] == l):
                c=c+1
        count.append(c)
        dish.append(l)
        dict[l]=c
    item_no = (len(ss))
    sc = sorted(count, key=int, reverse=True)
    
    print("\nWe have records of " + str(item_no) + " items. Four most Probable Dish that the customer will eat are :\n\n")
    
    for i in range (0,4,1):
        j = count.index(sc[i])
        per = (sc[i]*100)/len(items)
        print(str(i+1)+". "+dish[j]+" - "+str(per)+"%")
    
    title=t+" "+ty+" "+p    
    plt.pie(count, labels=sss, autopct='%1.1f%%')
    plt.axis('equal')
    plt.legend()
    plt.tight_layout()
    plt.title(title)
    plt.show()
    get_input()
        
def details():
    print("\n\nIs this Afternoon or Night?\n1. Afternoon\n2. Night")
    time = str(input())
    if(time!="1" and time!="2"):
        print("Incorrect selection!")
        details()
    else:
        print("\nHas the customer come Alone or in Group?\n1. Alone\n2. Group")
        person = str(input())
        if(person!="1" and person!="2"):
            print("Incorrect selection!")
            details()
        else:
            print("\nIs the customer Veg or Non-veg?\n1. Vegetarian\n2. Non-Vegetarian")
            p_type = str(input())
            if(p_type!="1" and p_type!="2"):
                print("Incorrect selection!")
                details()
            else:
                if(time == "1"):
                    t = "AfterNoon"
                elif(time == "2"):
                    t = "Night"

                if(person == "1"):
                    p = "Alone"
                elif(person == "2"):
                    p = "Group"
    
                if(p_type == "1"):
                    ty = "Veg"
                elif(p_type == "2"):
                    ty = "Non-Veg"
                cal(t,p,ty)


def asd(position_in_csvfile,question):
    splited_data=[]
    count=[]
    
    for data in data_restaurant_list:
        data_of_response_only=data[position_in_csvfile].split(';')
        for k in data_of_response_only:
            splited_data.append(k)
    
    non_repeat_data=set(splited_data)
    lab=[]
    for data in non_repeat_data:
        data_repeat=0
        for i in range(len(splited_data)):
            if (splited_data[i] == data):
                data_repeat=data_repeat+1
        count.append(data_repeat)
        lab.append(data)
        print(data+" - "+str(data_repeat)+"/"+no_of_entries+" times.")
        
    plt.pie(count, labels=lab, autopct='%1.1f%%')
    plt.axis('equal')
    plt.legend()
    plt.tight_layout()
    plt.title(question)
    plt.show()
    get_input()
def get_input():
    response = int(input("\nEnter your choice - " ))
    print("\n")
    if response == 1:
        asd(0,"How often students go out to restaurants?")
    elif response == 2:
        asd(1,"What is the main reason to go out?")
    elif response == 3:
        asd(2,"At what time they go out?")
    elif response == 4:
        asd(3,"What is the main expectation from the restaurants?")
    elif response == 5:
        asd(4,"How Much time students are willing to wait to get seat?")
    elif response == 6:
        asd(5,"Per head expenditure?")
    elif response == 7:
        asd(6,"Which one is the most preferred restaurant?")
    elif response == 8:
        am=[]
        for i in data_restaurant_list:
            am.append(i[6])
            amm=set(am)
        for a in amm:
            rate(a)
        get_input()
    elif response == 9:
        details()
    else:
        print("Invalid choice!")
        get_input()
f = open('restaurants.csv')
read = csv.reader(f)
data_restaurant_list = list(read)
no_of_entries=str(len(data_restaurant_list))
start()


            
