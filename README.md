# GJF


The Get_a_Job_Fast tool is here to... well help you get a job fast..

## Installation

Before running the automated job application tool, make sure to install the necessary dependencies. You can do this by executing the following command in your terminal or command prompt:

```bash
pip install -r requirements.txt
```

This command will install all the required Python packages specified in the `requirements.txt` file. Ensure that you have the appropriate version of Python installed on your system before running this command. Once the installation is complete, you're ready to set up and use the tool as outlined in the setup instructions above.

## Setup Instructions

1. **Email and Motivation Templates:**
   - Write your email and motivation templates in the corresponding `.txt` files.
   - Use the following placeholders for dynamic content:
     - `{ELEMENT_1}`: Company Name
     - `{ELEMENT_2}`: Expertise
     - `{ELEMENT_3}`: Reputation
     - `{ELEMENT_4}`: Engagement

2. **Configure Email Settings:**
   - Add your email address in the `mail.py` file.
   - If you have two-factor authentication set up on Google:
     - Generate an application password under the "Two-Factor Auth" tab on Google.
     - Place the generated key in the `secretGOOGLEkey.txt` file.
     - Use "api" instead of your regular password when prompted by the program.

3. **Run the Program:**
   - Execute the `main.py` code.
   - Complete the input boxes with the required information.
   - Click "Generate Outputs" to create `mail.txt` and `motiv.pdf` files in the output folder.
   - Review the generated files; if satisfied, click "Send" to send the email.
   - The program will update an Excel file with the sent email information for tracking purposes.

4. **Excel File Handling:**
   - If the Excel update fails, use the "Try Again" button to reattempt.
   - Check the Excel file for a record of all sent emails.

## Notes

- The program uses dynamic content placeholders to personalize each email.
- Ensure all setup steps are completed correctly to avoid errors.
- Have fun using the tool, and may you land a job swiftly!

**Disclaimer:** Use this tool responsibly and in compliance with applicable laws and regulations. The author is not responsible for any misuse or unintended consequences.
