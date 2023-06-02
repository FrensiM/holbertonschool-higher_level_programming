#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    x = "__"
    for item in dir(hidden_4):
        if x not in item:
            print(item)
