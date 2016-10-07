def create_report(file_path):
    counts_dict = {'sentences': 0, 'words': 0, 'characters': 0}
    with open(file_path) as txt_file:
        for line in txt_file:
            update_counts(line, counts_dict)
    return counts_dict

def update_counts(line, counts_dict):
    counts_dict["sentences"] += len(line.split('.'))
    counts_dict["words"] += len(line.split())
    counts_dict["characters"] += len(line)

print create_report('/Users/aleksod/PFRepos/PFNotes/scripts/test.txt')
