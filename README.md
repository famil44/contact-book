# Contact Book

A simple command-line contact book written in Python. It stores names, phone numbers and email addresses in a JSON file, so your contacts are still there the next time you run it.

## Features

- **Add** a contact with name, phone number and email
- **View** all saved contacts
- **Search** by name, phone number or email (partial matches work)
- **Edit** a contact (press Enter to keep the current value)
- **Delete** a contact, with a confirmation prompt
- **Validation** of phone numbers and emails
- **Duplicate detection** for phone numbers and emails

## How to run

1. Install Python 3.6 or newer.
2. Save `contacts.py` in a folder.
3. Open a terminal in that folder and run:

```
python contacts.py
```

(Use `python3 contacts.py` if `python` doesn't work.)

`contacts.json` is created automatically the first time you add a contact. No extra libraries are needed.

## Menu

```
1. Add  2. View  3. Search  4. Edit  5. Delete  6. Exit
```

Type the number of an option and press Enter.

## Validation rules

| Field | Rule |
|-------|------|
| Name | Cannot be empty. Saved in lowercase. |
| Phone | Exactly 10 digits. Spaces and dashes are removed before checking, so `98765-43210` is saved as `9876543210`. |
| Email | Must contain exactly one `@`, text before it, and a `.` in the part after it (not at the start or end). No spaces. Saved in lowercase. |

## Duplicate handling

- A new contact is rejected if its phone number **or** email already exists. Email comparison ignores uppercase and lowercase.
- When editing, a contact can keep its own phone and email, but cannot take another contact's.

## Data format

Contacts are stored in `contacts.json` as a list of dictionaries:

```json
[
    {
        "name": "john smith",
        "phone": "9876543210",
        "email": "john@example.com"
    }
]
```

If the file is missing, empty or damaged, the program starts with an empty contact list.

## Project structure

```
contact-book/
├── contacts.py     # the program
├── contacts.json   # created automatically when you save contacts
└── README.md
```

## Concepts practiced

- Lists and dictionaries
- File handling and the `json` module
- Functions and input validation
- Loops, conditionals and exception handling (`try/except`)
