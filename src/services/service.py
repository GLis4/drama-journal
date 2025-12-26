from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any, Generic, TypeVar

T = TypeVar('T')
R = TypeVar('R')

class BaseService(ABC, Generic[T, R]):
    def __init__(self, model_class: T, repository: R):
        self.model_class = model_class
        self.repository = repository

    @abstractmethod
    def find_all(self, **filters) -> List[T]:
        pass
    
    @abstractmethod
    def find(self, id: Any) -> Optional[T]:
        pass
    
    @abstractmethod
    def create(self, data: Dict[str, Any]) -> T:
        pass
    
    @abstractmethod
    def update(self, id: Any, data: Dict[str, Any]) -> Optional[T]:
        pass
    
    @abstractmethod
    def delete(self, id: Any) -> bool:
        pass

    def _build_filters(self, filters: dict) -> dict:
        conditions = []
        for field_name, value in filters.items():
            if value is None:
                continue
            
            if not hasattr(self.model_class, field_name):
                continue
            
            column = getattr(self.model_class, field_name)
            
            if isinstance(value, str) and value.strip() != "":
                conditions.append(column.ilike(f"%{value.strip()}%"))
            elif isinstance(value, (int, float)):
                conditions.append(column == value)
            elif isinstance(value, bool):
                conditions.append(column == value)
            elif isinstance(value, list):
                conditions.append(column.in_(value))
        
        return conditions