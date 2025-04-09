from text_summarizer.pipeline.step_01_data_ingestion import DataIngestionTrainingPipeline
from text_summarizer.logging import logger

STEP_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>>>> stage {STEP_NAME} started <<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> stage {STEP_NAME} completed <<<<<<")
except Exception as e:
    logger.exception(e)
    raise e
