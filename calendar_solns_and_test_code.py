# 4.1.3.6
def isYearLeap(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) :
        return True
    return False

testData = [1900, 2000, 2016, 1987]
testResults = [False, True, True, False]
for i in range(len(testData)):
	yr = testData[i]
	print(yr,"->",end="")
	result = isYearLeap(yr)
	if result == testResults[i]:
		print("OK")
	else:
		print("Failed")

# 4.1.3.7

def isYearLeap(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) :
        return True
    return False

months_length = [31,28,31,30,31,30,31,31,30,31,30,31]
def daysInMonth(year, month):
    if isYearLeap(year) == True and month == 2:
        return 29
    return months_length[month-1]

testYears = [1900, 2000, 2016, 1987]
testMonths = [2, 2, 1, 11]
testResults = [28, 29, 31, 30]
for i in range(len(testYears)):
	yr = testYears[i]
	mo = testMonths[i]
	print(yr, mo, "->", end="")
	result = daysInMonth(yr, mo)
	if result == testResults[i]:
		print("OK")
	else:
		print("Failed")

# 4.1.3.8
import datetime

def isYearLeap(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) :
        return True
    return False

months_length = [31,28,31,30,31,30,31,31,30,31,30,31]
def daysInMonth(year, month):
    if isYearLeap(year) == True and month == 2:
        return 29
    return months_length[month-1]

#
# dayOfYear function utilized Python's datetime library
# Although there's a way to do this algorithmically using
# the doomsday algorithim, I decided to use the library
# since the library will likely run the algm for me
#
def dayOfYear(year, month, day):
    # check types
    if(type(year) is not int or type(month) is not int
        or type(day) is not int):
            print("invalid value type")
            return None
    # check invalid values
    if(month < 1 or month > 12 or day < 1
        or daysInMonth(year,month) < day
        or (isYearLeap(year) == False and month == 2 and day == 29)):
            print("invalid month and day configuration")
            return None
    # check year is valid. The smallest allowed year value
    # for the datetime class is 1 and the maximum allowed year
    # value for the datetime class is 9999
    if(year < 1 or year > 9999):
        print("invalid year")
        return None
    # Find the date, then .weekday() returns the day as a digit
    # Monday is 0 and Sunday is 6
    intDay = datetime.date(year, month, day).weekday()
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return days[intDay]

# test code
testData = [ [2000, 12, 31], [2020, 2, 29], [2019, 2, 29],
             [0, 1, 1], [10000, 1, 1], ["hi", 1, 1],
             [2015, 0, 1], [2015, 1, 35], [2000, 12.0, 31.5] ]

# test cases are indexed 0 to 8
# 0 and 1 are normal cases,
# the other cases test invalid inputs of different conditions
# case 2: "invalid month and day configuration"
# case 3: "invalid year"
# case 4: "invalid year"
# case 5: "invalid value type"
# case 6: "invalid month and day configuration"
# case 7: "invalid month and day configuration"
# case 8: "invalid value type"
testResults = [ "Sunday", "Saturday", None,
                None, None, None,
                None, None, None ]

for i in range(len(testData)):
    year = testData[i][0]
    month = testData[i][1]
    day = testData[i][2]
    result = dayOfYear(year, month, day)
    if testResults[i] == result:
        print("Test case number: ", i, "passed")
    else:
        print("Test case number: ", i, "failed")
