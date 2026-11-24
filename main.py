from pathlib import Path


def main() -> None:
    # Let the shine show what the cobbler did before his reply explains why.
    repair = "I picked up my boots today. The left had a new heel. Both toes shone."
    reply = "When I thanked the cobbler for the polish, he said, “They came in together.”"
    line = f"{repair} {reply}"
    if len(line) > 200:
        raise ValueError("The entry exceeds 200 characters.")

    output = Path("/output/entry.txt")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(line, encoding="utf-8")


if __name__ == "__main__":
    main()
