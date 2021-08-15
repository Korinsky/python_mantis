from model.project import Project
import random


def test_del_project(app):
    app.session.login("administrator", "root")
    old_projects = app.project.get_project_list()
    if len(old_projects) == 0:
        app.project.create_project(Project(name="Autotest" + str(random.randint(0, 10000))))
        old_projects = app.project.get_project_list()
    index = random.randrange(len(old_projects))
    app.project.delete_project_by_name(old_projects[index].name)
    new_projects = app.project.get_project_list()
    assert len(old_projects) - 1 == len(new_projects)
    old_projects[index:index + 1] = []
    assert old_projects == new_projects
