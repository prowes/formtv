torchrun --nproc_per_node 2 example_chat_completion.py \
    --ckpt_dir /home/iv/llama/llama-2-13b-chat/ \
    --tokenizer_path /home/iv/llama/tokenizer.model \
    --max_seq_len 512 --max_batch_size 6