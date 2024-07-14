import spacy
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV
from owlready2 import get_ontology, World
from spacy.lang.en.stop_words import STOP_WORDS
from spacy.lang.en.tokenizer import Tokenizer
from spacy.matcher import Matcher
from spacy.pipeline import EntityRuler
from spacy.training import Example
from spacy.vocab import Vocab
from spacy_transformers import TransformerModel
import torch
import transformers

# Veri ön işleme
def preprocess_data(data):
    nlp = spacy.load("en_core_web_sm")
    data["text"] = data["text"].apply(lambda x: nlp(x.lower()).text)
    data["text"] = data["text"].apply(lambda x: " ".join([token.lemma_ for token in nlp(x) if token.lemma_ not in STOP_WORDS]))
    return data

# Sembolik semantik
def symbolic_semantic(data, ontology_path):
    world = World()
    world.get_ontology(ontology_path).load()
    onto = world.get_ontology(ontology_path)
    matcher = Matcher(nlp.vocab)
    for concept in onto.classes():
        pattern = [{"LOWER": concept.name.lower()}]
        matcher.add(concept.name, None, *pattern)
    ruler = EntityRuler(nlp)
    ruler.add_patterns(matcher)
    nlp.add_pipe(ruler)
    data["symbolic_features"] = data["text"].apply(lambda x: [ent.label_ for ent in nlp(x).ents])
    return data

# İstatistiksel semantik
def statistical_semantic(data):
    vectorizer = TfidfVectorizer(max_features=5000)
    data["statistical_features"] = vectorizer.fit_transform(data["text"])
    return data

# Dağıtılmış semantik
def distributed_semantic(data):
    model_name = "bert-base-uncased"
    model = TransformerModel(model_name)
    nlp.add_pipe(model)
    data["distributed_features"] = data["text"].apply(lambda x: model(x).vector)
    return data

# Bilgi tabanlı semantik
def knowledge_based_semantic(data, rules_path):
    with open(rules_path, "r") as f:
        rules = f.readlines()
    rules = [rule.strip() for rule in rules]
    data["knowledge_based_features"] = data["text"].apply(lambda x: [rule for rule in rules if rule in x])
    return data

# Pragmatik semantik
def pragmatic_semantic(data):
    nlp = spacy.load("en_core_web_sm")
    data["pragmatic_features"] = data["text"].apply(lambda x: nlp(x)._.coref_clusters)
    return data

# Bilişsel semantik
def cognitive_semantic(data):
    nlp = spacy.load("en_core_web_sm")
    data["cognitive_features"] = data["text"].apply(lambda x: [token.dep_ for token in nlp(x)])
    return data

# Model entegrasyonu
def integrate_models(data):
    features = np.hstack([data["statistical_features"].toarray(), data["distributed_features"], data["symbolic_features"].apply(lambda x: np.array(x)).values, data["knowledge_based_features"].apply(lambda x: np.array(x)).values, data["
