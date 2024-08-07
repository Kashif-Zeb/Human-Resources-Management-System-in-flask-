from blinker import Namespace

my_signals = Namespace()

user_logged_in = my_signals.signal("before-request")
