 Problem Statement for Never3Steps


Problem Statement
    	
As usual in many counting problems, you are standing on the point (0, 0) and you want to reach the point (X, Y) - that is, the point X steps east and Y steps north from your current location.

You move by taking steps. Each step must lead either east or north.

There is one extra rule tonight: along your way, you are not allowed to take exactly three steps in a row in the same direction. Fewer is good, more is also good, only exactly three is bad.

Count all valid ways of reaching the goal. Return that count modulo 10^9 + 7.

 
Definition
    	
Class:	Never3Steps
Method:	count
Parameters:	int, int
Returns:	int
Method signature:	int count(int X, int Y)
(be sure your method is public)
    
 
Constraints
-	X will be between 0 and 1000, inclusive.
-	Y will be between 0 and 1000, inclusive.
 
Examples
0)	
    	
2
2
Returns: 6
All six paths from (0, 0) to (2, 2) are valid.
1)	
    	
3
3
Returns: 14
Using 'N' for a step north and 'E' for a step east, the valid paths include "NENENE" and "EENENN" while the invalid paths include "NNNEEE" and "ENNNEE".
2)	
    	
0
7
Returns: 1
The only valid path consists of seven consecutive steps north. Seven is not three, so this is a valid path.
3)	
    	
10
2
Returns: 45
As we'll only take a total of two steps north, we don't have to worry about making three consecutive steps north. We just need to make sure we'll never make exactly three consecutive steps east.

Each valid path can be described as follows: "x steps east, step north, y steps east, step north, z steps east", where x+y+z = 10 and none of them equals 3. We can easily count that there are 45 such paths.

4)	
    	
0
0
Returns: 1
There's exactly one valid way to get from (0, 0) to (0, 0): take no steps.
