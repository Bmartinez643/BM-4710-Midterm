import networkx as nx
import matplotlib.pyplot as plt


def draw_path(G, path):
    """
    Draw the connection path between songs.
    Only the songs in the discovered path will be shown.
    """

    # Create a subgraph containing only the path nodes
    subgraph = G.subgraph(path)

    pos = nx.shell_layout(subgraph)

    # Draw nodes
    nx.draw_networkx_nodes(
        subgraph,
        pos,
        node_color="lightblue",
        node_size=2000
    )

    # Draw edges
    nx.draw_networkx_edges(subgraph, pos, width=2)

    # Draw song titles as labels
    nx.draw_networkx_labels(
        subgraph,
        pos,
        font_size=8
    )

    # Draw weights on edges
    edge_labels = nx.get_edge_attributes(subgraph, "weight")
    nx.draw_networkx_edge_labels(subgraph, pos, edge_labels=edge_labels)

    plt.title("Song Connection Path")

    plt.axis("off")

    plt.show()