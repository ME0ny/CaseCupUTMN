# coding: utf-8
import sys
import codecs
import numpy as np
from keras_bert import load_trained_model_from_checkpoint
import tokenization

# папка, куда распаковали преодобученную нейросеть BERT
folder = 'multi_cased_L-12_H-768_A-12'

config_path = folder+'/bert_config.json'
checkpoint_path = folder+'/bert_model.ckpt'
vocab_path = folder+'/vocab.txt'

# создаем объект для перевода строки с пробелами в токены
tokenizer = tokenization.FullTokenizer(vocab_file=vocab_path, do_lower_case=False)

# загружаем модель
model = load_trained_model_from_checkpoint(config_path, checkpoint_path, training=True)

def overlaps(client,collabor):
    sentence_1 = client      #@param {type:"string"}
    sentence_2 = collabor          #@param {type:"string"}

    # строки в массивы токенов
    tokens_sen_1 = tokenizer.tokenize(sentence_1)
    tokens_sen_2 = tokenizer.tokenize(sentence_2)

    tokens = ['[CLS]'] + tokens_sen_1 + ['[SEP]'] + tokens_sen_2 + ['[SEP]']

    # преобразуем строковые токены в числовые индексы:
    token_input = tokenizer.convert_tokens_to_ids(tokens)  
    # удлиняем до 512      
    token_input = token_input + [0] * (512 - len(token_input))

    # маска в этом режиме все 0
    mask_input = [0] * 512

    # в маске предложений под второй фразой, включая конечный SEP, надо поставить 1, а все остальное заполнить 0
    seg_input = [0]*512
    len_1 = len(tokens_sen_1) + 2                   # длина первой фразы, +2 - включая начальный CLS и разделитель SEP
    for i in range(len(tokens_sen_2)+1):            # +1, т.к. включая последний SEP
            seg_input[len_1 + i] = 1                # маскируем вторую фразу, включая последний SEP, единицами
    #print(seg_input)


    # конвертируем в numpy в форму (1,) -> (1,512)
    token_input = np.asarray([token_input])
    mask_input = np.asarray([mask_input])
    seg_input = np.asarray([seg_input])


    # пропускаем через нейросеть...
    predicts = model.predict([token_input, seg_input, mask_input])[1]       # в [1] ответ на вопрос, является ли второе предложение логичным по смыслу
    #print('Sentence is okey: ', not bool(np.argmax(predicts, axis=-1)[0]), predicts)
    print('Sentence is okey:', int(round(predicts[0][0]*100)), '%')                    
    out = int(round(predicts[0][0]*100)) 
    
    return out