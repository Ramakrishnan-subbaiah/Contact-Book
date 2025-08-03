import pandas as pd
import os

FILE_NAME = "contacts.csv"
COLUMNS = ['Name', 'Phone', 'Email', 'Address']

# Load contacts or create an empty file
def load_contacts():
    if os.path.exists(FILE_NAME):
        return pd.read_csv(FILE_NAME)
    else:
        return pd.DataFrame(columns=COLUMNS)

# Save DataFrame to CSV
def save_contacts(df):
    df.to_csv(FILE_NAME, index=False)

# Add a new contact
def add_contact(df):
    name = input("Enter Name: ")
    phone = input("Enter Phone: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")
    df.loc[len(df)] = [name, phone, email, address]
    print("✅ Contact added.")
    return df

# View all contacts
def view_contacts(df):
    if df.empty:
        print("📭 No contacts found.")
    else:
        print("\n📋 All Contacts:")
        print(df)

# Search contact by name
def search_contact(df):
    name = input("Enter name to search: ").lower()
    result = df[df['Name'].str.lower().str.contains(name)]
    print(result if not result.empty else "❌ No matching contact.")

# Update a contact
def update_contact(df):
    name = input("Enter name of contact to update: ").lower()
    index = df[df['Name'].str.lower() == name].index
    if not index.empty:
        print("Leave field empty to keep existing value.")
        for i in index:
            print(f"Updating contact: {df.loc[i, 'Name']}")
            for col in COLUMNS:
                new_val = input(f"{col} ({df.loc[i, col]}): ")
                if new_val:
                    df.at[i, col] = new_val
        print("✅ Contact updated.")
    else:
        print("❌ Contact not found.")
    return df

# Delete a contact
def delete_contact(df):
    name = input("Enter name of contact to delete: ").lower()
    df_new = df[~df['Name'].str.lower().str.contains(name)]
    if len(df_new) != len(df):
        print("🗑️ Contact deleted.")
    else:
        print("❌ Contact not found.")
    return df_new

# Main menu
def main():
    df = load_contacts()

    while True:
        print("\n--- Contact Book Menu ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            df = add_contact(df)
        elif choice == '2':
            view_contacts(df)
        elif choice == '3':
            search_contact(df)
        elif choice == '4':
            df = update_contact(df)
        elif choice == '5':
            df = delete_contact(df)
        elif choice == '6':
            save_contacts(df)
            print("💾 Contacts saved. Exiting.")
            break
        else:
            print("❗ Invalid option. Try again.")

if __name__ == "__main__":
    main()