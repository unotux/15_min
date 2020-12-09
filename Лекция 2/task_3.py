def check_existing_files(required_files, all_files):
    missed_required_files = []
    for x in range(len(required_files)):
        if required_files[x] not in all_files:
            missed_required_files.append(required_files[x])
    print("Отсутствующие объекты:\n")
    for i in range(len(missed_required_files)):
        print(f"{missed_required_files[i]}\n")


required_files = ['README.txt', 'scenario.json', 'config.hat']
all_files = ['bla.html', 'lala.xsl']

check_existing_files(required_files, all_files)
