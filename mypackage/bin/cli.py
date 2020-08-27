from mypackage import datareader


def main():
    for msg in datareader.get_messages():
        print(msg)
