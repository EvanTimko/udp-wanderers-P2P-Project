# Software Engineering
## Non-functional and Functional Requirements of [Expense Tracker]
### Sabrina Krueger, Nigel Jennings, Jada Hudson, Gustavo Lopez, Keyonte Jackson
----------------------
----------------------


1. **The system must allow users to create an account for authentication and privacy**
  - _The system should take user input for:_
    - Email
    - Username (check if its unique with all other accounts)
    - Password
      - The password should contain at least 8 characters
      - The password should use at least 3 of the following:
      - Uppercase characters
      - Lowercase characters
      - Numeric characters
      - Special characters
  - _The system should send a verification email to the user within 5 minutes when the user finishes the account sign up(and clicks the next button)_
  - _[or] The system should allow users to connect their Google account_
    - https://developers.google.com/identity/sign-in/web/sign-in
----------------
2. **The system must allow the user to enter in goals for how they want to save and spend money**
  - _The system should ask the user to create weekly/monthly goals and create yearly goals based on the users previous goals(if less than 3 months of previous goals, yearly goal will display(NOT ENOUGH INFORMATION))_
  - _The system should list categories:_
    - Housing
    - Transportation
    - Food
    - Utilities
    - Insurance
    - Medical
    - Saving/Investments/Debt Payments
    - Personal(‘wants’/impulses)
    - Entertainment
    - Miscellaneous
  - _The user should input integers for spending goals._
  ----------------
3. **The system must allow users to manually input their spendings**
  - _After logging in, the system should prompt the user with a question : “Do you want to add spending?”_
  - _If the user enters yes, the system should let the user input a real number._
  - _The system should let user input type of expense based on categories:_
    - Housing
    - Transportation
    - Food
    - Utilities
    - Insurance
    - Medical
    - Saving/Investments/Debt Payments
    - Personal(‘wants’/impulses)
    - Entertainment
    - Miscellaneous
----------------
4. **The system must allow users to customize the settings to their liking**
  - The system should display various menus as well as the version of the system
  - The system can include the following in settings:
    - Account information (Edit,Change sign-in, etc)
    - Help/Contact us
    - Notifications
  - The system enables linking through google accounts

----------------
5. **The system must allow users to see recent activity.**
  - The system should display the history of spendings from newest to oldest.
  - The system should display total number of expenses
  - The system should let user choose type of recent activity
  - The system should let the user choose period of time of recent activity
    - Week
    - Month
    - N Months
----------------
6. **The system must allow users to create a weekly / monthly budget and tell them if they are overspending.**
  - The system should display money spent in a week.
    - The system should breakdown the weekly report by expense categories, and see if the user had met their weekly goal by comparing how much was spent in each category subtracted by how much the user wanted to spend
  - The system should display money spent in a month.
    - The system should breakdown the monthly report by expense categories, and see if the user had met their monthly goal by comparing how much was spent in each category subtracted by how much the user wanted to spend
    - The system should also give a percentage of how close the user was to meeting their goal throughout the month
  - Built in calculator where users can get their total money spent.
----------------
7. **The system must detect security threats.**
  - After 5 failed login attempts, the system must lock the user's account.
    - The user will then be sent an email about multiple sign on attempts and be asked to reset their password, (if they believe this to be a mistake contact us with further information)
  - https://www.cr-t.com/blog/how-can-i-detect-cyber-threats/
  - https://www.cisco.com/c/dam/m/en_ca/business-transformation/pdf/5-ways-to-detect-a-cyber-attack.pdf
  - https://www.certitudesecurity.com/blog/incident-detection-response/how-to-detect-and-mitigate-cyber-threats-protecting-your-business-in-the-digital-age/
----------------


<img src="https://drive.google.com/file/d/18ixRRsbjisODKpor36xkeG3ofbzZ8eEa/view?usp=sharing"
     alt=""
     style="float: left; margin-right: 10px;" />



