import gpt_2_simple as gpt2
import os
import requests
import tensorflow as tf

model_name = "774M"
# if not os.path.isdir(os.path.join("models", model_name)):
# 	print(f"Downloading {model_name} model...")
# 	gpt2.download_gpt2(model_name=model_name)   # model is saved into current directory under /models/124M/

file_name = "new_text.txt"
    
sess = gpt2.start_tf_sess()
tf.compat.v1.reset_default_graph()
sess.close()


sess = gpt2.start_tf_sess()



gpt2.finetune(sess,
            file_name,
            model_name=model_name,
			run_name='run2',
            steps=1000)   #s steps is max number of training steps

gpt2.generate(sess)

gpt2.load_gpt2(sess, run_name='run2')
single_text = gpt2.generate(sess, return_as_list=True, prefix='<|startoftext|>', include_prefix=False, truncate='<|endoftext|>')[0]
print(single_text)