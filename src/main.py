from src.call.work_with_data import DataWork
from src.settings import settings


def main():
    obj = DataWork(settings)
    obj.insert_data(2)
    obj.read_data(flag=True)


if __name__ == '__main__':
    main()

