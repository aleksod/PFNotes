# def repeat_list_of_file_line(file_name, line_num, num_copies):
#    '''
#    Input:  Str - path to file,
#            Int - number of line to copy from file,
#            Int - number of times to copy line into list
#    Output: List - filled with num_copies of line_num in file_name
#    '''
#    line = None
#    with open(file_name) as f:
#        for i, file_line in enumerate(f, 1):
#            if i == line_num:
#                line = file_line.strip()
#    if not line:
#        copies_of_line = 'There were not {} lines in the document'.format(line_num)
#    else:
#        copies_of_line = [line for _ in range(num_copies)]
#    return copies_of_line

def repeat_list_of_file_line(file_name, line_num, num_copies):

    def file_open(file_name, line_num):
        line = None
        with open(file_name) as f:
            for i, file_line in enumerate(f, 1):
                if i == line_num:
                    line = file_line.strip()
        return line

    line = file_open(file_name, line_num)

    def line_copier(line, num_copies):
        if not line:
            copies_of_line = 'There were not {} lines in the document'.format(line_num)
        else:
            copies_of_line = [line for _ in range(num_copies)]
        return copies_of_line

    print line_copier(line, num_copies)
    return line_copier(line, num_copies)

repeat_list_of_file_line('/Users/aleksod/Documents/PFRepos/PFNotes/scripts/test.txt',
20, 8)
