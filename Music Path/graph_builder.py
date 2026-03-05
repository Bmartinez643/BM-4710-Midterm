import networkx as nx

def build_graph(df):

    G = nx.Graph()

    songs = df.to_dict("records")

    # Nodes= songs and edges= similarity based on genre, bpm, year
    for song in songs:
        G.add_node(song['Title'], artist=song['Artist'])

    """Only connect songs that are close in the 
     dataset to limit edges and improve performance"""
    for i in range(len(songs)):

        for j in range(i+1, min(i+10, len(songs))):

            s1 = songs[i]
            s2 = songs[j]

            weight = 1

            # genre difference
            if s1['Top Genre'] != s2['Top Genre']:
                weight += 2

            # bpm difference
            weight += abs(s1['Beats Per Minute (BPM)'] - s2['Beats Per Minute (BPM)']) / 20

            # year difference
            weight += abs(s1['Year'] - s2['Year']) / 2

            G.add_edge(s1['Title'], s2['Title'], weight=weight)

    return G