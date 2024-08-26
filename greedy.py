# coding=utf-8
# {} means set, {} costs less time compared with set()
states = {'mt', 'wa', 'or', 'id', 'nv', 'ut', 'ca', 'az', 'mt'}
radio_station = dict()
radio_station['kone'] = {'id', 'nv', 'ut'}
radio_station['ktwo'] = {'wa', 'id', 'mt'}
radio_station['kthree'] = {'or', 'nv', 'ca'}
radio_station['kfour'] = {'nv', 'ut'}
radio_station['kfive'] = {'ca', 'az'}

final_stations = set()
while states:
    best_station = None
    covered_states = set()
    for station, state in radio_station.items():
        covered = states & state
        if len(covered) > len(covered_states):
            best_station = station
            covered_states = covered
    states -= covered_states
    final_stations.add(best_station)
print(final_stations)
