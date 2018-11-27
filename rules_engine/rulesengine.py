from .prep_objects import forgotpassword_prep as forgotpass_prep
from .prep_objects import search_prep as search


class RulesEngine:
    """
    This is the rules engine class which is used to detect tasks in json
    and assigning the task to the right object to process them
    """
    response = []
    taskid = ""

    def process_request(self, elements):
        self.response = []
        counter = 0
        my_element = ""
        for i in range(len(elements)):
            my_element = elements[i]
            self.taskid = my_element["id"]
            if self.taskid == "ForgotPassword":
                result = forgotpass_prep.ForgotPassword_Prep.reset_password(forgotpass_prep, my_element)
                self.response.append(result)

            elif self.taskid == "SetNewPassword":
                result = forgotpass_prep.ForgotPassword_Prep.reset_password(forgotpass_prep, my_element)
                self.response.append(result)

            elif self.taskid == "users":
                pass

            elif self.taskid == "search":
                result = search.Search_Prep.process_search(search, my_element)
                self.response.append(result)
                break

            elif self.taskid == "Signup":
                pass

            else:
                pass

        return self.response




