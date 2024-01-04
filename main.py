import json
import datetime


class project:
    def __init__(self, name:str) -> None:
        self.name = name

    def to_dict(self) -> dict:
        return {'name': self.name}

class entry:
    def __init__(self, project:project, description:str) -> None:
        self.project = project
        self.description = description
    
    @classmethod
    def from_dict(cls, dict_entry):
        return cls(project(dict_entry['project']),
                   dict_entry['description'])
    
    def to_dict(self) -> dict:
        return {'project': self.project,
                'description': self.description}


class work_date:
    def __init__(self, date:datetime.date = datetime.datetime.date(datetime.datetime.today())) -> None:
        self.date = date
        self.data = []

    @classmethod
    def from_dict(cls, raw_data:dict):
        new_work_date = cls(raw_data['date'])
        for e in raw_data['entrys']:
            new_work_date.add_project(entry.from_dict(e))

    def add_project(self, entry:entry) -> None:
        self.data.append(entry)

    def get_dict(self) -> dict:
        return {'date': self.date,
                'entrys': self.data}


class data:
    def __init__(self) -> None:
        self.main_data = []

    @classmethod
    def from_file(cls, location):
        with open(location, 'r') as file:
            json_data = json.load(file)
        new_class = cls()
        for d in json_data:
            cls.add_date(work_date.from_dict(d))
        return new_class

    def add_date(self, date:work_date) -> None:
        if date in self.main_data:
            print('date already exists')
        else:
            self.main_data.append(date)

    def save_data(self, location):
        dict_data = []
        for d in self.main_data:
            dict_data.append(d.get_dict())
        with open(location, 'w') as file:
            json.dump(dict_data, file)


my_data = [
    {'date':[
        {{'name': 'project'}:'discription'},
        {{'name': 'project1'}:'discription'}
    ]},
]
