import argparse


def main():
    parser = argparse.ArgumentParser(description="Greet a user by name.")
    parser.add_argument("name", type=str, help="The name of the user")
    args = parser.parse_args()

    print(f"Hello, {args.name}!")

# if __name__ == "__main__":
#     main()
