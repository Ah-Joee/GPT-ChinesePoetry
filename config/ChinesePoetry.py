out_dir = 'out-ChinesePoetry'
eval_interval = 250 # keep frequent because we'll overfit
eval_iters = 200
log_interval = 50 # don't print too too often

# we expect to overfit on this small dataset, so only save when val improves
always_save_checkpoint = False

wandb_log = False # override via command line if you like
wandb_project = 'ChinesePoetry'
wandb_run_name = 'mini-gpt'

dataset = 'ChinesePoetry'
gradient_accumulation_steps = 1
batch_size =24
block_size = 256 # context of up to 256 previous characters

# baby GPT model :)
n_layer = 8
n_head = 8
n_embd = 512
dropout = 0.1

learning_rate = 5e-4 # with baby networks can afford to go a bit higher
max_iters = 5000
lr_decay_iters = 5000 # make equal to max_iters usually
min_lr = 5e-5 # learning_rate / 10 usually
beta2 = 0.97 # make a bit bigger because number of tokens per iter is small