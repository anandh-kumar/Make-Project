import json


def update(args, path):
    data = None
    with open("/home/anandh/Documents/Projects/Python/mk-project/data/projects.json", "r") as json_file:
        data = json.load(json_file)

        # Get stuffs
        project_id = data['next-project-id']
        projects = data['projects']

        # Create new project
        project = {
            'project-id': project_id,
            'project-name': args.projName,
            'project-language': args.language,
            'project-type': args.type,
            'project-path': path,
            'project-category': args.categoryName
        }
        projects.append(project)

        # Update
        data['next-project-id'] = project_id + 1
        data['projects'] = projects

    # Save it to json file
    with open("/home/anandh/Documents/Projects/Python/mk-project/data/projects.json", "w") as json_file:
        json.dump(data, json_file)
