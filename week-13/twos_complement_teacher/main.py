"""Command-line entry point for the two's-complement teacher."""
import argparse
import sys
import lesson


def main() -> None:
    """Parse a teaching mode and report friendly input errors."""
    parser = argparse.ArgumentParser(description="Learn why two's complement works.")
    modes = parser.add_mutually_exclusive_group(required=True)
    for name in ("lesson", "why", "table", "quiz", "overflow"):
        modes.add_argument(f"--{name}", action="store_true")
    modes.add_argument("--subtract", nargs=2, type=int, metavar=("A", "B"))
    modes.add_argument("--negate", type=int, metavar="N")
    parser.add_argument("--bits", type=int, choices=(4, 8, 16), default=8)
    parser.add_argument("--no-pause", action="store_true")
    parser.add_argument("--no-color", action="store_true")
    args = parser.parse_args()
    color = sys.stdout.isatty() and not args.no_color
    try:
        if args.lesson:
            lesson.guided(args.bits, not args.no_pause, color)
        elif args.why:
            lesson.why(args.bits)
        elif args.subtract is not None:
            lesson.walkthrough(*args.subtract, args.bits, color)
        elif args.negate is not None:
            lesson.negate(args.negate, args.bits)
        elif args.table:
            lesson.table(args.bits)
        elif args.overflow:
            lesson.overflow_lesson(args.bits, color)
        else:
            lesson.quiz(args.bits)
    except ValueError as error:
        parser.error(str(error))
    except (EOFError, KeyboardInterrupt):
        print("\nPractice paused. Come back whenever you're ready.")


if __name__ == "__main__":
    main()
