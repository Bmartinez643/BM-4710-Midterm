import networkx as nx


def find_song_path(G, song1, song2):
    """
    Finds the shortest weighted path between two songs
    using Dijkstra's algorithm.
    """

    # Check if songs exist in the graph
    if song1 not in G:
        print(f"'{song1}' not found in dataset.")
        return None, None

    if song2 not in G:
        print(f"'{song2}' not found in dataset.")
        return None, None

    try:

        # Make a temporary copy of the graph
        temp_graph = G.copy()

        # Remove direct edge if it exists so we see intermediate songs
        if temp_graph.has_edge(song1, song2):
            temp_graph.remove_edge(song1, song2)

        # Run Dijkstra
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

    if row.empty:
        print(f"'{song}' not found in dataset.")
        return []

    row = row.iloc[0]

    candidates = []

    for _, other in df.iterrows():

        if other['Title'] == song:
            continue

        score = 0

        # Genre similarity
        if other['Top Genre'] == row['Top Genre']:
            score += 2

        # BPM similarity
        if abs(other['Beats Per Minute (BPM)'] - row['Beats Per Minute (BPM)']) < 15:
            score += 1

        # Year similarity
        if abs(other['Year'] - row['Year']) <= 5:
            score += 1

        candidates.append((other['Title'], score))

    # Sort by best score
    candidates.sort(key=lambda x: x[1], reverse=True)

    return candidates[:5]