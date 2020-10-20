# How to use
1. clone this repository:
```
git clone https://github.com/redd4ford/iot-laboratory-works-algorithms-2020
```
* or simply download and extract it anywhere you wish;

2. open command prompt and switch the directory to **/lab-1-insertion-merge-sort**:
```
cd iot-laboratory-works-algorithms-2020/lab-1-insertion-merge-sort
```
* if you decided to download and extract it to, let us say, D:/projects, you would do it like that:
```
D:
```
```
cd projects/iot-laboratory-works-algorithms-2020/lab-1-insertion-merge-sort
```


3. make sure you have Python 3+! then you must be able to run:
```
python main.py
```

***

this program shows you the results of insertion and merge sorts for each algorithm, it also shows some additional information, such as:
* execution time,
* swap counter,
* comparison counter.

counters represent the numbers of corresponding operations that occurred during the sorting process.

the list of objects is taken from *helicopter.csv* file. each row there represents a new object as a sequence of its properties' values separated by commas. the order is:
```
name,max_passengers,max_speed
```
you can edit this file with any text editor. add any amount of objects you want*
\* - *but if you want 1000 or more objects, perhaps you should edit the code and remove the output of the sorted array - you know, just in case. the corresponding lines in [main.py](https://github.com/redd4ford/iot-laboratory-works-algorithms-2020/blob/main/lab-1-insertion-merge-sort/main.py):*
```
20    info_printer.print_list(sorted_helicopters) # main.py
```
```
31    info_printer.print_list(sorted_helicopters) # main.py
```
comment or delete them if you do not want to see the sorted list.
