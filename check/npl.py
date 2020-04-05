import torch
from torch.utils.data import TensorDataset, DataLoader, RandomSampler, SequentialSampler
from keras.preprocessing.sequence import pad_sequences
from sklearn.model_selection import train_test_split
from pytorch_transformers import BertTokenizer, BertConfig
from pytorch_transformers import AdamW, BertForSequenceClassification
from tqdm import tqdm, trange
import pandas as pd
import io
import numpy as np
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

if device != torch.device('cpu'):
    n_gpu = torch.cuda.device_count()

def recognition(text):
    model = torch.load('classML')
    tokenizer = BertTokenizer.from_pretrained('bert-base-uncased', do_lower_case=True)
    tokenized_texts = [tokenizer.tokenize(sent) for sent in text]
    input_ids = [tokenizer.convert_tokens_to_ids(x) for x in tokenized_texts]

    input_ids = pad_sequences(
        input_ids,
        maxlen=100,
        dtype="long",
        truncating="post",
        padding="post"
    )
    attention_masks = [[float(i>0) for i in seq] for seq in input_ids]

    prediction_inputs = torch.tensor(input_ids)
    prediction_masks = torch.tensor(attention_masks)
    prediction_labels = torch.tensor(test_gt)

    prediction_data = TensorDataset(
        prediction_inputs,
        prediction_masks,
        prediction_labels
    )

    prediction_dataloader = DataLoader(
        prediction_data, 
        sampler=SequentialSampler(prediction_data),
        batch_size=32
    )
    model.eval()
    test_preds, test_labels = [], []

    for batch in prediction_dataloader:
        # добавляем батч для вычисления на GPU
        batch = tuple(t.to(device) for t in batch)
        
        # Распаковываем данные из dataloader
        b_input_ids, b_input_mask, b_labels = batch
        
        # При использовании .no_grad() модель не будет считать и хранить градиенты.
        # Это ускорит процесс предсказания меток для тестовых данных.
        with torch.no_grad():
            logits = model(b_input_ids, token_type_ids=None, attention_mask=b_input_mask)
    return logits
