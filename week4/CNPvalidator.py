month_dict = {
    '01': ['January', 31],
    '02': ['February', 28],
    '03': ['March', 31],
    '04': ['April', 30],
    '05': ['May', 31],
    '06': ['June', 30],
    '07': ['July', 31],
    '08': ['August', 31],
    '09': ['September', 30],
    '10': ['October', 31],
    '11': ['November', 30],
    '12': ['December', 31]
}
district_dict = {
    '01': 'Alba',
    '02': 'Arad',
    '03': 'Argeș',
    '04': 'Bacău',
    '05': 'Bihor',
    '06': 'Bistrița-Năsăud',
    '07': 'Botoșani',
    '08': 'Brașov',
    '09': 'Brăila',
    '10': 'Buzău',
    '11': 'Caraș-Severin',
    '12': 'Cluj',
    '13': 'Constanța',
    '14': 'Covasna',
    '15': 'Dâmbovița',
    '16': 'Dolj',
    '17': 'Galați',
    '18': 'Gorj',
    '19': 'Harghita',
    '20': 'Hunedoara',
    '21': 'Ialomița',
    '22': 'Iași',
    '23': 'Ilfov',
    '24': 'Maramureș',
    '25': 'Mehedinți',
    '26': 'Mureș',
    '27': 'Neamț',
    '28': 'Olt',
    '29': 'Prahova',
    '30': 'Satu Mare',
    '31': 'Sălaj',
    '32': 'Sibiu',
    '33': 'Suceava',
    '34': 'Teleorman',
    '35': 'Timiș',
    '36': 'Tulcea',
    '37': 'Vaslui',
    '38': 'Vâlcea',
    '39': 'Vrancea',
    '40': 'București',
    '41': 'București - Sector 1',
    '42': 'București - Sector 2',
    '43': 'București - Sector 3',
    '44': 'București - Sector 4',
    '45': 'București - Sector 5',
    '46': 'București - Sector 6',
    '51': 'Călărași',
    '52': 'Giurgiu'
}


def validate_length(cnp: str) -> str:
    """
    Function to check if the entered cnp has a valid length
    :param cnp: the cnp that has to be checked
    :return: 'valid' in case it has the right length, otherwise 'invalid'
    """
    if len(cnp) == 13:
        return 'valid'
    return 'invalid'


def validate_numeric(cnp: str) -> str:
    """
    Function to check if the entered cnp is numeric
    :param cnp: the cnp that has to be checked
    :return: 'valid' in case it is numeric, otherwise 'invalid'
    """
    if cnp.isnumeric():
        return 'valid'
    return 'invalid'


def validate_first_digit(s: int) -> str:
    """
    Function to check if the first digit S of the CNP is valid (is 1, 2 .. or 9)
    :param s: the first digit S
    :return: 'valid' in case it is valid, otherwise 'invalid'
    """
    if 1 <= s <= 9:
        return 'valid'
    return 'invalid'


def validate_month(ll: str) -> str:
    """
    Function that validates the month, by searching in dictionary
    :param ll: the month LL
    :return: 'valid' in case it is valid, otherwise 'invalid'
    """
    if month_dict.get(ll) is None:
        return 'invalid'
    return 'valid'


def validate_day(zz: str, ll: str, aa: str, s: int) -> str:
    """
    Function to validate the day in which the person is born, additional check on bisect years (february has 29 days)
    :param zz: ZZ from cnp
    :param ll: LL from cnp
    :param aa: AA from cnp
    :param s: S from cnp
    :return: 'valid' if day is valid, otherwise 'invalid'
    """
    month_values = month_dict.get(ll)
    if 1 <= int(zz) <= month_values[1]:
        return 'valid'
    if month_values[0] == 'February':
        year = extract_year(aa, s)
        if int(year) % 4 == 0:
            if int(zz) == 29:
                return 'valid'
    return 'invalid'


def validate_district(jj: str) -> str:
    """
    Function to validate the district code, by searching in district_dict
    :param jj: JJ from CNP
    :return: 'valid' if district is valid, otherwise 'invalid'
    """
    if district_dict.get(jj) is None:
        return 'invalid'
    return 'valid'


