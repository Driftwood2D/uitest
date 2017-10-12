def test():
    # Set the window title.
    Driftwood.window.title("Driftwood 2D - UI Test #2")

    # Load the widgets.
    a = Driftwood.script["stdlib/widget.py"].load("widgets/menu1.json")

    print(a)

