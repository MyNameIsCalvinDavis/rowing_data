# rowing_data
Scripts that keep track of parsed rowing data

**_pace_parser.py_**

Plug in a 2K pace to create a small chart depicting other threshold workout paces, based on various metrics.

![image](/pictures/p2.png)

**_Rowing.ipynb_ & _Rowing_V2.ipynb_**

Upload a C2 season csv and breakdown basic data like HR, pace, etc over time. Oof, that's Ugly! This is what happens when you are your own customer

![image](/pictures/row_data.png)

In the first file, categorization of each workout is based on the "Comment" column, but in _Rowing_V2.ipynb_ this is calculated based on data retrieved from your most recent set of workouts, specifically delimited by 2K workouts over the season, and then workout categories are derived from that time. Here's an example of formatted data in the first version:

![image](/pictures/table.png)

Workout categorization in the second notebook is based on your last 2K time. So if you do a 2K on day 30 and day 90, days 0-30 will be categorized based on the first time, and days 31-90 based on the second, so you can see over time how your times have improved while keeping the category discrimination relevant to your fitness at the time of the workout. Doing this prevents an increase in fitness fuzzing previous data - if over a year your UT2 SS time decreases dramatically (10s), your previous UT1 sessions aren't automatically categorized into a different bracket based on your (current) fitness level, so an example UT1 workout (2:10) won't be categorized as a UT2 later because your split has improved over time.

The second go at tabularization and graphs can be seen below. In it we can see, for example, the average workout change between both categories of 2K (in this data I've only done one 2K workout)

![image](/pictures/T2.png)

![image](/pictures/R2.png)

![image](/pictures/R3.png)

We can see here that my UT2 splits and HR have increased, though the HR range is tighter than in the first half. This suggests that my fitness and technique is improving (tighter data), though I may be going too fast in my UT2 workouts, or otherwise losing efficiency on each stroke (higher HR).
