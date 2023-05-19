problem_list_path = '../data/base/problem_lists/'
data_root = '../data/'
base_path = '../data/base/'
model_data_path = '../data/models/'
results_path = '../results/'
metrics_path = '../data/metrics/'
xml_name = 'problem'
data_path = '../data/base/problems_with_tag50.xml'
feature = 'text'
label = 'tag'

model_name = 'lstm'
model_path = 'cpc_lstm.model'
threshold = 0.5
max_length = 200
epoch = 100
batch_size = 20
num_classes = 50
learning_rate = 1e-4
schedule = 'constant'
exp_gamma = 0.9999
warmup = 0
max_iters = 0
decay_start = 0

bert_name = 'bert-base-uncased'
hidden_dropout_prob = 0.3
weight_decay = 0.01

conv_sizes = [2, 3, 4, 5]

vocab_len = 3000000
vec_dim = 300
# hidden_dim = 20
num_kernel = 100
cnn_dropout = 0.15
num_layers = 3

single_label = False
