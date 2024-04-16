import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import sys

def is_csv(file_name):
    split_list = file_name.split('.')
    if(split_list[-1] == 'csv'):
        return True

    print("Error: not a .csv file.")
    return False

def visualize_data(file_name):
    if(is_csv(file_name)):
        df = pd.read_csv(file_name)
        
        # Extract columns
        time = df['Time']
        Ax = df['Ax']
        Ay = df['Ay']
        Az = df['Az']
        Gx = df['Gx']
        Gy = df['Gy']
        Gz = df['Gz']

        # Plot each column as a separate line
        fig, axs = plt.subplots(2)

        axs[0].plot(time, Ax, 'b-', label='Ax')
        axs[0].plot(time, Ay, 'g-', label='Ay')
        axs[0].plot(time, Az, 'r-', label='Az')
        axs[1].plot(time, Gx, 'b-', label='Gx')
        axs[1].plot(time, Gy, 'g-', label='Gy')
        axs[1].plot(time, Gz, 'r-', label='Gz')

        # Set labels and title
        fig.suptitle('Sensor Data Visualization')
        for ax in axs.flat:
            
            ax.set(xlabel='Time', ylabel='Values')

            x_patch = mpatches.Patch(color='blue', label='X axis')
            y_patch = mpatches.Patch(color='green', label='Y axis')
            z_patch = mpatches.Patch(color='red', label='Z axis')
            ax.legend(handles=[x_patch, y_patch, z_patch])

        # Show the plot
        plt.show()

if __name__ == "__main__":
    if(len(sys.argv) != 2):
        print("Error: incompatible arguments. To run, use 'python data_visualization.py your_file.csv'.")
    else:
        file_name = sys.argv[1]
        visualize_data(file_name)
