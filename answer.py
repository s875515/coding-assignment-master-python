import data1 as data
# import data2 as data
# import data3 as data

def exercise1(person, people):
  output = []
  for key in dir(data):
    value = getattr(data, key)
    if hasattr(value, 'is_team') and value.is_team and (person in get_people(value, [], {})):
      output.append(value)
  return output

def get_people(team, members = [], record = {}):
  if team.id in record:
    return []

  record[team.id] = True
  for membersValue in team.members:
    if membersValue.is_team:
      members + get_people(membersValue, members, record)
    else:
      members.append(membersValue)
  return members

print [t.displayname for t in exercise1(data.alice, data.people)]
print sorted(p.displayname for p in get_people(data.c_team))