# LINE_UP = '\033[1A'

# def print_prompt_box(prompt, prompt_input=False, valid_inputs=""):
#     """Assumes the cursor is at the bottom of the screen,
#     located on the bottom line, where input takes place"""
#     print(LINE_UP * 2)
#     print(prompt, end="\n\n")
#     if prompt_input:
#         if valid_inputs == "":
#             print("ERROR in print_prompt_box()")
#         inp = input(">>> ")
#         while inp not in valid_inputs:
#             print(LINE_UP * 2)
#             print("Try again. " + prompt)
#         return inp