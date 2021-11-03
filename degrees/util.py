class Node():
    def __init__(self, id, parent, movie_id):
        self.id =id
        self.parent = parent
        self.movie_id = movie_id


class StackFrontier():

    frontier_set = set()

    def __init__(self):
        self.frontier = []

    def add(self, node):
        self.frontier.append(node)
        self.frontier_set.add(node.id)

    def contains_id(self, id):
        return id in self.frontier_set

    def empty(self):
        return len(self.frontier) == 0

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[-1]
            self.frontier = self.frontier[:-1]
            self.frontier_set.remove(node.id)
            return node


class QueueFrontier(StackFrontier):

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[0]
            self.frontier = self.frontier[1:]
            self.frontier_set.remove(node.id)
            return node
