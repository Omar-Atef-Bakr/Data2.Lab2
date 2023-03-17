import matplotlib.pyplot as plt

def plot_data(*args, x = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14], labels=None, title="Example Plot", xlabel="X Axis Label", ylabel="Y Axis Label"):
    # Create a figure and axis object
    fig, ax = plt.subplots()

    # Plot the data and add labels
    for i, data in enumerate(args):
        if labels is not None and i < len(labels):
            ax.plot(x, data, label=labels[i])
        else:
            ax.plot(x, data, label=f"Data {i+1}")

    # Add labels and title to the plot
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)

    # Add a legend to the plot
    ax.legend()

    # Show the plot
    plt.show()
