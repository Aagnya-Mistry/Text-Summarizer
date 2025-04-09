from text_summarizer.pipeline.step_01_data_ingestion import DataIngestionTrainingPipeline
from text_summarizer.pipeline.step_02_data_validation import DataValidationTrainingPipeline
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

STEP_NAME = "Data Validation Stage"
try:
    logger.info(f">>>>>> stage {STEP_NAME} started <<<<<<")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f">>>>>> stage {STEP_NAME} completed <<<<<<")
except Exception as e:
    logger.exception(e)
    raise e
