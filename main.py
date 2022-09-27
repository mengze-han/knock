from utils import Utils as Du


class DataPlan:

    def __init__(self):
        self.data = Du.raw_data()
        self._version = self.data.get('version')
        self._name = self.data.get('name')
        self.tasks = self.data.get('tasks')

    def version(self):
        return self._version

    def name(self):
        return self._name

    def create(self, date, task):
        self.tasks.get(date).append(task)
        Du.write(self.data)
        return self.query(date)

    def update(self, date, index, task):
        self.tasks.get(date)[int(index)] = task
        Du.write(self.data)
        return self.query(date)

    def delete(self, date, index):
        self.tasks.get(date).pop(int(index))
        Du.write(self.data)
        return self.query(date)

    def query(self, date):
        print(f"{date} plan: ")
        return self.tasks.get(date)


class Gtd:
    CREATE_LENGTH = 3
    UPDATE_LENGTH = 4
    DELETE_LENGTH = 3
    READ_LENGTH = 2

    CREATE_SIG = 'c'
    READ_SIG = 'l'
    UPDATE_SIG = 'u'
    DELETE_SIG = 'd'

    def __init__(self):
        self.data_plan = DataPlan()
        self.welcome()

    def welcome(self):
        print(f"welcome {self.data_plan.name()} version {self.data_plan.version()}")

    def run(self):
        pass

    def console(self):
        while True:
            command = input(">>> ").split(' ')
            if len(command) < 2:
                print("ERROR")
                continue
            date = Du.data_map(command[0].lower())
            operator = command[1]
            print(operator == self.READ_SIG)
            if operator == self.READ_SIG:
                res = self.data_plan.query(date)
            elif operator == self.CREATE_SIG:
                msg = command[-1]
                res = self.data_plan.create(date, msg)
            elif operator == self.UPDATE_SIG:
                index = command[2]
                msg = command[3]
                res = self.data_plan.update(date, index, msg)
            elif operator == self.DELETE_SIG:
                res = self.data_plan.delete()

            print(res)


if __name__ == "__main__":
    gtd = Gtd()
    gtd.console()
