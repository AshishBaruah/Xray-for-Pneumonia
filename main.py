# from src.xray import logger
# from xray import logger
# from xray.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

# ---------------------------------------------------------

import os
from xray import logger
from xray.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
# from xray.pipeline.training_pipeline import TrainingPipeline


STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>>>>> Stage {STAGE_NAME} Started <<<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>>> Stage {STAGE_NAME} Completed <<<<<<<\n\nx====================x")
     
except Exception as e:
    logger.exception(e)
    raise(e)
 
# STAGE_NAME = "Training Stage"

# if __name__ == "__main__":
#     try:
#         logger.info(f"************************")
#         logger.info(f">>>>>>> Stage {STAGE_NAME} Started <<<<<<<")
#         obj = TrainingPipeline()
#         obj.main()
#         logger.info(f">>>>>>> Stage {STAGE_NAME} Completed <<<<<<<\n\nx====================x")
        
#     except Exception as e:
#         logger.exception(e)
#         raise(e)