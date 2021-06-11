#https://www.codewars.com/kata/597f334f1fe82a950500004b/train/python
get_common_directory_path=lambda _:''.join(__import__('os').path.commonprefix(_).rpartition('/')[:2])
