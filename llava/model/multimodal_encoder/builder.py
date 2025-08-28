from .clip_encoder import CLIPVisionTower
import os

def build_vision_tower(vision_tower_cfg, **kwargs):
    # 获取配置中的 vision_tower
    vision_tower = getattr(vision_tower_cfg, 'mm_vision_tower', getattr(vision_tower_cfg, 'vision_tower', None))

    # 检查是否是以 "openai" 或 "laion" 开头，若是，则加载这些预训练模型
    if vision_tower.startswith("openai") or vision_tower.startswith("laion"):
        return CLIPVisionTower(vision_tower, args=vision_tower_cfg, **kwargs)
    
    # 如果是本地路径，检查该路径是否存在
    elif os.path.isdir(vision_tower):
        print(f"Loading local CLIP model from {vision_tower}")
        return CLIPVisionTower(vision_tower, args=vision_tower_cfg, **kwargs)
    
    # 如果配置不符合预期，抛出异常
    raise ValueError(f'Unknown vision tower: {vision_tower}')
