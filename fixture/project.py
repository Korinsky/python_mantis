from model.project import Project


class ProjectHelper:
    def __init__(self, app):
        self.app = app

    def get_project_list(self):
        wd = self.app.wd
        self.open_manage_proj_page()
        project_list = []
        for row in wd.find_elements_by_xpath("//body/table[3]/tbody/tr"):
            if row.get_attribute("class") == "" or row.get_attribute("class") == "row-category":
                continue
            cells = row.find_elements_by_tag_name("td")
            name = cells[0].find_element_by_tag_name("a").text
            id = cells[0].find_element_by_tag_name("a").get_attribute("href").split("=", 1)[1]
            project_list.append(Project(name=name, id=id))
        return project_list

    def open_manage_proj_page(self):
        wd = self.app.wd
        if not wd.current_url.endswith("manage_proj_page.php"):
            wd.get(self.app.base_url + "manage_proj_page.php")

    def create_project(self, project):
        wd = self.app.wd
        self.open_manage_proj_page()
        wd.find_element_by_xpath("//input[@value='Create New Project']").click()
        self.fill_field_value("name", project.name)
        wd.find_element_by_xpath("//input[@value='Add Project']").click()

    def fill_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def delete_project_by_name(self, name):
        wd = self.app.wd
        self.open_manage_proj_page()
        self.select_project_by_name(name)
        wd.find_element_by_xpath("//input[@value = 'Delete Project']").click()
        wd.find_element_by_xpath("//input[@value = 'Delete Project']").click()

    def select_project_by_name(self, name):
        wd = self.app.wd
        wd.find_element_by_xpath("//a[text()='%s']" % name).click()