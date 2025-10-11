from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.evaluation import Evaluation
from cnnClassifier import logger

STAGE_NAME = "Training Stage"

class EvaluationPipeline:
    def __init__(self):
        pass 
    
    def main(self):
        config = ConfigurationManager()
        evaluation_config = config.get_validation_config()
        evaluation = Evaluation(evaluation_config)
        evaluation.evaluate()
        evaluation.save_score()
    
if __name__ == "__main__":
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = EvaluationPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx================x")
    except Exception as e:
        logger.exception(e)
        raise e