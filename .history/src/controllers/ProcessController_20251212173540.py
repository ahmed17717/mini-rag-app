from .BaseController import BaseController
from .ProjectController import ProjectController

class ProcessController(BaseController):
  def __init__(self, project_id:str):
    super().__init__()

    self.project_id = project_id