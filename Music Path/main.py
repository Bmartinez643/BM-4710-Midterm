from data_loader import load_dataset
from graph_builder import build_graph
from algorithms import find_song_path, suggest_songs
from visualization import draw_path


def main():

    print("Loading dataset...")
    df = load_dataset("Spotify-2000.csv")

    print("Building song network...")
    G = build_graph(df)

    while True:

        print("\n--- Music Path Network ---")
        print("1. Find connection between two songs")
        print("2. Get song recommendations")
        print("3. Exit")

        choice = input("Choose option: ")

        # findthe connection path between two songs
        if choice == "1":

            song1 = input("Enter first song: ")
            song2 = input("Enter second song: ")

            path, distance = find_song_path(G, song1, song2)

            if path:

                print("\nConnection Path:\n")

                for i, song in enumerate(path):

                    if i == 0:
                        print(song)
                    else:
                        print("↓")
                        print(song)

                print("\nTotal weight:", distance)

                draw_path(G, path)

        # song recommendations based on genre, bpm, year
        elif choice == "2":

            song = input("Enter a song: ")

            suggestions = suggest_songs(df, song)

            print("\nSuggested Songs:\n")

            for s in suggestions:
                print(s[0])

        # to stop the program
        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please choose again.")


if __name__ == "__main__":
    main()