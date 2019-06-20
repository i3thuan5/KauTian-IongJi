from distutils.core import setup
from os import walk
from 版本 import 版本


def 揣工具包(頭):
    'setup的find_packages無支援windows中文檔案'
    工具包 = []
    for 目錄, _, 檔案 in walk(頭):
        if '__init__.py' in 檔案:
            工具包.append(目錄.replace('/', '.'))
    return 工具包


github網址 = 'https://github.com/i3thuan5/kau3-tian2_iong7-ji7'


setup(
    name='kau3-tian2_iong7-ji7',
    packages=揣工具包('用字'),
    version=版本,
    description='教典用字',
    long_description='教育部辭典台語用字',
    author='薛丞宏',
    author_email='ihcaoe@gmail.com',
    url='https://xn--v0qr21b.xn--kpry57d/',
    download_url=github網址,
    keywords=[
        '語料庫',
        'Taiwan', 'Natural Language', 'Corpus',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Operating System :: Unix',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Text Processing',
        'Topic :: Text Processing :: Linguistic',
    ],
    install_requires=[
        'tai5-uan5_gian5-gi2_kang1-ku7',
        'django',
    ],
    package_data={
        '用字': [
            '教典.json',
            '甘字典.json',
        ],
    }
)
