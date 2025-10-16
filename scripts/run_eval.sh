# model_path=$1 # /path/to/model/
# data_dir=$2 # /path/to/mixlora_data/mm_tasks


# python -m llava.cmoa_eval.evaluate \
#     --eval_mixlora \
#     --model-base "lmsys/vicuna-7b-v1.3" \
#     --question-dir $data_dir \
#     --image-folder $data_dir \
#     --model-path $model_path \

model_path=/root/autodl-tmp/MixLoRA/checkpoints/stance_mixlora_input_E-16_r-8_union2
image_folder=/root/autodl-tmp/MixLoRA/data/images
question_file=/root/autodl-tmp/MixLoRA/data/images

python -m llava.cmoa_eval.evaluate \
    --model-base "/root/autodl-tmp/model/Xorbits/vicuna-7b-v1.3" \
    --model-path $model_path \
    --image-folder $image_folder \
    --question-dir $question_file \
    --temperature 0.5 \
    --eval_mixlora \
    