def validate_nnn(nnn: str) -> str:
    """
    Function to validate the NNN code
    :param nnn: NNN from cnp
    :return: 'valid' if NNN is valid, otherwise 'invalid'
    """
    if 1 <= int(nnn) <= 999:
        return 'valid'
    return 'invalid'


def validate_control_digit(cnp: str) -> str:
    """
    Function that validates the control digit of the CNP, using a specific formula
    :param cnp: the cnp
    :return: 'valid' if control digit is valid, otherwise 'invalid'
    """
    result = 0
    control_number = '279146358279'
    for i in range(12):
        result = result + int(cnp[i]) * int(control_number[i])
    remainder = result % 11
    if remainder == 10:
        remainder = 1
    if remainder == int(cnp[12]):
        return 'valid'
    return 'invalid'


def extract_gender(s: int) -> str:
    """
    Function to identify the gender, requires validation of first digit of CNP (s)
    :param s: first digit of CNP
    :return: the gender
    """
    if s % 2 == 0 and s != 9:
        gender = 'female'
    elif s % 2 == 1 and s != 9:
        gender = 'male'
    else:
        gender = 'no gender'
    return gender


def extract_century(s: int) -> int:
    """
    Function to identify the century, requires validation of first digit of CNP (s)
    :param s: first digit of CNP
    :return: the century
    """
    if s == 1 or s == 2:
        century = 20
    elif s == 3 or s == 4:
        century = 19
    elif s == 5 or s == 6:
        century = 21
    else:
        century = 20  # persons with 7, 8, 9 as first digit are considered to be in the 20 century
    return century


def check_is_foreigner(s: int) -> str:
    """
    Function to check whether the person is foreigner or not
    :param s: first digit of CNP
    :return: the is_foreigner
    """
    if s == 7 or s == 8:
        is_foreigner = 'resident foreigner'
    elif s == 9:
        is_foreigner = 'foreigner'
    else:
        is_foreigner = 'not a foreigner'
    return is_foreigner


def extract_year(aa: str, s: int) -> str:
    """
    Function that extracts the year in which the person is born
    :param aa: AA from CNP
    :param s: S from CNP
    :return: the year
    """
    century = extract_century(s)
    year = (str(century - 1) + aa)
    return year


def extract_info_from_cnp(cnp: str) -> str:
    """
    Function that extracts some info about a person based on it's CNP
    :param cnp: the introduced CNP (has to be validated first)
    :return: the info about the person
    """
    gender = extract_gender(int(cnp[0]))
    is_foreigner = check_is_foreigner(int(cnp[0]))
    year = extract_year(cnp[1] + cnp[2], int(cnp[0]))
    return f"This person is {gender}, {is_foreigner}, born on {int(cnp[5] + cnp[6])}, " \
           f"{month_dict.get(cnp[3] + cnp[4])[0]}, {year}, " \
           f"in district {district_dict.get(cnp[7] + cnp[8])}"


def validate_cnp(cnp: str) -> str:
    """
    Function that calls al the validators and checks if the introduced CNP is valid
    :param cnp: the introduced CNP
    :return: 'valid' if it is valid, otherwise 'invalid'
    """
    if validate_length(cnp) == 'invalid':
        return 'invalid'
    if validate_numeric(cnp) == 'invalid':
        return 'invalid'
    if validate_first_digit(int(cnp[0])) == 'invalid':
        return 'invalid'
    if validate_month(cnp[3] + cnp[4]) == 'invalid':
        return 'invalid'
    if validate_day(cnp[5] + cnp[6], cnp[3] + cnp[4], cnp[1] + cnp[2], int(cnp[0])) == 'invalid':
        return 'invalid'
    if validate_district(cnp[7] + cnp[8]) == 'invalid':
        return 'invalid'
    if validate_nnn(cnp[9] + cnp[10] + cnp[11]) == 'invalid':
        return 'invalid'
    if validate_control_digit(cnp) == 'invalid':
        return 'invalid'
    return 'valid'


if __name__ == '__main__':
    my_cnp = input("Please enter a CNP: ")
    msg = validate_cnp(my_cnp)
    if msg == 'valid':
        print("The introduced CNP is valid.")
        print(extract_info_from_cnp(my_cnp))
    else:
        print("The introduced CNP is invalid.")
