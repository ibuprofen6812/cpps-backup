import csv
import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
import config
def print_mainmenu():
    print("="*100)
    print("MENU")
    print(f"="*100)
    for key,value in config.menu.items():
        print(f"{key} - {value}")


def store_data() -> tuple:
    private = []
    month = []
    with open('1_2_sgallelectricity_dataset.csv',mode = "r") as f:
        data = csv.DictReader(f, delimiter=',')
        for row in data: 
            cleaned_row = float(row["Private Apts, Condo"].replace(",", "").strip())
            private.append(cleaned_row)
            month.append(row['Month'].strip())

        return(private, month)

private, month = store_data() 
#print(store_data()[0])
def get_linegraph(ax):
    store_data()
    y = np.array(private) 
    x = np.array(month)
    ax.plot(x,y, marker='o') 
    ax.set_title('Line Graph of Electrcity Consumption of private Apts/Condo Over 12 Months', fontsize = 10)
def get_bargraph(ax): 
    store_data()
    y = np.array(private) 
    x = np.array(month)
    ax.bar(x,y)
    ax.set_title('Bar Graph of Electrcity Consumption of private Apts/Condo Over 12 Months', fontsize = 10) 

def get_dwelling_type() -> str:
    while True:
            for key, values in config.dwelling_options.items():
                    print("-".join([str(key),values]))
            try: 
                choice = str(input('Enter your dwelling type option: ')).capitalize().strip()
                if choice not in ['A','B','C','D','Q']:
                    raise ValueError
                return choice
            except ValueError as error: 
                print(f'Please enter a valid character (A ,B ,C ,D or Q)')

def get_apr_sept_data(choice):
                column_name = config.dwelling_options[choice]
                values = []
                max_month = []
                if choice == 'Q':
                     return None
                with open('1_2_sgallelectricity_dataset.csv',mode = "r") as f:
                    data = list(csv.DictReader(f, delimiter=','))
                    print(f"{'Month':^10} {'-':^20}{column_name:^20}")
                    for i, row in enumerate(data, start = 1):
                        if i <= 3: 
                            continue
                        if i >9:
                            break
                        values.append(float(row[column_name]))
                        print(f"{row['Month']:^10} {'-':^20} {row[column_name]:^20}")
                    max_val = max(values)
                    for i,v in enumerate(values): #used ai to show all together, but restuctured it myseld with claude
                         if v == max_val:
                              max_month.append(data[i+3]['Month'])
                    index = values.index(max(values))
                    index+=3
                    print(f"The maximum electricity consumption is {max(values)} during the month(s) of {', '.join(max_month)} ") #used ai to come out ','.join(max_month)
                    
def increase(choice): 
     if choice == 'Q':  #used ai for this to add a quit function
          return None
     column_name = config.dwelling_options[choice] 
     data_set = []
     with open('1_2_sgallelectricity_dataset.csv', mode ='r') as f:
        data = list(csv.DictReader(f,delimiter=','))
        for i, row in enumerate(data, start =1):
            data_set.append(float(row[column_name]))
        for i in range(len (data_set)-1):
                change = (data_set[i]-data_set[i+1])/data_set[i]
                if change >= 0.03:
                    print(f'{data[i+1]['Month']} ({data[i+1][column_name]}GWh) to {data[i]['Month']} ({data[i][column_name]}GWh) has increased by {change*100:.2f}%')
                elif change <-0.03:
                    print(f'{data[i+1]['Month']} ({data[i+1][column_name]}GWh) to {data[i]['Month']} ({data[i][column_name]}GWh) has decreased by {abs(change)*100:.2f}%') 
                else: 
                     continue