import copy

def reading(file_name):
    file = open(file_name)
    array = file.read().splitlines()
    file.close()
    return array


def format_answers(groups_answers):
    formated_answers = []
    formated_groups_answer = []
    for group_answers in groups_answers:
        if group_answers:
            formated_groups_answer.append(group_answers)
        else:
            formated_answers.append(copy.deepcopy(formated_groups_answer))
            formated_groups_answer.clear()
    formated_answers.append(formated_groups_answer)
    return formated_answers


def count_yes_answers_anyone(group):
    return len(set(''.join(group)))


def count_total_match_answers_anyone(groups):
    count = 0
    for group in groups:
        count += count_yes_answers_anyone(group)
    return count


def count_yes_answers_everyone(group):
    match_answers = set(group[0])
    for answers in group[1:]:
        match_answers &= set(answers)
    return len(match_answers)


def count_total_match_answers_everyone(groups):
    count = 0
    for group in groups:
        count += count_yes_answers_everyone(group)
    return count


lines = reading("inputs.txt")
groups_answers = format_answers(lines)
print("puzzle 1 =", count_total_match_answers_anyone(groups_answers))
print("puzzle 2 =", count_total_match_answers_everyone(groups_answers))
