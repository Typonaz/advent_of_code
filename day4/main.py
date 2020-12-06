import re

def reading(file_name):
    file = open(file_name)
    array = file.read().splitlines()
    file.close()
    return ordonat_passports(array)



def ordonat_passports(passports):
    ordonated_passports = []
    passport = ""
    for line in passports:
        if line:
            passport += (line + " ")
        else:
            ordonated_passports.append(passport)
            passport = ""
    return ordonated_passports


def parse_passport(passport):
    parsed_passport = []
    for element in passport.split():
        parsed_passport.append(element.split(':'))
    return parsed_passport

def valid_passport(parsed_passport):
    count = 0
    for entry in parsed_passport:
        if entry[0] in REQUIRED_FIELDS:
            count += 1
    return count == len(REQUIRED_FIELDS)


def valid_passports(passports):
    valid_passports = []
    for passport in passports:
        if valid_passport(parse_passport(passport)):
            valid_passports.append(passport)
    return valid_passports


def valid_byr(byr):
    return len(byr) == 4 and 1920 <= int(byr) <= 2002


def valid_iyr(iyr):
    return len(iyr) == 4 and 2010 <= int(iyr) <= 2020


def valid_eyr(eyr):
    return len(eyr) == 4 and 2020 <= int(eyr) <= 2030


def valid_hgt(hgt):
    return (hgt[-2:] == "in" and 59 <= int(hgt[:-2]) <= 76) or (hgt[-2:] == "cm" and 150 <= int(hgt[:-2]) <= 193)


def valid_hcl(hcl):
    return bool(re.match('#[0-9a-f]{6}$', hcl))


def valid_ecl(ecl):
    return ecl in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]


def valid_pid(pid):
    return bool(re.match('[0-9]{9}$', pid))


def valid_entry(entry_name, entry):
    if entry_name == "byr":
        return valid_byr(entry)
    if entry_name == "iyr":
        return valid_iyr(entry)
    if entry_name == "eyr":
        return valid_eyr(entry)
    if entry_name == "hgt":
        return valid_hgt(entry)
    if entry_name == "hcl":
        return valid_hcl(entry)
    if entry_name == "ecl":
        return valid_ecl(entry)
    if entry_name == "pid":
        return valid_pid(entry)
    return True


def valid_passport_fields(parsed_passport):
    for entry in parsed_passport:
        if not valid_entry(entry[0], entry[1]):
            return False
    return True


def count_valid_passports_fields(passports):
    count = 0
    for passport in passports:
        if valid_passport_fields(parse_passport(passport)):
            count += 1
    return count


REQUIRED_FIELDS = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
passports = reading("inputs.txt")
valid_passports = valid_passports(passports)
print("puzzle 1 =", len(valid_passports))

print("puzzle 2 =", count_valid_passports_fields(valid_passports))
