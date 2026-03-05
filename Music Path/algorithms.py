import networkx as nx


def find_song_path(G, song1, song2):
    """
    Finds the shortest weighted path between two songs
    using Dijkstra's algorithm
    """

    # This checks if songs exist in the graph
    if song1 not in G:
        print(f"'{song1}' not found in dataset.")
        return None, None

    if song2 not in G:
        print(f"'{song2}' not found in dataset.")
        return None, None

    try:

        temp_graph = G.copy()

        """ remove direct edge so algorithm finds a path 
         through other songs instead of just the direct connection """
        if temp_graph.has_edge(song1, song2):
            temp_graph.remove_edge(song1, song2)

        # Dijkstra's algorithm to find the shortest path and its total weight
        path = nx.dijkstra_path(temp_graph, song1, song2, weight="weight")
        distance = nx.dijkstra_path_length(temp_graph, song1, song2, weight="weight")

        return path, distance

    except nx.NetworkXNoPath:
        print("No connection found between these songs.")
        return None, None


def suggest_songs(df, song):
    """
    Recommend songs based on similarity in genre, BPM, and year.
    """

    row = df[df['Title'] == song]

    #if the song is not found in the dataset
    if row.empty:
        print(f"'{song}' not found in dataset.")
        return []

    row = row.iloc[0]

    candidates = []

    for _, other in df.iterrows():

        if other['Title'] == song:
            continue

        score = 0

        # genre similarity
        if other['Top Genre'] == row['Top Genre']:
            score += 2

        # BPM similarity
        if abs(other['Beats Per Minute (BPM)'] - row['Beats Per Minute (BPM)']) < 15:
            score += 1

        # year similarity
        if abs(other['Year'] - row['Year']) <= 5:
            score += 1

        candidates.append((other['Title'], score))

    # returns the 5 most similar songs based on the score
    candidates.sort(key=lambda x: x[1], reverse=True)

    return candidates[:5]