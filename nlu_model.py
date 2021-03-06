from rasa_nlu.training_data import load_data
from rasa_nlu.config import load
from rasa_nlu.model import Trainer
from rasa_nlu.model import Interpreter, Metadata

def train_nlu(data, config, model_dir):
	training_data = load_data(data)
	trainer = Trainer(load(config))
	trainer.train(training_data)
	model_directory = trainer.persist(model_dir, fixed_model_name = 'weathernlu')

def run_nlu():
	interpreter = Interpreter.load('./models/nlu/default/weathernlu')
	print(interpreter.parse(u"I am planning my holiday to Barcelona. I wonder what is the weather out there."))

if __name__=="__main__":
	train_nlu('./data/data.json', 'config_spacy.json', './models/nlu')
	run_nlu()
