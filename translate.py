import json

def convert_dataset(input_file, output_file):
    with open(input_file, 'r') as f:
        data = json.load(f)
    
    converted_data = []
    for item in data:
        # 跳过不完整的条目
        if 'conversations' not in item or not item.get('conversations'):
            continue
            
        new_item = item.copy()
        
        # 获取sentiment和stance信息
        sentiment = item.get('sentiment', item.get('intent', 'neutral'))
        stance = item.get('stance', 'neutral')  # 从stance字段获取立场信息
        
        # 获取target并格式化（首字母大写）
        target = item.get('target', 'Harris').capitalize()
        
        # 更新human的prompt
        if 'conversations' in new_item and len(new_item['conversations']) > 0:
            human_msg = new_item['conversations'][0]
            if 'value' in human_msg:
                # 设置新的prompt格式，包含sentiment和stance
                human_msg['value'] = f"Based on this image and {target}' post, please generate a comment with sentiment: {sentiment} and stance: {stance}."
        
        converted_data.append(new_item)
    
    with open(output_file, 'w') as f:
        json.dump(converted_data, f, indent=2, ensure_ascii=False)

# 使用示例
convert_dataset('/root/autodl-tmp/MixLoRA/data/train_dataset_sentiment.json', '/root/autodl-tmp/MixLoRA/data/train_dataset_union.json')