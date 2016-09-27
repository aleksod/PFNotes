state_dictionary = {'colorado': 'Denver', 'alaska': 'Juneau', 'california': 'Sacramento',
                      'georgia': 'Atlanta', 'kansas': 'Topeka', 'nebraska': 'Lincoln',
                      'oregon': 'Salem', 'texas': 'Austin', 'new york': 'Albany'}
usr_input = str(raw_input("enter a state's name: ")).strip().lower()
print state_dictionary.get(usr_input, 'No such state found in the database')
