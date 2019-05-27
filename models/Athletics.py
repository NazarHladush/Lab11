class Athletics:

    def __init__(self, max_athlete_count, name_kind_of_sports, availability_finish_line, average_duration, length):
        self.max_athlete_count = max_athlete_count
        self.name_kind_of_sports = name_kind_of_sports
        self.availability_finish_line = availability_finish_line
        self.average_duration = average_duration
        self.length = length

    def __del__(self):
        print("Destructor")

    def __repr__(self):
        return  str(self.__dict__)