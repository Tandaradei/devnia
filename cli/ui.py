import json


class CLI_UI:

    def __init__(self, base):
        self.base = json.loads(base)

    def update_base(self, base):
        self.base = json.loads(base)

    def render_world(self):
        tiles = self.base["world"]["tiles"].split(',')
        for tile in tiles:
            print(tile)

    def render(self, context):
        self.render_world()
        print(context)

    def get_input(self):
        raw_input = input()
        formatted_input = format_input(raw_input)
        return formatted_input

    def format_input(self, raw_input):
        formatted_input = raw_input
        return formatted_input

