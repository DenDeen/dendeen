from manim import *


class AsciiArtGreeting(Scene):
    def construct(self):
        full_message = """
                      o/
        Hello there!  /|
                      / \\
        """


        ascii_art_text_mobject = Text(
            full_message,
            font="Monospace",  # Crucial for ASCII art alignment!
            font_size=40,
            line_spacing=0.8,
            color=WHITE,
        )

        # Center the Mobject
        ascii_art_text_mobject.move_to(ORIGIN)

        # --- Animation Style: Slower Write ---
        self.play(Write(ascii_art_text_mobject), run_time=4.5)  # Adjusted run_time

        # Keep it on screen
        self.wait(2.5)
