import os
from xray.constants import *
from xray.utils.common import read_yaml, create_directories  
from xray.entity.config_entity import (DataIngestionConfig,
                                       PrepareCallbackConfig,
                                       TrainingConfig                                      
                                    )


class ConfigurationManager:
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH):
        
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        
        create_directories([self.config.artifacts_root])
        
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        
        create_directories([config.root_dir])
        
        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_url=config.source_url,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )
        return data_ingestion_config
    
    
    
    def get_prepare_callback_config(self) -> PrepareCallbackConfig:
        config = self.config.prepare_callbacks
        model_ckpt_dir = os.path.dirname(config.checkpoint_model_filepath)
        create_directories([
            Path(model_ckpt_dir),
            Path(config.tensorboard_root_log_dir)
        ])
        
        prepare_callback_config = PrepareCallbackConfig(
            root_dir=Path(config.root_dir),
            tensorboard_root_log_dir=Path(config.tensorboard_root_log_dir),
            checkpoint_model_filepath=Path(config.checkpoint_model_filepath)
        )
        
        return prepare_callback_config
    
    
    def get_training_config(self) -> TrainingConfig:
        training = self.config.training
        params = self.params
        training_data=os.path.join(self.config.data_ingestion.unzip_dir, "chest_xray")
        create_directories([
            Path(training.root_dir)
        ])
        
        training_config=TrainingConfig(
            root_dir=Path(training.root_dir),
            trained_model_path=Path(training.trained_model_path),
            training_data=Path(training_data),
            params_epochs=params.EPOCHS,
            params_batch_size=params.BATCH_SIZE,
            params_image_size=params.IMAGE_SIZE,
            params_label=params.LABELS
        )
        
        return training_config