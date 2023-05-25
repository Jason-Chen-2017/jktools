from moviepy.editor import *


def convert_mp4_to_gif(input_file, output_file):
    # 加载视频文件
    video = VideoFileClip(filename=input_file)

    # 可选：你可以使用 resize 或其他方法来调整视频的尺寸、裁剪等
    # video = video.resize(0.5)  # 如果需要，调整尺寸为原始大小的50%

    # 转换视频文件为 GIF
    video.write_gif(
        filename=output_file,
        # Number of frames per second
        fps=1,
        program='imageio',
        opt='nq',
        fuzz=1,
        verbose=True,
        loop=0,
        dispose=False,
        colors=None,
        tempfiles=False,
        logger='bar'
    )


file_name = 'attention_process'

if __name__ == "__main__":
    data_path = '/Users/bytedance/code/untitled/data/'
    input_file = data_path + file_name + '.mp4'
    output_file = data_path + file_name + '.gif'
    convert_mp4_to_gif(input_file, output_file)
