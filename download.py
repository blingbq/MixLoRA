from modelscope import snapshot_download

# 指定自定义下载路径
# model_dir = snapshot_download(
#     'Xorbits/vicuna-7b-v1.3',
#     cache_dir='/root/autodl-tmp/model'  # 替换为你想要的路径
# )



model_dir = snapshot_download(
    'AI-ModelScope/clip-vit-large-patch14',
    cache_dir='/root/autodl-tmp/model'  # 替换为你想要的路径
)
