# What is it?
Hello :v: This is a laboratory work on object-oriented programming. My friend and I slightly modified the task. But you can also check out the original task below.
# Original task
1. Create a class `Organizer` whose objects are Callable (for this, you need to describe the call method) and provide the ability to save and read records related to a specific date and time. When creating an object, the name of the file where the records will be stored is passed.

   For example: `lessons_timetable = Organizer("lessons.txt")`. If a file with such a name exists, the program should continue to append to it, rather than creating a new one. To save a record, the object is called with the following parameters: `date`, `start_time`, `end_time`, `main_message`, `additional_message` (optional parameter), for example: `lessons_timetable("10/02/2024", "10:10:00", "11:30:00", "00P lessons", "I must prepare 2 tasks")`.
   If the last two parameters are not passed, it means that a request for reading records is being made, with the following options:

      * The date parameter is passed in the form of `day/month/year`, for example, `lessons_timetable("10/10/2023")`: then all records for a specific day are displayed.

      * Two parameters are passed: `date and time`, for example, `lessons_timetable("10/02/2024", "10:30:11")`: then all records for the date whose time overlaps with the specified time are displayed.

      * Three parameters are passed: `date`, `start_time`, and `end_time`, for example, `lessons_timetable("18/02/2024", "9:40:11", "15:50:00")`: all records for the date whose time overlaps with the specified time interval are displayed.

2. For the date and time fields, describe descriptor classes that also need to validate the correctness of the entered data. Each type of incorrect data entry should generate a ValueError exception with the corresponding message, in particular:

      * If an incorrect date is entered (for example: "78/15/2024"), the message should be something like: "Incorrect date value".

      * If an incorrect time is entered (for example: "54:30:11"), the message should be: "Incorrect time value".

      * Other cases at your discretion.

3. If the object is passed a parameter in the form of `month1/year1:month2/year2`, the program should display a textual representation of all the days of the months in the specified interval, with the number of records for each specific day in square brackets next to each date, and the total number of records for the month in parentheses next to the name of the month and year, for example: `lessons_timetable("10/2023:11/2023")`, for example:
```
                   October 2023 (25)
   Mo      Tu      We      Th      Fr      Sa      Su
                                                    1
    2[7]    3       4       5       6       7       8
    9      10[1]   11      12      13      14      15
   16      17      18      19      20[13]  21      22
   23      24      25[3]   26      27[2]   28      29
   30      31

                   November 2023 (0)
   Mo      Tu      We      Th      Fr      Sa      Su
                    1       2       3       4       5
    6       7       8       9      10      11      12
   13      14      15      16      17      18      19
   20      21      22      23      24      25      26
   27      28      29      30
```
