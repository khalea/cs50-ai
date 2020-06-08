class Node():
    def __init__(self, movieID, personID):
        self.movieID = movieID
        self.personID = personID


class StackFrontier():
    def __init__(self):
        self.frontier = []

    def add(self, personID):
        self.frontier.append(personID)

    
    def contains_source(self, targetID):
       return any(personID.id == targetID for personID in self.frontier)

    def empty(self):
        return len(self.frontier) == 0

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            personID = self.frontier[-1]
            self.frontier = self.frontier[:-1]
            return personID


class QueueFrontier(StackFrontier):

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            personID = self.frontier[0]
            self.frontier = self.frontier[1:]
            return personID
    
    def peek(self):
        return self.frontier[0]
