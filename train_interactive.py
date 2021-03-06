import logging

from rasa_core import utils, train
from rasa_core.training import interactive

logger = logging.getLogger(__name__)

def train_agent():
	return train.train_dialogue_model(domain_file = 'weather_domain.yml', 
									  stories_file = './data/stories.md',
									  output_path = './models/dialogue',
									  policy_config = 'policy_config.yml'
									  )

if __name__ == '__main__':
	utils.configure_colored_logging(loglevel = "INFO")
	agent = train_agent()
	interactive.run_interactive_learning(agent = agent, stories = './data/stories.md')