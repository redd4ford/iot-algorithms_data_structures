# How to use
1. clone this repository:
```
git clone https://github.com/redd4ford/iot-laboratory-works-algorithms-2020
```
* or simply download and extract it anywhere you wish;

2. open command prompt and switch the directory to **/lab-2-data-structures**:
```
cd iot-laboratory-works-algorithms-2020/lab-2-data-structures
```
* if you decided to download and extract it to, let us say, D:/projects, you would do it like that:
```
D:
```
```
cd projects/iot-laboratory-works-algorithms-2020/lab-2-data-structures
```


3. make sure you have Python 3+! then you must be able to run:
```
python lngpok.py
```

***

this program uses a custom LinkedList implementation to solve the LNGPOK problem. lngpok.in file is for input; it contains a one-line sequence of numbers (0 <= number <= 1000000). these numbers represent the values of cards that a player has. joker cards have 0 value and can be replaced with any number.

the algorithm determines the length of the longest sequence of consecutive cards you can make. the length is then written to lngpok.out file.

the algorithm works like this:
1. add numbers to the LinkedList as Nodes. for joker cards, we only count their amount and do not add them to the LinkedList.
2. merge sort the LinkedList. merge sort was used since it is considered as mostly used sorting algorithm for LinkedList.
3. order the items again since the indexes cannot be swapped during sorting.
4. iterate through the LinkedList, get the difference of two adjacent elements.
5. if it's greater than 2 (which means there is at least one gap in this consecutive sequence), we consider placing as many jokers as possible between those two items.
6. if jokers_left value is absurd (less than 0), we have to break the sequence and remember its length if it is max length.
7. if there are still jokers left or we have just added the last joker, we add the difference to current sequence length.
8. repeat this for the next iterations.
9. the result is the max sequence length.
