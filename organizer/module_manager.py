# organizer/module_manager.py

import os
import json
import shutil
from organizer.module_creator import create_module

def list_modules():
    exclude = {'organizer', 'examples', '__pycache__'}
    folders = [f for f in os.listdir() if os.path.isdir(f) and f not in exclude and not f.endswith('.egg-info')]

    if not folders:
        print("No course modules found.")
    else:
        print("Available Course Modules:")
        for f in folders:
            print(f"- {f}")

def view_topics():
    module = input("Enter module folder name: ").strip().lower().replace(" ", "_")
    topics_file = os.path.join(module, 'topics.txt')

    if os.path.exists(topics_file):
        print(f"\nTopics in '{module}':")
        with open(topics_file, 'r') as f:
            for line in f:
                print(f"- {line.strip()}")
    else:
        print("Module not found or missing topics.txt")

def edit_topics():
    module = input("Enter module folder name to edit: ").strip().lower().replace(" ", "_")
    topics_file = os.path.join(module, 'topics.txt')

    if os.path.exists(topics_file):
        print("Current topics:")
        with open(topics_file, 'r') as f:
            for i, line in enumerate(f, 1):
                print(f"{i}. {line.strip()}")

        new_topics = input("\nEnter new topics (comma-separated): ").split(',')
        with open(topics_file, 'w') as f:
            for topic in new_topics:
                f.write(f"{topic.strip()}\n")
        print("Topics updated.")
    else:
        print("Module not found or missing topics.txt")

def delete_module():
    module = input("Enter module folder name to delete: ").strip().lower().replace(" ", "_")
    if os.path.exists(module) and os.path.isdir(module):
        confirm = input(f"Are you sure you want to delete '{module}'? This cannot be undone. (yes/no): ").lower()
        if confirm == 'yes':
            shutil.rmtree(module)
            print(f"Module '{module}' deleted.")
        else:
            print("Cancelled.")
    else:
        print("Module not found.")

def export_to_json():
    module = input("Enter module folder name to export: ").strip().lower().replace(" ", "_")
    topics_file = os.path.join(module, 'topics.txt')

    if os.path.exists(topics_file):
        with open(topics_file, 'r') as f:
            topics = [line.strip() for line in f.readlines()]

        data = {
            "module_name": module,
            "topics": topics
        }

        json_file = f"{module}_topics.json"
        with open(json_file, 'w') as f:
            json.dump(data, f, indent=4)

        print(f"Exported to {json_file}")
    else:
        print("Module not found or missing topics.txt")

def main():
    print("Welcome to Course Module Organizer")
    while True:
        print("\n1. Create Module")
        print("2. List Modules")
        print("3. View Topics")
        print("4. Edit Topics")
        print("5. Delete Module")
        print("6. Export to JSON")
        print("7. Exit")

        choice = input("Choose: ")

        if choice == '1':
            name = input("Course Name: ")
            topics = input("Topics (comma-separated): ").split(',')
            create_module(name.strip(), [t.strip() for t in topics])
        elif choice == '2':
            list_modules()
        elif choice == '3':
            view_topics()
        elif choice == '4':
            edit_topics()
        elif choice == '5':
            delete_module()
        elif choice == '6':
            export_to_json()
        elif choice == '7':
            break
        else:
            print("Invalid choice.")
