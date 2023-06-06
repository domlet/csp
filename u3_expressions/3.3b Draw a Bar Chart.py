# On the last test, Tim, Sam, Sue, and Ann scored 31,  21, 35, and 25 respectively. Create 4 variables for above test scores and use them to draw a bar chart as shown below.  Each "*" represents  1.
# (Don't type "*" 31 times!  Don’t use a loop; use string multiplication instead AND use f-string formatting.)

tim_score = 31
sam_score = 21
sue_score = 35
ann_score = 25

tim_chart = 31 * '*'
sam_chart = 21 * '*'
sue_chart = 35 * '*'
ann_chart = 25 * '*'

print(f"""
Tim: {tim_chart}
Sam: {sam_chart}
Sue: {sue_chart}
Ann: {ann_chart}""")
