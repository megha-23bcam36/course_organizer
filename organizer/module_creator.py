# organizer/module_creator.py

import os

def create_module(course_name, topics):
    folder_name = course_name.lower().replace(" ", "_")
    os.makedirs(folder_name, exist_ok=True)

    with open(os.path.join(folder_name, '__init__.py'), 'w') as f:
        f.write(f"# {course_name} module\n")

    with open(os.path.join(folder_name, 'topics.txt'), 'w') as f:
        for topic in topics:
            f.write(f"{topic}\n")

    print(f"Module '{course_name}' created with topics.")
