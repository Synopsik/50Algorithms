import matplotlib.pyplot as plt

def plot(plot_list):
    plots = len(plot_list)
    plot_mark = '.-'
    for item in range(plots):
        name = plot_list[item][0]
        y = plot_list[item][1]
        try:
            plot_mark = plot_list[item][2]
        except ValueError:
            print("No marking given")
        x = range(len(y))
        plt.plot(x, y, plot_mark, label=name)
    plt.legend()
    plt.show()

def main():
    # Demonstration
    test_list = [["blah", [1,2,3,4,5], "-"],
            ["test", [6,7,8,9,10], "-."],
             ["another", [2,5,12,18,6], ".-"]]
    plot(test_list)
    
if __name__ == "__main__":
    main()