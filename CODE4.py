# Clock Angle
# There are 360 Longitudes on the Earth, which are equidistant vertical imaginary lines drawn on the Earth, separated by 1 degree each from center of the Earth. Period of the rotation of the Earth on its axis is 24 hours. All countries have their own official times and hence time zones. UTC is universal time coordinate which passes through 0 (Zero Degree) longitude. Time at a particular location on Earth can be calculated using period of the rotation of Earth and Longitude of that particular location. For example, Indian time zone IST (Indian standard Time) is located at 82.50E longitude. Hence, Indian time can be calculated as below: IST = UTC + (24/360)*82.5 = UTC + 5:30Hrs Now suppose we changed period of rotation of the earth using some imaginary power, this will change the time at every longitude on the earth. Calculate the smallest angle between hour and minute hand of the clock, which shows the difference of time at a particular longitude and the time at UTC i.e., we have to take smaller of the two angle formed between hour and minute hand.
# Constraints:
# To show the time difference on clock, 12-hour clock (as shown below) shall be used, irrespective of period of the earths rotation, for this question only.
# Input Format:
#  1. Period of the earth’s rotation in Hours (Integer only)
#  2. Value of Longitude up to 2 place of decimal
# Output Format:
# Smallest angle between hour and minute hand of the clock, which shows the difference between time at a particular longitude and time at UTC, up to 2 decimal places.
# Sample Input
# 24
# 82.50
# Sample Output
# 15.00
# Explanation:
# ﻿If period of rotation of earth is 24 hours then time at 82.5 degree longitude will be (24/360)*82.50 = 5:30 and minimum angle at this time between minute and hour hand will be 15 degree.

pr = int(input())
longitude = float(input())

period_of_rotation = float(pr)

    # Calculate time t
t = ((period_of_rotation / 360.0) * longitude)

h = int(t)
m = int((t - h) * 60)

    # Calculate angle between hour and minute hands
angle = ((h*30)+(m*1/2)) - (m * 6)

#     # Normalize the angle
if angle < 0:
    print(360-(angle+360))
else:
    print(f"{angle:.2f}")