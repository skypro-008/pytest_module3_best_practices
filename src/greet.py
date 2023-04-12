from datetime import datetime


def greet(name: str, greeting_reader) -> str:
    return f"{greeting_reader()}, {name}."


def greet_list(names: list[str], greeting_reader) -> list[str]:
    return [greet(name, greeting_reader) for name in names]


def read_greeting() -> str:
    current_time = datetime.now()
    if current_time.hour < 12:
        return "Good morning"
    elif 12 <= current_time.hour < 18:
        return "Good afternoon"
    else:
        return "Good evening"


def main() -> None:
    print(greet(input("Enter your name: "), read_greeting))
    print(greet_list(["John", "Jane", "Joe"], read_greeting))


if __name__ == "__main__":
    main()
