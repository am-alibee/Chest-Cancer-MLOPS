from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_url: str
    local_data_file: Path
    unzip_dir: Path


# update entity
@dataclass(frozen=True)
class PrepareBaseModelConfig:
    root_dir: Path
    base_model_path: Path
    updated_base_model_path: Path
    params_image_size: list          # Should match your params.yaml
    params_learning_rate: float
    params_include_top: bool
    params_weights: str
    params_classes: int


# update config entity for base model load
@dataclass(frozen=True)
class TrainingConfig:
    root_dir:Path
    trained_model_path:Path
    updated_base_model_path:Path
    training_data:Path
    params_epochs:int
    params_batch_size:int
    params_augumentation:bool
    params_image_size: list