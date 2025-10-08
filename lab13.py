class BubbleSorter:
    def __init__(self,data):
        self.data = data

    def show_data(self):
        print(",".join(map(str,self.data)))

    def bubble_sort(self):
        n = len(self.data)
        for i in range(n - 1):
            for j in range(n - i - 1):
                if self.data[j] > self.data[j+1]:
                    self.data[j],self.data[j+1] = self.data[j+1],self.data[j]

if __name__=="__main__":
    data = [64,34,25,12,22,11]
    sorter = BubbleSorter(data)

    print("Before sorting:")
    sorter.show_data()
    sorter.bubble_sort()
    print("After sorting:")
    sorter.show_data()
       
        