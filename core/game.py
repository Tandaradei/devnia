import json
import core.debug as debug

class Game:
    
    def __init__(self):
        self.last_input = ""
        self.context = ""
        self.is_running = False
        self.base = '{"world": {"tiles":"4,4,1,4,5,5,4,4"}}'
        self.was_base_updated = False

    def start(self):
        self.is_running = True
        self.context = '{"running": true}'

    def base_updated(self):
        return self.was_base_updated

    def get_base(self):
        return self.base

    def running(self):
        return self.is_running

    def get_context(self):
        return self.context

    def update(self, input):
        if(input == "q"):
            self.is_running = False
        self.last_input = input
