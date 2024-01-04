import json
import datetime


class project:
    def __init__(self, id:int, name:str) -> None:
        self.id = id
        self.name = name

    @classmethod
    def from_dict(cls, dict_project):
        return cls(dict_project['name'])

    def to_dict(self) -> dict:
        return {'id': self.id,
                'name': self.name}

class entry:
    def __init__(self, project:project, description:str) -> None:
        self.project = project
        self.description = description
    
    @classmethod
    def from_dict(cls, dict_entry):
        return cls(project(dict_entry['project']),
                   dict_entry['description'])
    
    def to_dict(self) -> dict:
        return {'project_id': self.project.id,
                'description': self.description}


class work_date:
    def __init__(self, date:datetime.date = datetime.datetime.today().date()) -> None:
        self.date = date
        self.entrys = []

    @classmethod
    def from_dict(cls, raw_data:dict):
        new_work_date = cls(datetime.datetime.strptime(raw_data['date'], "%Y-%m-%d").date())
        for e in raw_data['entrys']:
            new_work_date.add_entry(entry.from_dict(e))

    def add_entry(self, entry:entry) -> None:
        self.entrys.append(entry)

    def to_dict(self) -> dict:
        dict_entrys = []
        for e in self.entrys:
            dict_entrys.append(e.to_dict())
        return {'date': self.date.strftime("%Y-%m-%d"),
                'entrys': dict_entrys}

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
        projects_data = []
        for d in self.main_data:
            dict_data.append(d.to_dict())
        with open(location, 'w') as file:
            json.dump({'main_data':dict_data,
                       }, file)


new_data = data()

for i in range(5):
    new_date = work_date(datetime.datetime.date(datetime.datetime.today()) + datetime.timedelta(days=i))
    new_project = project(f'project{i+1}')
    for j in range(10):
        new_entry = entry(new_project, f'this is disc{(i+1)*j}')
        new_date.add_entry(new_entry)
    new_data.add_date(new_date)

new_data.save_data('test.json')