class Option:
    def __init__(self, prompt: str, action: str):
        self.prompt = prompt
        self.action = action
 # Option class represents a selectable option in a menu, with a prompt and an associated action.
    def get_prompt(self) -> str:       # -> str: return type for function
        return self.prompt
    def get_action(self) -> str:
        return self.action
    def __str__(self) -> str:
        return "Prompt {prompt}, Action {action}".format(
            prompt=self.prompt, action=self.action
        ) # .format(): insert values into string
          # __str__(): same as toString() in Java