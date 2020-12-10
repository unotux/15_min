required_files = ['README.txt', 'scenario.json', 'config.hat']
all_files = ['bla.html', 'lala.xsl']

#option1
def check_existing_files(required_files, all_files):
    missed_required_files = []
    for x in range(len(required_files)):
        if required_files[x] not in all_files:
            missed_required_files.append(required_files[x])
    print("Отсутствующие объекты:\n")
    for i in range(len(missed_required_files)):
        print(f"{missed_required_files[i]}\n")

#option2
def use_list_comprehension(required_files, all_files):
    missed_required_files = [i for i in required_files if i not in all_files]
    print(missed_required_files)


check_existing_files(required_files, all_files)
use_list_comprehension(required_files, all_files)
