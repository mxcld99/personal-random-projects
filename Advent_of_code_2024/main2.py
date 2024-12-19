def read_reports(path):
    with open(path) as f:
        l = f.readlines()
    reports=[]
    for line in l:
        levels = list(int(x) for x in line[:-1].split(' '))
        reports.append(tuple(levels))
    return reports

def check_report_is_safe(report):
    diffs = []
    comp_val = report[0]
    for level in report[1:]:
        diffs.append(comp_val-level)
        comp_val=level
    abs_sum = abs(sum(diffs))

    indiv_abs_sum = 0
    for diff in diffs:
        abs_diff = abs(diff)
        if not 1<=abs_diff<=3:
            return 0
        indiv_abs_sum+=abs_diff
    if indiv_abs_sum == abs_sum:
        return 1
    return 0

# Could just do initial function followed by multiple iterations of the original funnction on reports with one item removed.
def check_report_with_problem_dampener(report):
    initial_safety_check = check_report_is_safe(report)
    if initial_safety_check:
        return 1
    else:
        # testing safety by taking out each level
        report_len=len(report)
        for index in range(report_len):
            temp_report = report[:index]+report[index+1:]
            if check_report_is_safe(temp_report):
                return 1

    return 0

# # Test
# reports = [[1,2,3,4,5,6],# 1
#            [1,2,3,4,3,6,7,8],# 0
#            [3,6,7,10,11], # 1
#            [1,5,6,7,8,9], # 0
#            [8,6,5,4,2], # 1
#            [9,5,4,3]] # 0
# for report in reports:
#     print(check_report_is_safe(report))

# General
path_to_input = "input2.txt"
reports = read_reports(path_to_input)


# Part 1
safe_reports = 0
for report in reports:
    safe_reports += check_report_is_safe(report)

print('Part 1 answer: ',safe_reports)


# Part 2
safe_reports = 0
for report in reports:
    safe_reports += check_report_with_problem_dampener(report)

print('Part 2 answer: ',safe_reports)