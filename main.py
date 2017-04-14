import core.game as game
import cli.ui as ui

my_game = game.Game()
my_game.start()
print(my_game.get_base())
my_ui = ui.CLI_UI(my_game.get_base())

while (my_game.running()):
    if(my_game.base_updated()):
        base = my_game.get_base()
        my_ui.update_base(base)

    # rendering
    context = my_game.get_context()
    my_ui.render(context)
    input = my_ui.get_input()
    my_game.update(input)
