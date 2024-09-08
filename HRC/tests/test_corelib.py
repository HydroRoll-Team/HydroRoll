from hrc import LibCore

cb = LibCore


def main():
    rule_pack = "example_rule_pack"
    result = cb.process_rule_pack(rule_pack)
    print(result)


if __name__ == "__main__":
    main()
