from Chapter_1_3.complexity_timer import TestingTimer

timer = TestingTimer()
import random


#-------------------------------------------------------------------#
#                          Algo Testing Class                       #
#-------------------------------------------------------------------#
class AlgSorter:
    def bubble_sort(self, elements):
        changed = False
        for i in range(len(elements) - 1):
            if elements[i] > elements[i + 1]:
                elements[i], elements[i+1] = elements[i+1], elements[i]
                changed = True
        if changed:
            return self.bubble_sort(elements)
        return elements

    def merge_sort(self, elements):
        if len(elements) <= 1:
            return elements
        # Split the list in half
        mid = len(elements) // 2
        left = elements[:mid]
        right = elements[mid:]
        self.merge_sort(left) # Sort the left half
        self.merge_sort(right) # Sort the right half
        a, b, c = 0, 0, 0
        # Merge the two halves
        while a < len(left) and b < len(right):
            if left[a] < right[b]:
                elements[c] = left[a]
                a += 1
            else:
                elements[c] = right[b]
                b += 1
            c += 1
        # If there are remaining elements in the left half
        while a < len(left):
            elements[c] = left[a]
            a += 1
            c += 1
        # If there are remaining elements in the right half
        while b < len(right):
            elements[c] = right[b]
            b += 1
            c += 1
        return elements
    
    def insertion_sort(self, elements):
        for i in range(1, len(elements)):
            j = i - 1
            next_element = elements[i]
            while j >= 0 and elements[j] > next_element:
                elements[j + 1] = elements[j]
                j -= 1
            elements[j + 1] = next_element
        return elements


    def shell_sort(self, elements):
        distance = len(elements) // 2
        while distance > 0:
            for i in range(distance, len(elements)):
                temp = elements[i]
                j = i
                # Sort the sub list for this distance
                while j >= distance and elements[j - distance] > temp:
                    elements[j] = elements[j - distance]
                    j = j - distance
                elements[j] = temp
            # Reduce the distance for the next element
            distance = distance // 2
        return elements


    def selection_sort(self, elements):
        for fill_slot in range(len(elements) - 1, 0, -1):
            max_index = 0
            for location in range(1, fill_slot + 1):
                if elements[location] > elements[max_index]:
                    max_index = location
            elements[fill_slot],elements[max_index] = elements[max_index],elements[fill_slot]
        return elements

#-------------------------------------------------------------------#


def test_sort(category="bubble_sort", amt=10, avg_amt=100, can_print=True):
    sorter = AlgSorter()
    averages = []
    for x in range(1,amt+1):
        for y in range(avg_amt):
            random_list = [random.randint(1,1000) for y in range(x*100)]
            timer.start()
            match category:
                case "bubble_sort":
                    sorter.bubble_sort(random_list)
                case "insert_sort":
                    sorter.insertion_sort(random_list)
                case "merge_sort":
                    sorter.merge_sort(random_list)
                case "shell_sort":
                    sorter.shell_sort(random_list)
                case "selection_sort":
                    sorter.selection_sort(random_list)
            timer.stop()
        avg = timer.average_results()
        if can_print:
            print(f" {category} #{x}: {avg}")
        averages.append(avg)
        timer.clear()
    return averages