from .logger import update_log_files

update_log_files()


def main():
    from modellsteuerung_backend.main import main
    from asyncio import run
    run(main())


if __name__ == "__main__":
    main()
