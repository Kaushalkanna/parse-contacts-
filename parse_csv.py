import csv
import re

csv_file = 'contacts_final.csv'
num = ''
final_list = []


def validate(number):
    if number and len(number) > 10:
        if '-' in number:
            number = number.replace('-', '')
        if ' ' in number:
            number = number.replace(' ', '')
        if number.startswith('91') or number.startswith('+91') or number.startswith('?') or not number.startswith(
                '040') or not number.startswith('08457'):
            number = number[-10:]
        if '.' in number:
            number = number.split('.')[0]
        number = re.sub("[^0-9]", "", number)
    return number


with open(csv_file, 'rU') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        if row:
            if ',' in row[0]:
                for ele in row[0].split(','):
                    if ele:
                        parsed_data = validate(ele.strip())
            else:
                num = row[0].strip()
                parsed_data = validate(num)
            if len(parsed_data) == 10:
                final_list.append(parsed_data)
    final = (list(set(final_list)))
    with open('final_parsed_csv.csv', 'w', newline='') as myfile:
        wr = csv.writer(myfile)
        for element in final:
            wr.writerow([element])
