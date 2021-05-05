class Poll:
    def __init__(self, question, *args):
        self._id = poll_id
        self._question = question
        self._votes = []
        self._args = args
        self._active = True
        for option in options:
            self._votes[] = []

    def get_id(self):
        return self._id

    def get_question(self):
        return self._question

    def get_votes(self):
        return self._votes

    def add_vote(self, option, voter):
        if option in self._votes.keys(): 
            self._votes[option].append(voter)
            return True
        else:
            return False

    def set_id(self):
      self

    def deactivate(self):
        self._active = False

    def isActive(self):
        return self._active