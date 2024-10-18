import gradio as gr

# 项目地址: /Volumes/2T/com/yanghoo205/OutfitPlannerAI

def season_module(season):
    if season == "spring":
        return ["薄针织衫", "风衣", "牛仔裤", "薄围巾"]
    elif season == "summer":
        return ["轻薄T恤", "连衣裙", "短裤", "防晒衣"]
    elif season == "autumn":
        return ["轻外套", "毛衣", "长裤", "围巾"]
    elif season == "winter":
        return ["厚外套", "羽绒服", "毛衣", "保暖裤"]

def temperature_module(temperature):
    if temperature >= 25:
        return ["短袖T恤", "短裤", "凉鞋"]
    elif 15 <= temperature < 25:
        return ["薄长袖", "牛仔裤", "运动鞋"]
    elif 5 <= temperature < 15:
        return ["毛衣", "外套", "长裤", "短靴"]
    else:
        return ["厚毛衣", "羽绒服", "保暖裤", "保暖靴"]

def occasion_module(occasion):
    if occasion == "work":
        return ["简约风", "衬衫", "西装裤"]
    elif occasion == "casual":
        return ["舒适风", "牛仔裤", "T恤"]
    elif occasion == "formal":
        return ["优雅风", "长裙", "高跟鞋"]

def color_module(base_color, accent_color):
    return f"基础色：{base_color}, 点缀色：{accent_color}"

def accessories_module(season):
    if season == "spring" or season == "autumn":
        return ["丝巾", "帽子"]
    elif season == "summer":
        return ["墨镜", "发带"]
    elif season == "winter":
        return ["围巾", "手套", "帽子"]

def detailed_sweater(style, thickness, material, pattern):
    style_item = sweater_style_module(style)
    thickness_item = sweater_thickness_module(thickness)
    material_item = sweater_material_module(material)
    pattern_item = sweater_pattern_module(pattern)
    
    return f"{thickness_item}, {material_item}, {style_item}, {pattern_item}"

def outfit_recommendation(season, temperature, occasion, base_color, accent_color):
    season_items = season_module(season)
    temperature_items = temperature_module(temperature)
    occasion_items = occasion_module(occasion)
    colors = color_module(base_color, accent_color)
    accessories = accessories_module(season)
    
    outfit = {
        "季节搭配": season_items,
        "温度适配": temperature_items,
        "场景风格": occasion_items,
        "颜色选择": colors,
        "配饰": accessories
    }
    
    return outfit

def recommend_outfit(season, temperature, occasion, base_color, accent_color):
    recommendation = outfit_recommendation(season, temperature, occasion, base_color, accent_color)
    return recommendation

# 使用 Gradio 创建一个界面
demo = gr.Interface(
    fn=recommend_outfit,
    inputs=[
        gr.Dropdown(choices=["spring", "summer", "autumn", "winter"], label="季节 (Season)"),
        gr.Slider(minimum=-10, maximum=40, step=1, label="温度 (Temperature in °C)"),
        gr.Dropdown(choices=["work", "casual", "formal"], label="场景 (Occasion)"),
        gr.Textbox(label="基础颜色 (Base Color)"),
        gr.Textbox(label="点缀颜色 (Accent Color)"),
    ],
    outputs="json",
    title="衣服搭配推荐系统 (Outfit Recommendation System)",
    description="输入季节、温度、场景和颜色，获取适合的衣服搭配建议。",
)

if __name__ == "__main__":
    demo.launch()
