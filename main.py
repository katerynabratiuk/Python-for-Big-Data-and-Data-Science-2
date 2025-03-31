import app.io.input as ipt


def main():

    # read_input
    res = ipt.read_input()
    print(res)
    with open("data/res.txt", "a") as file:
        file.write(res)

    # read_file
    content = ipt.read_file("data/random_text.txt")
    print(content)
    with open("data/res.txt", "a") as file:
        file.write(content)

    # read_file_pd
    content_pd = ipt.read_file_pd("data/random_table.csv")
    print(content_pd)
    with open("data/res.txt", "a") as file:
        file.write(content_pd)


if __name__ == "__main__":
    main()
