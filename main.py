def on_gesture_shake():
    basic.show_icon(IconNames.ANGRY)
    music.play_melody("- - - - - - - - ", 120)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)
