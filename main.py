import generateOutput,completeXcel,mail
import tkinter as tk
from tkinter import messagebox
import datetime



# PROGRAM STRUCT
#
#   1) ask user for variables
#
#   2) Generate email.txt and motiv.pdf
#
#   3) usr review
#
#   4)send the email



def output():
    # Collect parameters from the user
    entreprise = entreprise_entry.get()
    expertise = expertise_entry.get()
    milieu_de_reputation = reputation_entry.get()
    engagement = engagement_entry.get()

    motivDicoChange = {
        "{ELEMENT_1}":str(entreprise),
        "{ELEMENT_2}":str(expertise),
        "{ELEMENT_3}":str(milieu_de_reputation),
        "{ELEMENT_4}":str(engagement)
    }

    if generateOutput.generateMail(entreprise) == 0:
        if generateOutput.generateMotiv(motivDicoChange) == 0:
            # Display a message indicating that the output has been generated.
            messagebox.showinfo("Output", "Output has been correctly generated.")
        else:messagebox.showinfo("Output", "Output returned error code. See terminal for more inf0")
    else:messagebox.showinfo("Output", "Output returned error code. See terminal for more inf0")        
    
def open_file():
    try:
        """
        #method 1(not working)
        # Open and read the 'CPC-Motiv.pdf' file
        import os
        os.system("output/CPC-Motiv.pdf")
        #method 2 (not working)
        import webbrowser
        webbrowser.open_new("output/CPC-Motiv.pdf")
        #method 3 (not working fffssss)
        import subprocess
        subprocess.Popen(["output/CPC-Motiv.pdf"],shell=True)
        """
        

        # Open and read the 'email.txt' file
        with open("output/email.txt", "r",encoding="utf-8") as email_file:
            # Read the contents of the email.txt file
            email_contents = email_file.read()

        # Display the contents of the email.txt file in a message box
        messagebox.showinfo("Email Contents", email_contents)
    except FileNotFoundError:
        messagebox.showerror("File Not Found", "One or both of the files not found.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")
    
def send_mail():
    def getGoogleApiKey():
        key_path = "secretGOOGLEKey.txt"
        key_contents = ""
        try:
            with open(key_path, "r") as file:
                key_contents = file.read()
        except FileNotFoundError:
            print("The api key file does not exist.")
        except Exception as e:
            print("KeyFetchingError : An error occurred:", e)
        if key_contents:
            return key_contents
        else:
            print("KeyFetchingError: No content found in the file.")
    entreprise = entreprise_entry.get()
    personne_de_contact = contact_entry.get()
    mail_de_contact = contact_mail_entry.get()
    mdp_gmail = gmail_password_entry.get()
    
    if mdp_gmail == "api":mdp_gmail = getGoogleApiKey()
    subject = "Demande de stage - Côme Plantin-Carrenard"
    date = "sent " + str(datetime.date.today())
    
    if mail.sendEmail(mail_de_contact,subject,mdp_gmail) == 0:
        if completeXcel.write_to_excel(entreprise,personne_de_contact,date,mail_de_contact) == 0:
            messagebox.showinfo("Output", "Mail has been sent and xcel completed.")
        else:messagebox.showinfo("Mail", "Mail returned error code. See terminal for more inf0") 
    else:messagebox.showinfo("Mail", "Mail returned error code. See terminal for more inf0") 
    
def xcelOnly():
    entreprise = entreprise_entry.get()
    personne_de_contact = contact_entry.get()
    mail_de_contact = contact_mail_entry.get()
    date = "sent " + str(datetime.date.today())
    completeXcel.write_to_excel(entreprise,personne_de_contact,date,mail_de_contact)


# Create the main application window
app = tk.Tk()
app.title("Parameter Collection Interface")

# Create and position the input fields
entreprise_label = tk.Label(app, text="ENTREPRISE:")
entreprise_label.pack()
entreprise_entry = tk.Entry(app)
entreprise_entry.pack()

expertise_label = tk.Label(app, text="EXPERTISE:")
expertise_label.pack()
expertise_entry = tk.Entry(app)
expertise_entry.pack()

reputation_label = tk.Label(app, text="MILIEU DE REPUTATION:")
reputation_label.pack()
reputation_entry = tk.Entry(app)
reputation_entry.pack()

engagement_label = tk.Label(app, text="ENGAGEMENT:")
engagement_label.pack()
engagement_entry = tk.Entry(app)
engagement_entry.pack()

contact_label = tk.Label(app, text="Personne de contact:")
contact_label.pack()
contact_entry = tk.Entry(app)
contact_entry.pack()

contact_mail_label = tk.Label(app, text="Adresse mail de contact:")
contact_mail_label.pack()
contact_mail_entry = tk.Entry(app)
contact_mail_entry.pack()

gmail_password_label = tk.Label(app, text="Mdp Gmail:")
gmail_password_label.pack()
gmail_password_entry = tk.Entry(app, show="*")  # Password field
gmail_password_entry.pack()

# Create the buttons
gen_output_button = tk.Button(app, text="Gen Output", command=output)
gen_output_button.pack()

review_outputs_button = tk.Button(app, text="Review Outputs", command=open_file)
review_outputs_button.pack()

send_mail_button = tk.Button(app, text="Send Mail", command=send_mail)
send_mail_button.pack()

xcelOnly_button = tk.Button(app, text="Complete xcel(included in mail!)", command=xcelOnly)
xcelOnly_button.pack()

app.mainloop()