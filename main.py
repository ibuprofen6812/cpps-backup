import csv

import function as fct
import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
import config

if __name__ == '__main__':
    while True:
        fct.print_mainmenu()
        while True:
            sel = str(input("Please enter your selection: ")).capitalize().strip()
            
            if sel not in config.menu:
                print("Please enter a valid choice")
                continue
            break
        while True:
            if sel == 'A': 
                private_electricity= dict(zip(fct.store_data()[1], fct.store_data()[0])) 
                for month,private in private_electricity.items():
                    print(month,private)
                break
            if sel == 'B' :
                while True: 
                    choice=fct.get_dwelling_type()
                    if choice == 'Q':
                        break 
                    fct.get_apr_sept_data(choice)
                break

            if sel == 'C': 
                while True: #used ai to change the stucture of the code
                    choice = fct.get_dwelling_type()
                    if choice == 'Q':
                        break
                    fct.increase(choice)
                break

                

            if sel == 'D':
                
                fig, (ax1,ax2) = plt.subplots(1,2, figsize = (16,6) )
                fct.get_linegraph(ax1)
                fct.get_bargraph(ax2)
                plt.tight_layout() 
                plt.savefig("combined.png")
                plt.show() 
                plt.close('all')
                break

            if sel == 'Q':
                print("Thank you for using this programme")
                exit() #used ai for this to exit the programme without too much breaks

    