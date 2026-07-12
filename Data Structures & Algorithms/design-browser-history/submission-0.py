'''
BrowserPage respresenting the Current page: 
- current page value 
- pointer to the previous page 
- pointer to the next page

visit:  
1. From the last visited page
    a. set the next  pointer for that Browser page to the new page the user just visited
    b. set our current visited page to the new page
back:
1. Check if steps is > than the amount of pages we've visited 
    a. If yes then move back to the beginning of the history 
    b. If no then move back that amount of steps 
forward:
    1. Check if steps is > than size of our history 
        a. if yes then move to the last possible page
        b. if no move x steps forward 
'''

class BrowserHistory:
    class BrowserPage:
        def __init__(self, url, prev=None, next=None):
            self.url = url
            self.prev= prev
            self.next = next


    def __init__(self, homepage: str):
        self.currentPage = self.BrowserPage(homepage)

    def visit(self, url: str) -> None:
        self.currentPage.next = self.BrowserPage(url, self.currentPage, None)
        self.currentPage = self.currentPage.next
        return
            

    def back(self, steps: int) -> str:
        backStepsTaken = 0
        while self.currentPage.prev and backStepsTaken != steps:
            self.currentPage = self.currentPage.prev
            backStepsTaken += 1
        
        return self.currentPage.url
        

    def forward(self, steps: int) -> str:
        forwardStepsTaken = 0
        while self.currentPage.next and forwardStepsTaken != steps:
            self.currentPage = self.currentPage.next
            forwardStepsTaken += 1
        return self.currentPage.url


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)


## Doubly linked list 



'''
Explanation:
BrowserHistory browserHistory = new BrowserHistory("neetcode.com");
browserHistory.visit("google.com");       // You are in "neetcode.com". Visit "google.com"
browserHistory.visit("facebook.com");     // You are in "google.com". Visit "facebook.com"
browserHistory.visit("youtube.com");      // You are in "facebook.com". Visit "youtube.com"
browserHistory.back(1);                   // You are in "youtube.com", move back to "facebook.com" return "facebook.com"
browserHistory.back(1);                   // You are in "facebook.com", move back to "google.com" return "google.com"
browserHistory.forward(1);                // You are in "google.com", move forward to "facebook.com" return "facebook.com"
browserHistory.visit("linkedin.com");     // You are in "facebook.com". Visit "linkedin.com"
browserHistory.forward(2);                // You are in "linkedin.com", you cannot move forward any steps.
browserHistory.back(2);                   // You are in "linkedin.com", move back two steps to "facebook.com" then to "google.com". return "google.com"

currentPage = google
visual representation of the history = [neetcode, google,facebook,linkedin]
'''