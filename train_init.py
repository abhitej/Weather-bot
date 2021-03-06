from __future__ import absolute_import
from __future__ import division
#from __future__ import unicode_laterals

import logging, warnings
warnings.simplefilter('ignore')


from rasa_core.agent import Agent
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.policies.memoization import MemoizationPolicy

if __name__ == '__main__':
	warnings.filterwarnings(action='ignore',category=DeprecationWarning)
	logging.basicConfig(level='INFO')
	
	model_path = './models/dialogue'
	
	agent = Agent('weather_domain.yml', policies = [MemoizationPolicy(max_history = 2), KerasPolicy()])
	training_data_file = agent.load_data('./data/stories.md')
	
	agent.train(training_data_file,	epochs = 500, batch_size = 10, validation_split = 0.2)
	
	agent.persist(model_path)