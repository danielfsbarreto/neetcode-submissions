class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.current_page_index = 0

    def visit(self, url: str) -> None:
        self.current_page_index += 1
        self.history = self.history[:self.current_page_index]
        self.history.append(url)

    def back(self, steps: int) -> str:
        # while steps > 0 and self.current_page_index > 0:
        #     steps -= 1
        #     self.current_page_index -= 1
        self.current_page_index = max(0, self.current_page_index - steps)
        return self.history[self.current_page_index]

    def forward(self, steps: int) -> str:
        # while steps > 0 and self.current_page_index < len(self.history) - 1:
        #     steps -= 1
        #     self.current_page_index += 1
        self.current_page_index = min(len(self.history) - 1, self.current_page_index + steps)
        return self.history[self.current_page_index]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)