from pydantic import BaseModel, Field
from typing import List, Dict, Optional, Set, Union

class ArgsItem(BaseModel):
    name: Optional[str]
    validation: Optional[str]

class WorkflowStep(BaseModel):
    name: str
    type: str
    args: Optional[Set[List[ArgsItem], List[str]]]
    output: Optional[str]

class Metadata(BaseModel):
    name: str
    authors: List[str]  
    version: str
    workflow: List[str]

class COC7Config(BaseModel):
    __metadata__: Metadata
    FillTimeBackground: WorkflowStep
    DetermineAttributes: WorkflowStep
    InputBasicInfo: WorkflowStep
    InputLuck: WorkflowStep
    SelectJob: WorkflowStep
    AssignSkills: WorkflowStep
    FillCharacterBackground: WorkflowStep
    DetermineEquipment: WorkflowStep
    ExportCharacterCard: WorkflowStep

with open('data/coc7.json', 'r', encoding='utf-8') as file:
    json_data = file.read()

config = COC7Config.model_validate_json(json_data)
print(config)
